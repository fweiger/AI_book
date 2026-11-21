#!/usr/bin/env bash
# TOPIC-017 / AC-05: true public HG002 chr20:2-3Mb bcftools + RTG vcfeval.
# No downloads, package installs, personal DNA, Docker, or Git uploads.
set -euo pipefail
MODE="${1:-preflight}"
: "${WGS_WORK_DIR:?Set absolute directory containing G8 public HG002 input/reference/benchmark/metadata}"
: "${WGS_EVAL_DIR:?Set absolute NEW output directory outside public Git checkout}"
: "${BCFTOOLS_BIN:?Set path to existing bcftools 1.19 executable}"
: "${RTG_BIN:?Set path to existing RTG Tools 3.13 executable}"
THREADS="${WGS_THREADS:-4}"
[[ "$MODE" == preflight || "$MODE" == run ]] || { echo 'Usage: script [preflight|run]' >&2; exit 2; }
[[ "$WGS_WORK_DIR" == /* && "$WGS_EVAL_DIR" == /* ]] || { echo 'Absolute paths required' >&2; exit 2; }
[[ "$THREADS" =~ ^[1-9][0-9]*$ ]] || { echo 'Invalid WGS_THREADS' >&2; exit 2; }
if [[ -n "${BCFTOOLS_LIB_DIR:-}" ]]; then
  export LD_LIBRARY_PATH="$BCFTOOLS_LIB_DIR${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
fi
d="$WGS_WORK_DIR"
ref="$d/reference/GCA_000001405.15_GRCh38_no_alt_analysis_set.fasta"
fai="$d/reference/GCA_000001405.15_GRCh38_no_alt_analysis_set.fasta.fai"
bam="$d/input/HG002.novaseq.pcr-free.35x.dedup.grch38_no_alt.chr20.bam"
truth="$d/benchmark/HG002_GRCh38_1_22_v4.2.1_benchmark.vcf.gz"
bed="$d/benchmark/HG002_GRCh38_1_22_v4.2.1_benchmark_noinconsistent.bed"
for f in "$ref" "$fai" "$bam" "$bam.bai" "$truth" "$truth.tbi" "$bed" "$d/metadata/sha256-inputs.txt"; do
  [[ -s "$f" ]] || { echo "Missing public input: $f" >&2; exit 3; }
done
"$BCFTOOLS_BIN" --version | head -2
"$RTG_BIN" version | grep -E '^Product:|^Core Version:' || true
if [[ "$MODE" == preflight ]]; then
  echo "DATA_PATHS_PRESENT; no sequencing analysis performed."
  exit 0
fi

# No accidental overwriting of a prior real benchmark.
[[ ! -e "$WGS_EVAL_DIR" ]] || { echo "Refusing existing output: $WGS_EVAL_DIR" >&2; exit 4; }
mkdir -p "$WGS_EVAL_DIR"
out="$WGS_EVAL_DIR"
(cd "$d" && sha256sum -c metadata/sha256-inputs.txt) > "$out/inputs-checksums.log"
date -u +%FT%TZ > "$out/start-utc.txt"
{
  echo "WGS_THREADS=$THREADS; fixed region chr20:2000000-3000000"
  echo "bcftools command: mpileup -Ou -d 250 --threads $THREADS -f <fasta> -r chr20:2000000-3000000 <bam> | call -m -v --ploidy 2 -Oz --threads $THREADS"
  /usr/bin/time -f 'elapsed_sec=%e max_rss_kb=%M' \
    bash -o pipefail -c '"$1" mpileup -Ou --max-depth 250 --threads "$2" -f "$3" -r chr20:2000000-3000000 "$4" | "$1" call -m -v --ploidy 2 -Oz --threads "$2" -o "$5"' \
    _ "$BCFTOOLS_BIN" "$THREADS" "$ref" "$bam" "$out/HG002.chr20_2-3Mb.bcftools.calls.vcf.gz"
} > "$out/caller.log" 2>&1
"$BCFTOOLS_BIN" index -t "$out/HG002.chr20_2-3Mb.bcftools.calls.vcf.gz"

# Extract chr20 reference by the verified GRCh38 no-alt FASTA index.
python3 - "$ref" "$fai" "$out/chr20.fa" "$bed" "$out/confident.chr20_2-3Mb.bed" <<'PY'
import sys
from pathlib import Path
ref,fai,out,bed,outbed=map(Path,sys.argv[1:])
line=next(x for x in fai.read_text().splitlines() if x.startswith('chr20\t'))
_,L,offset,line_bases,line_width,*_=line.split('\t')
L,offset,line_bases,line_width=map(int,(L,offset,line_bases,line_width))
with ref.open('rb') as inp:
    inp.seek(offset)
    raw=inp.read(L+((L+line_bases-1)//line_bases)*(line_width-line_bases)+10)
seq=raw.replace(b'\n',b'').replace(b'\r',b'')[:L]
assert len(seq)==L and L==64444167, 'chr20 reference extraction length mismatch'
with out.open('wb') as w:
    w.write(b'>chr20\n')
    for i in range(0,L,60):w.write(seq[i:i+60]+b'\n')
count=bp=0
with bed.open() as inp,outbed.open('w') as w:
    for line in inp:
        t=line.split('\t')
        if t[0]!='chr20':continue
        a,b=max(2000000,int(t[1])),min(3000000,int(t[2]))
        if a<b:
            w.write(f'chr20\t{a}\t{b}\n')
            count+=1;bp+=b-a
assert count>0 and bp>0, 'GIAB confident region empty'
print('CONFIDENT_BED',count,'intervals',bp,'bases')
PY

"$BCFTOOLS_BIN" view -r chr20:2000000-3000000 -Oz \
  -o "$out/GIAB_v4.2.1.chr20_2-3Mb.truth.vcf.gz" "$truth"
"$BCFTOOLS_BIN" index -t "$out/GIAB_v4.2.1.chr20_2-3Mb.truth.vcf.gz"
"$RTG_BIN" format -o "$out/chr20.sdf" "$out/chr20.fa" > "$out/rtg-format.log" 2>&1
"$RTG_BIN" vcfeval \
  --baseline="$out/GIAB_v4.2.1.chr20_2-3Mb.truth.vcf.gz" \
  --calls="$out/HG002.chr20_2-3Mb.bcftools.calls.vcf.gz" \
  --template="$out/chr20.sdf" \
  --evaluation-regions="$out/confident.chr20_2-3Mb.bed" \
  --roc-subset=snp,indel --vcf-score-field=QUAL --threads="$THREADS" \
  --output="$out/vcfeval" > "$out/vcfeval-stdout.log" 2>&1

# Report the full/unfiltered end of each ROC, not the post-hoc max F1 cut-off.
python3 - "$out/vcfeval" "$out/no-extra-quality-filter.tsv" <<'PY'
import gzip,sys
from pathlib import Path
folder,output=map(Path,sys.argv[1:])
with output.open('w') as w:
    w.write('class\tbaseline_n\tcall_n\ttp_baseline\ttp_call\tfp\tfn\tprecision\trecall\tf1\n')
    for name in ('snp','indel','weighted'):
        with gzip.open(folder/(name+'_roc.tsv.gz'),'rt') as inp:
            rows=inp.read().splitlines()
        get=lambda label:next(int(s.split(':',1)[1].strip()) for s in rows if s.startswith(label))
        baseline=get('#total baseline variants:');calls=get('#total call variants:')
        last=[r for r in rows if r and not r.startswith('#')][-1].split('\t')
        assert len(last)==8
        w.write('\t'.join([name,str(baseline),str(calls),last[1],last[3],last[2],last[4],last[5],last[6],last[7]])+'\n')
PY
(
  cd "$out"
  sha256sum HG002.chr20_2-3Mb.bcftools.calls.vcf.gz GIAB_v4.2.1.chr20_2-3Mb.truth.vcf.gz confident.chr20_2-3Mb.bed vcfeval/summary.txt vcfeval/snp_roc.tsv.gz vcfeval/indel_roc.tsv.gz no-extra-quality-filter.tsv > sha256-outputs.txt
)
date -u +%FT%TZ > "$out/end-utc.txt"
cat "$out/no-extra-quality-filter.tsv"
echo "DONE: Public HG002 chr20 limited benchmark only; no personal or clinical conclusions."

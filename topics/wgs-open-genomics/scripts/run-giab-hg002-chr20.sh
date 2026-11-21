#!/usr/bin/env bash
# TOPIC-017 / AC-05. Public HG002 chr20 variant-call benchmark.
# Commands adapted from google/deepvariant r1.10 deeptrio-wgs-case-study.
# Does not process private genome data. First action is safe preflight.
set -euo pipefail
MODE="${1:-preflight}"
WORK_DIR="${WGS_WORK_DIR:-}"
DEEPVARIANT_IMAGE="google/deepvariant:1.10.0"
HAPPY_IMAGE="jmcdani20/hap.py:v0.3.12"
THREADS="${WGS_THREADS:-4}"

usage() {
  cat <<'EOF'
Usage:
  bash run-giab-hg002-chr20.sh preflight
  WGS_WORK_DIR=/absolute/path WGS_THREADS=4 bash run-giab-hg002-chr20.sh fetch
  WGS_WORK_DIR=/absolute/path WGS_THREADS=4 bash run-giab-hg002-chr20.sh run
The default mode performs NO download or analysis. Files are public HG002 only.
Warning: benchmark v4.2.1 is a fixed reproducibility baseline, not NIST's newest HG002 benchmark.
EOF
}

if [[ "$MODE" == "preflight" ]]; then
  usage
  for tool in curl gzip sha256sum docker; do
    if command -v "$tool" >/dev/null 2>&1; then
      printf 'FOUND %s\n' "$tool"
    else
      printf 'MISSING %s\n' "$tool"
    fi
  done
  if [[ -n "$WORK_DIR" ]]; then printf 'WGS_WORK_DIR=%s\n' "$WORK_DIR"; fi
  exit 0
fi

[[ "$MODE" == "fetch" || "$MODE" == "run" ]] || { usage; exit 2; }
[[ "$WORK_DIR" == /* ]] || { echo 'ERROR: WGS_WORK_DIR must be an absolute path outside the public repository' >&2; exit 2; }
[[ "$THREADS" =~ ^[1-9][0-9]*$ ]] || { echo 'ERROR: WGS_THREADS must be positive integer' >&2; exit 2; }
mkdir -p "$WORK_DIR"/{input,reference,benchmark,output,happy,metadata}
cd "$WORK_DIR"

REF_PREFIX='GCA_000001405.15_GRCh38_no_alt_analysis_set'
REF_URL="https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/000/001/405/GCA_000001405.15_GRCh38/seqs_for_alignment_pipelines.ucsc_ids"
TRUTH_PREFIX='HG002_GRCh38_1_22_v4.2.1_benchmark'
TRUTH_URL='https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/release/AshkenazimTrio/HG002_NA24385_son/NISTv4.2.1/GRCh38'
BAM_NAME='HG002.novaseq.pcr-free.35x.dedup.grch38_no_alt.chr20.bam'
BAM_URL='https://storage.googleapis.com/deepvariant/case-study-testdata'

fetch_one() {
  local url="$1" dest="$2"
  if [[ -s "$dest" ]]; then printf 'EXISTS %s\n' "$dest"; return 0; fi
  printf 'FETCH %s\n' "$url"
  curl --fail --location --retry 3 --retry-delay 3 --connect-timeout 30 --continue-at - --output "${dest}.part" "$url"
  [[ -s "${dest}.part" ]] || { echo "ERROR: empty download: $dest" >&2; exit 3; }
  mv "${dest}.part" "$dest"
}

if [[ "$MODE" == "fetch" ]]; then
  for cmd in curl gzip sha256sum; do command -v "$cmd" >/dev/null || { echo "MISSING $cmd" >&2; exit 2; }; done
  fetch_one "$REF_URL/$REF_PREFIX.fna.gz" "reference/$REF_PREFIX.fna.gz"
  gzip -t "reference/$REF_PREFIX.fna.gz"
  if [[ ! -s "reference/$REF_PREFIX.fasta" ]]; then gzip -dc "reference/$REF_PREFIX.fna.gz" > "reference/$REF_PREFIX.fasta.part" && mv "reference/$REF_PREFIX.fasta.part" "reference/$REF_PREFIX.fasta"; fi
  fetch_one "$REF_URL/$REF_PREFIX.fna.fai" "reference/$REF_PREFIX.fasta.fai"
  fetch_one "$TRUTH_URL/$TRUTH_PREFIX.vcf.gz" "benchmark/$TRUTH_PREFIX.vcf.gz"
  fetch_one "$TRUTH_URL/$TRUTH_PREFIX.vcf.gz.tbi" "benchmark/$TRUTH_PREFIX.vcf.gz.tbi"
  fetch_one "$TRUTH_URL/${TRUTH_PREFIX}_noinconsistent.bed" "benchmark/${TRUTH_PREFIX}_noinconsistent.bed"
  fetch_one "$BAM_URL/$BAM_NAME" "input/$BAM_NAME"
  fetch_one "$BAM_URL/$BAM_NAME.bai" "input/$BAM_NAME.bai"
  gzip -t "benchmark/$TRUTH_PREFIX.vcf.gz"
  find input reference benchmark -type f ! -name '*.part' -print0 | sort -z | xargs -0 sha256sum > metadata/sha256-inputs.txt
  printf 'Fetched files with checksums in %s/metadata/sha256-inputs.txt\n' "$WORK_DIR"
  exit 0
fi

command -v docker >/dev/null || { echo 'ERROR: docker not installed' >&2; exit 2; }
for x in "reference/$REF_PREFIX.fasta" "reference/$REF_PREFIX.fasta.fai" "benchmark/$TRUTH_PREFIX.vcf.gz" "benchmark/$TRUTH_PREFIX.vcf.gz.tbi" "benchmark/${TRUTH_PREFIX}_noinconsistent.bed" "input/$BAM_NAME" "input/$BAM_NAME.bai"; do
  [[ -s "$x" ]] || { echo "ERROR: missing input $x; run fetch mode first" >&2; exit 3; }
done
# Record container image digests for provenance.
docker pull "$DEEPVARIANT_IMAGE"
docker pull "$HAPPY_IMAGE"
(docker image inspect --format '{{json .RepoDigests}}' "$DEEPVARIANT_IMAGE"; docker image inspect --format '{{json .RepoDigests}}' "$HAPPY_IMAGE") > metadata/image-digests.txt

docker run --rm \
  -v "$WORK_DIR/input:/input:ro" -v "$WORK_DIR/reference:/reference:ro" -v "$WORK_DIR/output:/output" \
  "$DEEPVARIANT_IMAGE" /opt/deepvariant/bin/run_deepvariant \
  --model_type=WGS --ref="/reference/$REF_PREFIX.fasta" --reads="/input/$BAM_NAME" \
  --output_vcf=/output/HG002.chr20.calls.vcf.gz --output_gvcf=/output/HG002.chr20.calls.g.vcf.gz \
  --regions=chr20 --num_shards="$THREADS"

docker run --rm \
  -v "$WORK_DIR/benchmark:/benchmark:ro" -v "$WORK_DIR/reference:/reference:ro" \
  -v "$WORK_DIR/output:/output:ro" -v "$WORK_DIR/happy:/happy" \
  "$HAPPY_IMAGE" /opt/hap.py/bin/hap.py \
  "/benchmark/$TRUTH_PREFIX.vcf.gz" /output/HG002.chr20.calls.vcf.gz \
  -f "/benchmark/${TRUTH_PREFIX}_noinconsistent.bed" \
  -r "/reference/$REF_PREFIX.fasta" \
  -o /happy/HG002.chr20 --engine=vcfeval --pass-only -l chr20
[[ -s happy/HG002.chr20.summary.csv ]] || { echo 'ERROR: missing hap.py summary' >&2; exit 4; }
sha256sum output/HG002.chr20.calls.vcf.gz happy/HG002.chr20.summary.csv > metadata/sha256-outputs.txt
printf 'DONE: see %s/happy/HG002.chr20.summary.csv\n' "$WORK_DIR"

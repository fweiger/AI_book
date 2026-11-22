#!/usr/bin/env python3
"""Reproduce TOPIC-013's 16 modern-DEM crossing scenarios (NOT ancient roads).
Uses read-only public AWS Mapzen Terrain Tiles. Requirements: numpy scipy Pillow.
Writes CSV to stdout; makes no local file changes.
"""
import io, math, urllib.request
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

ZOOM=10
W,S,E,N=112.60,35.62,113.30,35.95
BLOCK=4
def project(lat,lon):
    z=2**ZOOM
    return ((lon+180)/360*z,(1-math.asinh(math.tan(math.radians(lat)))/math.pi)*z/2)

def load_slope():
    xw,yn=project(N,W);xe,ys=project(S,E)
    xa,xb=math.floor(xw),math.floor(xe)
    ya,yb=math.floor(yn),math.floor(ys)
    tiles={}
    for y in range(ya,yb+1):
        for x in range(xa,xb+1):
            url=f'https://s3.amazonaws.com/elevation-tiles-prod/geotiff/{ZOOM}/{x}/{y}.tif'
            with urllib.request.urlopen(url,timeout=25) as resp:
                tiles[x,y]=np.asarray(Image.open(io.BytesIO(resp.read())),dtype=np.float64)
    mosaic=np.vstack([np.hstack([tiles[x,y] for x in range(xa,xb+1)]) for y in range(ya,yb+1)])
    sx,sy=int(round((xw-xa)*512)),int(round((yn-ya)*512))
    ex,ey=int(round((xe-xa)*512)),int(round((ys-ya)*512))
    elev=mosaic[sy:ey,sx:ex]
    if elev.size==0 or (elev<-1000).any():raise ValueError('Unexpected DEM void')
    meter=76.43702828517416*math.cos(math.radians((S+N)/2))
    dy,dx=np.gradient(gaussian_filter(elev,1),meter,meter)
    slope=np.degrees(np.arctan(np.hypot(dx,dy)))
    h,w=slope.shape[0]//BLOCK,slope.shape[1]//BLOCK
    pool=slope[:h*BLOCK,:w*BLOCK].reshape(h,BLOCK,w,BLOCK)
    return pool.mean((1,3)),pool.max((1,3)),meter*BLOCK

def crossing(slope,cap,heading,cell):
    valid=slope<=cap
    h,w=valid.shape
    idx=np.arange(h*w,dtype=np.int32).reshape(h,w)
    if heading=='WE':
        start=np.array([(i,0) for i in range(int(h*.12),int(h*.88)) if valid[i,0]],dtype=np.int32).reshape(-1,2)
        end=np.array([(i,w-1) for i in range(int(h*.12),int(h*.88)) if valid[i,w-1]],dtype=np.int32).reshape(-1,2)
    else:
        start=np.array([(0,j) for j in range(int(w*.12),int(w*.88)) if valid[0,j]],dtype=np.int32).reshape(-1,2)
        end=np.array([(h-1,j) for j in range(int(w*.12),int(w*.88)) if valid[h-1,j]],dtype=np.int32).reshape(-1,2)
    if len(start)==0 or len(end)==0:return None
    costweight=1+(slope/8)**2
    sources=[];targets=[];values=[]
    for di,dj in [(0,1),(1,0),(1,1),(1,-1),(-1,0),(0,-1),(-1,-1),(-1,1)]:
        r0,r1=max(0,-di),min(h,h-di)
        c0,c1=max(0,-dj),min(w,w-dj)
        ok=valid[r0:r1,c0:c1]&valid[r0+di:r1+di,c0+dj:c1+dj]
        if di and dj:ok&=valid[r0+di:r1+di,c0:c1]&valid[r0:r1,c0+dj:c1+dj]
        sources.append(idx[r0:r1,c0:c1][ok])
        targets.append(idx[r0+di:r1+di,c0+dj:c1+dj][ok])
        values.append((costweight[r0:r1,c0:c1][ok]+costweight[r0+di:r1+di,c0+dj:c1+dj][ok])*.5*cell*math.hypot(di,dj))
    supernode=h*w
    sources.append(np.full(len(start),supernode))
    targets.append(idx[start[:,0],start[:,1]])
    values.append(np.full(len(start),1e-8))
    graph=csr_matrix((np.concatenate(values),(np.concatenate(sources),np.concatenate(targets))),shape=(supernode+1,supernode+1))
    distance,parent=dijkstra(graph,indices=supernode,return_predecessors=True,directed=True)
    ends=idx[end[:,0],end[:,1]]
    node=int(ends[np.argmin(distance[ends])])
    if not np.isfinite(distance[node]):return None
    path=[]
    while node>=0 and node!=supernode:
        path.append(divmod(node,w))
        node=int(parent[node])
    path=path[::-1]
    return round(sum(math.hypot(path[k][0]-path[k-1][0],path[k][1]-path[k-1][1])*cell for k in range(1,len(path)))/1000,2)

def main():
    mean,maximum,cell=load_slope()
    print('坡度聚合,坡度上限度,测试方向,可贯通,达限网格占比,路径长度公里,测试口径')
    for method,field in [('mean',mean),('max',maximum)]:
        for limit in (5,10,15,20):
            fraction=round(float(np.mean(field<=limit)),4)
            for direction in ('WE','NS'):
                km=crossing(field,limit,direction,cell)
                value='' if km is None else str(km)
                print(f'{method},{limit},{direction},{"NO" if km is None else "YES"},{fraction},{value},现代DEM矩形边界测试非古代道路')

if __name__=='__main__':
    main()

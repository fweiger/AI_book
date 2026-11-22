#!/usr/bin/env python3
"""Modern DEM minimax crossing threshold brackets. Not a 260 BCE troop model.
Requires numpy, scipy, Pillow and public Mapzen Terrain Tile AWS access.
4-neighbor critical slope: upper bound for no-corner-cutting 8-neighbor movement.
8-neighbor with corner cutting permitted: lower bound; it is optimistic.
Never treat either as real ancient road gradient or military vehicle limit.
"""
import io,math,urllib.request,csv,sys
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter,label
Z=10; WEST,SOUTH,EAST,NORTH=112.60,35.62,113.30,35.95

def coordinates(lat,lon):
    n=2**Z
    return ((lon+180)/360*n,(1-math.asinh(math.tan(math.radians(lat)))/math.pi)*n/2)

def terrain_slope():
    xl,yt=coordinates(NORTH,WEST);xr,yb=coordinates(SOUTH,EAST)
    x0,x1=math.floor(xl),math.floor(xr)
    y0,y1=math.floor(yt),math.floor(yb)
    tiles={}
    for y in range(y0,y1+1):
        for x in range(x0,x1+1):
            url=f'https://s3.amazonaws.com/elevation-tiles-prod/geotiff/{Z}/{x}/{y}.tif'
            with urllib.request.urlopen(url,timeout=25) as f:
                tiles[x,y]=np.asarray(Image.open(io.BytesIO(f.read())),dtype=np.float64)
    tiled=np.vstack([np.hstack([tiles[x,y] for x in range(x0,x1+1)]) for y in range(y0,y1+1)])
    dem=tiled[round((yt-y0)*512):round((yb-y0)*512),round((xl-x0)*512):round((xr-x0)*512)]
    if (dem<-1000).any():
        raise ValueError('DEM contains invalid/void values')
    pixel=76.43702828517416*math.cos(math.radians((SOUTH+NORTH)/2))
    dy,dx=np.gradient(gaussian_filter(dem,1),pixel,pixel)
    return np.degrees(np.arctan(np.hypot(dx,dy)))

FOUR=np.array([[0,1,0],[1,1,1],[0,1,0]],dtype=np.uint8)
EIGHT=np.ones((3,3),dtype=np.uint8)

def connected(arr,threshold,direction,diagonal):
    passed=arr<=threshold
    lab,_=label(passed,EIGHT if diagonal else FOUR)
    h,w=lab.shape
    if direction=='WE':
        first=lab[int(h*.12):int(h*.88),0]
        last=lab[int(h*.12):int(h*.88),-1]
    else:
        first=lab[0,int(w*.12):int(w*.88)]
        last=lab[-1,int(w*.12):int(w*.88)]
    a=np.unique(first[first>0])
    b=np.unique(last[last>0])
    return len(np.intersect1d(a,b,assume_unique=True))>0

def critical(arr,axis,diag):
    low,high=0.,50.
    for _ in range(11):
        mid=(low+high)/2
        if connected(arr,mid,axis,diag):
            high=mid
        else:
            low=mid
    return round(high,2)

def main():
    s=terrain_slope()
    writer=csv.writer(sys.stdout)
    writer.writerow(['block_pixels','estimated_cell_m','aggregation','axis','threshold_8neighbor_corner_cutting_permitted_lower_deg','threshold_4neighbor_upper_deg','note'])
    for block in (2,4,8,16):
        h,w=s.shape[0]//block,s.shape[1]//block
        bb=s[:h*block,:w*block].reshape(h,block,w,block)
        for agg,raster in [('mean',bb.mean((1,3))),('max',bb.max((1,3)))]:
            for axis in ('WE','NS'):
                writer.writerow([block,round(62.01*block),agg,axis,
                    critical(raster,axis,True),critical(raster,axis,False),
                    '现代DEM敏感性_严格不切角8邻域阈值位于上下界之间'])

if __name__=='__main__':
    main()

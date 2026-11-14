#!/usr/bin/env python3
"""Modern terrain screening only; NOT BC260 battlefield troop model.
Downloads 4 Mapzen Terrain Tiles TIFFs in memory; does not write files.
pip dependencies: numpy Pillow scipy; requires read-only internet to public AWS S3.
"""
import io, json, math, urllib.request
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter

ZOOM=10
XS=(832,833)
YS=(402,403)
BBOX=(112.71,35.63,113.14,35.99) # W,S,E,N, not a historic site boundary
BASE='https://s3.amazonaws.com/elevation-tiles-prod/geotiff'

def pixel(lat,lon):
 n=2**ZOOM
 x=(lon+180)/360*n
 y=(1-math.asinh(math.tan(math.radians(lat)))/math.pi)*n/2
 return round((x-XS[0])*512),round((y-YS[0])*512)

def main():
 tiles={}
 for y in YS:
  for x in XS:
   url=f'{BASE}/{ZOOM}/{x}/{y}.tif'
   with urllib.request.urlopen(url,timeout=20) as f: raw=f.read()
   tiles[x,y]=np.asarray(Image.open(io.BytesIO(raw)),dtype=np.float64)
 img=np.vstack([np.hstack([tiles[x,y] for x in XS]) for y in YS])
 w,s,e,n=BBOX; x0,y0=pixel(n,w);x1,y1=pixel(s,e)
 dem=img[y0:y1,x0:x1]
 if dem.shape != (647,626) or np.min(dem)<-1000:
  raise ValueError('Tile dimensions or void masks changed; inspect before analysis')
 ground_m=76.43702828517416*math.cos(math.radians((s+n)/2))
 smooth=gaussian_filter(dem,sigma=1.0)
 dy,dx=np.gradient(smooth,ground_m,ground_m)
 slope=np.degrees(np.arctan(np.hypot(dx,dy)))
 result={'data':'Mapzen Terrain Tiles GeoTIFF z10, modern DEM','bbox':BBOX,
 'tiles':[f'{ZOOM}/{x}/{y}' for y in YS for x in XS],
 'width_height':[dem.shape[1],dem.shape[0]],'pixel_ground_m':round(ground_m,1),
 'elevation_min_m':int(np.min(dem)),'elevation_median_m':int(np.median(dem)),
 'elevation_max_m':int(np.max(dem)),
 'elevation_p10_p90_m':np.percentile(dem,[10,90]).round().astype(int).tolist(),
 'slope_median_deg':round(float(np.median(slope)),1),
 'slope_p90_deg':round(float(np.percentile(slope,90)),1),
 'share_lt5_deg':round(float(np.mean(slope<5)),3),
 'share_lt10_deg':round(float(np.mean(slope<10)),3),
 'share_gt20_deg':round(float(np.mean(slope>20)),3),
 'meaning':'Terrain slope is NOT ancient military passability or 125 km garrison estimate.'}
 print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__=='__main__': main()

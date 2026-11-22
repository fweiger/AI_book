#!/usr/bin/env python3
"""Indicative pre-georeferencing QA only, not control-point registration.
Li & Hou (2023) user-supplied Fig. 1B crop is 717x557px.
These are manually estimated label centers (not graticule intersections).
No source figure/Copyright PDF is redistributed in AI_book.
"""
import json, math
IMAGE_PX=[717,557]
MID_LAT=35.75
LON_LABELS=[(112.75,177),(113.0,367),(113.25,542)]
LAT_LABELS=[(35+50/60,215),(35+40/60,365)]
BAR_ENDS_PX=[437,531]  # caption says 10km; approximate endpoints
lon_km=111.32*math.cos(math.radians(MID_LAT))*0.25
lat_km=111.132/6
barscale=(BAR_ENDS_PX[1]-BAR_ENDS_PX[0])/10
east_scales=[(LON_LABELS[i+1][1]-LON_LABELS[i][1])/lon_km for i in range(2)]
ns_scale=(LAT_LABELS[1][1]-LAT_LABELS[0][1])/lat_km
value={
'image_crop_pixels':IMAGE_PX,'source':'user-provided Li/Hou 2023 p62 Fig1B - no image redistributed',
'pixel_inputs_rough':{'longitude_label_center_px':LON_LABELS,'latitude_label_center_px':LAT_LABELS,'scale_bar_0_10km_px':BAR_ENDS_PX},
'longitude_gridlabel_pixels_per_km':[round(z,2) for z in east_scales],
'latitude_gridlabel_pixels_per_km':round(ns_scale,2),
'scale_bar_pixels_per_km':round(barscale,2),
'apparent_scale_differences_percent':[round(100*(barscale/q-1),1) for q in [*east_scales,ns_scale]],
'interpretation':'VISUAL_PREFLIGHT_ONLY_NO_PRECISE_GRID_INTERSECTIONS',
'warning':'Approximate label centers and scale bar are not precise georeferencing control points; differences may come from label placement, schematic drawing and rescaling. This does NOT prove 1998 original map or Li/Hou field work was wrong. Do not digitize the Qin 125km line as WGS84 geometry from this figure.'}
print(json.dumps(value,ensure_ascii=False,indent=2))

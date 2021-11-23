# -*- coding: utf-8 -*-
# Written by Vamei, http://www.cnblogs.com/vamei/
# Feel free to use or modify this script.
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
 
#============================================
# read data
names = []
pops  = []
lats  = []
lons  = []
countries = []
for line in open("major_city.txt","r"):
    info = line.split()
    names.append(info[0])
    pops.append(float(info[1]))
    lat  = float(info[2][:-1])
    if info[2][-1] == 'S': lat = -lat
    lats.append(lat)
    lon  = float(info[3][:-1])
    if info[3][-1] == 'W': lon = -lon + 360.0
    lons.append(lon)
    country = info[4]
    countries.append(country)
 
#============================================
# set up map projection with
# use low resolution coastlines.
map = Basemap(projection='ortho',lat_0=35,lon_0=120,resolution='l')
# draw coastlines, country boundaries, fill continents.
map.drawcoastlines(linewidth=0.25)
map.drawcountries(linewidth=0.25)
# draw the edge of the map projection region (the projection limb)
map.drawmapboundary(fill_color='#689CD2')
# draw lat/lon grid lines every 30 degrees.
map.drawmeridians(np.arange(0,360,30))
map.drawparallels(np.arange(-90,90,30))
# Fill continent wit a different color
map.fillcontinents(color='#BF9E30',lake_color='#689CD2',zorder=0)
# compute native map projection coordinates of lat/lon grid.
x, y = map(lons, lats)
max_pop = max(pops)
# Plot each city in a loop.
# Set some parameters
size_factor = 80.0
y_offset    = 15.0
rotation    = 30
for i,j,k,name in zip(x,y,pops,names):
    size = size_factor*k/max_pop
    cs = map.scatter(i,j,s=size,marker='o',color='#FF5600')
    plt.text(i,j+y_offset,name,rotation=rotation,fontsize=10)
 
plt.title('Major Cities in Asia & Population')
plt.show()

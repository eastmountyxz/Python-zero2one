# -*- coding: utf-8 -*-
# By:Eastmount CSDN
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
 
width = 28000000; lon_0 = -105; lat_0 = 40
m = Basemap(width=width,height=width,projection='aeqd',
            lat_0=lat_0,lon_0=lon_0)
 
# 填充背景
m.drawmapboundary(fill_color='aqua')

# 绘制海岸线并填充大陆
m.drawcoastlines(linewidth=0.5)
m.fillcontinents(color='coral',lake_color='aqua')

# 20度经纬度，范围-80到81 -180到180
m.drawparallels(np.arange(-80,81,20))
m.drawmeridians(np.arange(-180,180,20))

# 在中心绘制一个黑点
xpt, ypt = m(lon_0, lat_0)
m.plot([xpt],[ypt],'ko')

# 绘制标题
plt.title('Azimuthal Equidistant Projection')
plt.show()

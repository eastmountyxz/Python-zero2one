# -*- coding: utf-8 -*-
# By:Eastmount CSDN
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
 
# 设置basemap-Lambert Conformal 
m = Basemap(width=12000000,height=9000000,projection='lcc',
            resolution='c',lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
 
# 绘制海岸线
m.drawcoastlines()
# 在地图周围绘制边界并填充背景aqua（这个背景最终成为海洋的颜色）
# 将大洲绘制在最上面
m.drawmapboundary(fill_color='aqua')
 
# 填充大陆coral颜色,并设置湖泊颜色为blue
m.fillcontinents(color='coral',lake_color='blue')
plt.show()

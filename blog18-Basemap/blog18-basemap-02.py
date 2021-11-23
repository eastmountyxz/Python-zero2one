# -*- coding: utf-8 -*-
# By:Eastmount CSDN
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
 
# 设置basemap Lambert-Conformal 
# 设置分辨率参数resolution=None 跳过处理边界数据集
m = Basemap(width=12000000,height=9000000,projection='lcc',
            resolution=None,lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
 
# 为地图背景绘制海陆罩
# lakes=True 意味着内陆湖和海洋颜色一致
m.drawlsmask(land_color='coral',ocean_color='aqua',lakes=True)
plt.show()

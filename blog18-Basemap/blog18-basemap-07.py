# -*- coding: utf-8 -*-
# By:Eastmount CSDN
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
 
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80,
            llcrnrlon=-180, urcrnrlon=180)
m.drawcoastlines()
plt.show()

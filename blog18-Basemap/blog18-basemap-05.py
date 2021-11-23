# -*- coding: utf-8 -*-
# By:Eastmount CSDN
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
 
m = Basemap(width=12000000,height=9000000,projection='lcc',
            resolution=None,lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
m.etopo()
plt.show()

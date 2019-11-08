import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import filters 
#Convert google maps to GPX via http://www.gpsies.com/convert.do
import gpxpy
with open('AH-route.gpx', 'r') as gpx_file:
    gpx = gpxpy.parse(gpx_file)
height_data = np.zeros((len(gpx.get_points_data())))
distance_data = np.zeros((len(gpx.get_points_data())))
for i,p in enumerate(gpx.get_points_data()):
    height_data[i] = p.point.elevation
    distance_data[i] = p.distance_from_start
#pos_data = distance_data[:]
#pos_data[1:] = pos_data[1:] - pos_data[:-1]
#pos_data[0] = 0
grad = np.gradient(height_data,distance_data)
plt.figure()
plt.plot(distance_data,height_data)
plt.figure()
plt.plot(filters.gaussian_filter(grad,5))
plt.show()

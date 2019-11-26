import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import filters 
#Convert google maps to GPX via https://www.gpsvisualizer.com/elevation
import gpxpy
with open('AH-route.gpx', 'r',encoding='utf-8') as gpx_file:
    gpx_string = str(gpx_file.read())
    gpx = gpxpy.parse(gpx_string)
height_data = np.zeros((len(gpx.get_points_data())), dtype=np.float)
distance_data = np.zeros((len(gpx.get_points_data())), dtype=np.float)
for i,p in enumerate(gpx.get_points_data()):
    height_data[i] = float(p.point.elevation)
    distance_data[i] = float(p.distance_from_start)
#pos_data = distance_data[:]
#pos_data[1:] = pos_data[1:] - pos_data[:-1]
#pos_data[0] = 0
delta = height_data[1:] - height_data[:-1] 
print("Uphill",np.sum(delta[delta>0]))
print("Downhill",np.sum(delta[delta<0]))
grad = np.gradient(height_data,distance_data)
plt.figure()
plt.plot(distance_data,height_data)
plt.title("Elevation of the AH's example route")
plt.xlabel("Distance (m)")
plt.ylabel("Elevation (m)")
plt.savefig("elevation.png")
plt.figure()
plt.title("Gradient of the AH's example route")
plt.plot(distance_data,grad*100,label="Raw")
plt.plot(distance_data,filters.gaussian_filter(grad,5)*100,label="Filtered")
plt.xlabel("Distance (m)")
plt.ylabel("Gradient (%)")
plt.legend()
plt.savefig("grad.png")
plt.show()

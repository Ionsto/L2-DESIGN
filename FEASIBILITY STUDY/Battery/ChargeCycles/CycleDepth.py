import numpy as np
import matplotlib.pyplot as plt
DoDData = np.array([100,80,60,40,20,10])
Lion = np.array([300,400,600,1000,2000,6000])
LiPo = np.array([600,900,1500,3000,9000,15000])
plt.figure()
plt.plot(DoDData,Lion,label="Lion")
plt.plot(DoDData,LiPo,label="LiPo")
plt.title("Depth of discharge vs lifespan (charge cycles)")
plt.xlabel("Depth of discharge (%)")
plt.ylabel("Lifespan (Charge cycle count)")
plt.legend()
plt.savefig("DoD.png")
plt.show()

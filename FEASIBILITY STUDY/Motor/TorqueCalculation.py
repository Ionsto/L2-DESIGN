import numpy as np
import math
#KG
Mass = 140
#N/kg
Gravity = 9.81
#From a paper
RollingResistance = 0.01
#In percentage
MaxGradient = 10.0/6.28
#From route analysis
GradientAngle = np.arctan(MaxGradient / 100.0)
#Reasonable value
WheelRadius = (70e-3)/2
#Calcuations
MinTorque = RollingResistance * Gravity * Mass * WheelRadius
MaxTorque = MinTorque + (Mass * Gravity * math.sin(MaxGradient) * WheelRadius)
print("Min torque",MinTorque)
print("Max torque",MaxTorque)

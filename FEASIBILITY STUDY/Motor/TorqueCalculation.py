import numpy as np
#KG
Mass = 120
#N/kg
Gravity = 9.8
#From a paper
RollingResistance = 0.01
#In percentage
MaxGradient = 10.0
#From route analysis
GradientAngle = np.arctan(MaxGradient / 100.0)
#Reasonable value
WheelRadius = 100e-3/2
#Calcuations
MinTorque = RollingResistance * Gravity * Mass * WheelRadius
MaxTorque = MinTorque + (Mass * Gravity * np.sin(WheelRadius))
print("Min torque",MinTorque)
print("Max torque",MaxTorque)

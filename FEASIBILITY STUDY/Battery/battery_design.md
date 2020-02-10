
# Battery overview
## Battery picked
Two 6S batteries are more affordable to find, and allow for the batteries to be placed in disparate locations
There is also the thermal dissapation benifits for having two seperate batteries.
We picked this battery as it has roughly half the voltage we needed, and was small enought that it could fit in the encolsure.

https://www.banggood.com/ZOP-POWER-22_2V-8000mAh-60C-6S-Lipo-Battery-With-XT60-Plug-For-RC-Model-p-1328629.html

Stats:

- Watt hour capacity: 177.6Wh each
- Cell count: 6S
- Voltage: 22.2V
- Size 90x46x158mm

2 batteries in parallel, 355.2Wh

The batteries will be in series, so the capacity will be 178Wh together, but the operating voltage will be will be 44.4V.



## Battery charging
https://electronics.stackexchange.com/questions/115795/charging-batteries-in-parallel-when-they-are-connected-in-series-in-the-circuit
Since we have two seeprate batteries that are being used in parralel, we will either need a charger that can handle a 12S system or we will have to do some TDMA parralel charging.
https://www.flitetest.com/articles/Parallel_Charging_Your_LiPo_Batteries

## Battery charging mode 
When in operation, the  batteries are in series to get the correct operating voltage, but for charging they need to be in parralel for the charger to work.

## Battery microcontroller
Low power, separate coin battery supply, min lifespan 5 years

Power supply CR2032 - 225 mAh, 3V nominal

LED indicator:

- Off - hibernating
- On - functioning
- Blinking - dead

Battery status monitor:

- 2 ADC, voltage
- 1 Ammeter, current

Battery capacity line, report both battery voltages to arduino
Battery draw line, report current usage


## Battery states
Battery system state

- Hibernation (battery isolated,LED indicator)
- Idle state (battery live, V+S,V-S, V+P, V-P all off)
- Charge state (V+P, V-P on, V+S,V-S off)
- Drive state (V+P, V-P off, V+S,V-S on)
- Battery disabled state (All off, LED indicator) - wake Arduino state reason?

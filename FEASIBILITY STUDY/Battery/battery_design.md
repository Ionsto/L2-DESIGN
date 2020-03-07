
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
- Size: 90x46x158mm
- Mass: 1.24Kg

2 batteries in parallel, 355.2Wh

The batteries will be in series, so the capacity will be 178Wh together, but the operating voltage will be will be 44.4V.



## Battery charging
https://electronics.stackexchange.com/questions/115795/charging-batteries-in-parallel-when-they-are-connected-in-series-in-the-circuit
Since we have two seeprate batteries that are being used in parralel, we will either need a charger that can handle a 12S system or we will have to do some TDMA parralel charging.
https://www.flitetest.com/articles/Parallel_Charging_Your_LiPo_Batteries
Charger: CHANGED
https://www.banggood.com/ToolkitRC-URUAV-M800-300W-15A-DC-Smart-1-8S-Lipo-Battery-Balance-Charger-Discharger-With-Voltage-Servo-Checker-Receiver-Signal-Tester-Quick-Charger-Function-p-1588415.html?rmmds=search&ID=6280172&cur_warehouse=CN
This charger has a higher current rating - to drop charge times (did some more maths).
OLD charger: https://uk.banggood.com/SKYRC-e680-80W-8A-ACDC-Balance-Charger-Discharger-for-1-6S-Lipo-Battery-p-1526977.html?gmcCountry=GB&currency=GBP&createTmp=1&utm_source=googleshopping&utm_medium=cpc_bgcs&utm_content=lijing&utm_campaign=ssc-gbg-all-0218&ad_id=332556156911&gclid=Cj0KCQiAkKnyBRDwARIsALtxe7jVKPeWvrknm1ky1uDgQWFhhLgEnDdWBOXv_zR9uhSxIB9SeKE4DUEaAoWnEALw_wcB&ID=47184&cur_warehouse=CN

## Battery charging mode 
When in operation, the  batteries are in series to get the correct operating voltage, but for charging they need to be in parralel for the charger to work.

## Battery microcontroller
Low power, separate coin battery supply, min lifespan 5 years
https://www.digikey.co.uk/product-detail/en/stmicroelectronics/STM8L152C6T6/497-10512-ND/2269726

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

## Battery switch
Used multiple N channel power MOSFETs as a high side switch

Use gate drivers: https://www.analog.com/en/about-adi/news-room/press-releases/2017/fast-60v-high-side-n-channel-mosfet-driver-provides-100-duty-cycle-capability.html
LTC7004 

Use power mosfets
FDC6324L

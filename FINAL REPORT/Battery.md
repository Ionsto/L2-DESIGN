# Battery section outline
First section is headings and sub topics
## Headings
- Introduction
- Capacity
- Charging
- Control system
- Disposal  
# Direction 
### Introduction
- Actual configuration 
- Need for a battery
- Battery types
- Estimated capacity
- Estimated size and volume
### Capacity
- Range
- Gradient
- Estimated efficiency 
- Size
- Weight
- Off the shelf solutions
### Charging
- Dangers
- Mitigations
- Voltages
- Currents
- Charging times
- Use of pre-built chargers
- Need for a parallel - series mux
### Charging MUX
- Whats the purporse
- What are the key goals (safty, supplying power, allowing safe charging)
- Overview of mux circuitry
- Switching technolog
### Control system
- Seperate power supply
- Monitor charge cycles and battery health
- Wake up and monitor voltages
- Control supply MUX
- 
### Disposal
- WEEE
- Take back scheme
- Maintanance and takeback

# Nomenclture:
- S rating for batteries - how many cells in series
- Gravometric density, Wh per kg
- Volumetric density, Wh per litre 



# Direction
## Introduction 
- Battery pack is made of two smaller 6S batteries - battery voltage has increased since the feasiblity report
- Batteries are integral to eletric vehicles
- We chose lithum polymer, much better current suuply and lifespan compared to other chemistrys.
- Estimated minimum capcaity ~180Wh from feasibilty report
- We are going to be useing off the shelf batteries: XXXX XXXX
- Two battereies required to reach line voltage ~50V
- Each battery is aproximately the size xxx,xxx,xxx mm
## Capacity
- Each battery has a caoacity of ~180Wh
## Charging
- Lithium polymer is very dangerous, lots of mitigations requried to make them "safe" see faliure mode analysis
- Instead of designing and building a charging circuit - use an off the shelf solution
- We are going to use an afordable charger, model XXX which can charge one battery in X hours.
- The charger can only charge at a rail voltage of 24V - so our two batteries need to be chaged parralel
- We will need a system to take them from series to parrralel
## Control system
- To control the battery system we need an independent control system
- The control system will be based around a low power microcontroler
- There are 4 states as shown in the control flow diagram
- The control micro will monitor the battery pack and will control the series/parralel state.
- The mux will be eletrically controled and isolated from the battery micro
- The control circuit will have a serial connection to the drive micro - along with a heartbeat connection
## Battery mux
- Mux circuitry
- How the mux will make the circuit safer
- The charger can't charge in series - voltage is too high
- The balancing leads are required to keep the cells from degrading from overdischarge
- Switching technology chosen is solid state power switches (high side switching fet based systems).
- Fets > Relays and mechanical switches as they are resistant to vibration and wont contact weld shorted 


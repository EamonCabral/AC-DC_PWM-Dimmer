# AC-DC_PWM-Dimmer
Home project to develop a PWM signal to control the frequency output via Firing Angle control. 

# ------------------------------------------------------------- #
# Warning: 
Always take the necessary precautions when working with high-medium AC/DC Voltage!
I do not endorse the manipulation of High voltage without the guidance of a certified technician. 
Proper knowledge, training, and working understandings of Electrodynamics are paramount to safely performing this project

# ------------------------------------------------------------- #
The purpose of this project was to use a Raspberry Pi to control the phase of the AC frequency in order to dampen or increase light potency.
This method is commonly known as Firing Angle Method and instead of modulating the voltage, you modulate the degrees at which the cycle is activated.

You can read more about this here: https://www.elprocus.com/power-control-using-scr/

In a nutshell:
This is fancy way of building a dimmer for my Wind Turbine fan controlled by a Raspberry pi.

The code comes with instructions and explanations at each stage and each line

To use the same Arduino controller I used for Firing Angle control, check out: https://www.amazon.com/gp/product/B06Y1DT1WP/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1

If you want to be a bit more badass, build your own controller (I have not tested this option)

The starting frequency of your code should ALWAYS match your grid's frequency. i.e. (60 Hz for North America, 50 Hz EU, etc)
This is explained in the code so be sure to read through when using it.

You can instruct your electrician to use a Multimeter to verify your grid's frequency

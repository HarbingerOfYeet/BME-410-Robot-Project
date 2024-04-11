from machine import ADC
import math
from time import sleep



Ro = 47000 #47k Resistor
Vin = 3.3 #Reference voltage on pico
# B = -4050 #B-constant
To = 298.15 #Reference Temperature

# Steinhart Constants
A = 0.001129148
B = 0.000234125
C = 0.0000000876741

#Get Voltage
def get_voltage(adc):
    Vout = (Vin / 65535) * adc
    return Vout

#Voltage Divider
def calc_resistance(Vout):
    Rt = (Vout * Ro) / (Vin - Vout)
    return Rt

def get_temp(adcpin):
    thermistor = ADC(adcpin)
    adc = thermistor.read_u16()
    Vout = get_voltage(adc)
    
    # Calculate Resistance
    Rt = calc_resistance(Vout)
 
    # Steinhart - Hart Equation
    tempK = 1 / (A + (B * math.log(Rt)) + C * math.pow(math.log(Rt), 3))

    # Convert from Kelvin to Celsius
    tempC = tempK - 273.15

    return tempC


if __name__ == "__main__":
    while True:
        left = get_temp(26)
        right = get_temp(27)
        print(f"Left: {left}, Right: {right}")
        sleep(1)

#B-Constant Equation
# def calc_temperature(Rt):
#     temp = (B / math.log(Rt/Ro)) + To
#     temp -= 273.15 #Convert to celsius
#     return temp

#Main Code
# while True:    
#     # Get Voltage value from ADC   
#     left_adc = left_therm.read_u16()
#     right_adc = right_therm.read_u16()
#     left_Vout = get_voltage(left_adc)
#     right_Vout = get_voltage(right_adc)
    
#     # Calculate Resistance
#     left_Rt = calc_resistance(left_Vout)
#     right_Rt = calc_resistance(right_Vout)

    
#     # Steinhart - Hart Equation
#     left_TempK = 1 / (A + (B * math.log(left_Rt)) + C * math.pow(math.log(left_Rt), 3))
#     right_TempK = 1 / (A + (B * math.log(right_Rt)) + C * math.pow(math.log(right_Rt), 3))


#     # Convert from Kelvin to Celsius
#     left_TempC = left_TempK - 273.15
#     right_TempC = right_TempK - 273.15

#     # print(f"Left: {left_TempC}")
#     # print(f"Right: {right_TempC}")
#     print(f"Temp diff (left minus right): {round(left_TempC - right_TempC, 3)}")
#     sleep(1)
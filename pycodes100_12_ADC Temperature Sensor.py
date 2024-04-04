#https://newdigitals.org/2024/02/24/100-basic-python-codes/#adc-temperature-sensor
SYSVOLT = 5
ADC_RESOLUTION = 4095
MAX_VOLT = 2.442
MIN_VOLT = 0
 
MIN_TEMP = -50
MAX_TEMP = 50
def adc_raw_value(v):
    if(v >= MIN_VOLT and v <= MAX_VOLT):
        ADC = (v*(ADC_RESOLUTION/SYSVOLT))
        return round(ADC)
    else:
        return None
     
def adc_to_c(x):
    if x == 0:
        return -50
    else:
        return ((adc_to_c(x-1)) + 0.05)
def sensor_temp(v):
    print(f"SENSOR READ: {v} Volt")
    ADC = adc_raw_value(v)
    if ADC is None:
        print("Voltage is not within the sensor range")
    else:
        print("**********************\nAnalog to Digital Convertion\n**********************")
        print(f"Analog: {v}\nDigital: {ADC}")
        print("**********************")
        print(f"Temperature is: {round(adc_to_c(ADC))}")
sensor_temp(MIN_VOLT)
SENSOR READ: 0 Volt
**********************
Analog to Digital Convertion
**********************
Analog: 0
Digital: 0
**********************
Temperature is: -50
sensor_temp(MAX_VOLT) 
SENSOR READ: 2.442 Volt
**********************
Analog to Digital Convertion
**********************
Analog: 2.442
Digital: 2000
**********************
Temperature is: 50
sensor_temp(1.221) 
SENSOR READ: 1.221 Volt
**********************
Analog to Digital Convertion
**********************
Analog: 1.221
Digital: 1000
**********************
Temperature is: 0
sensor_temp(1.5)
SENSOR READ: 1.5 Volt
**********************
Analog to Digital Convertion
**********************
Analog: 1.5
Digital: 1228
**********************
Temperature is: 11

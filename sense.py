"""
Arduino component of my Greenhouse dashboard

Sidney Thiel
PCB-11
"""
# import time
# import csv
from CustomPymata4 import CustomPymata4

# Note: LDR_PIN and DHT_PIN is in uppercase due to the suggestion of pylint.
#       As that is the python convention for global variables.
LDR_PIN = 2
DHT_PIN = 12
board = CustomPymata4(com_port='COM3', baud_rate=57600)
board.set_pin_mode_dht(DHT_PIN, sensor_type=11)
board.set_pin_mode_analog_input(LDR_PIN)

def sensor_data():
    """Get the raw data from the the DHT11 sensor"""
    s_data = board.dht_read(DHT_PIN)
    return list(s_data)

def get_temp(s_data):
    """Function to return the temparature."""
    return s_data[0]

def get_hum(s_data):
    """Function to return the relative humitidy"""
    return s_data[1]

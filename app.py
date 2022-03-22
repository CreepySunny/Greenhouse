"""
Greenhouse authantic task.
Dashboard using Flask and Pymata to display enviroment data of a greenhouse. 

Sidney Thiel
PCB-11
"""
import csv
from random import randint
from datetime import datetime
from flask import Flask, render_template
from CustomPymata4 import CustomPymata4


data = {}
# Note: LDR_PIN and DHT_PIN is in uppercase due to the suggestion of pylint. As that is the python convention for global variables.
LDR_PIN = 2
DHT_PIN = 12
board = CustomPymata4(com_port="COM3", baud_rate=59000)
board.set_pin_mode_dht(DHT_PIN, sensor_type=11)
board.set_pin_mode_analog_input(LDR_PIN)
app = Flask(__name__)

def sensor_data():
    """Get the raw data from the the DHT11 sensor"""
    s_data = board.dht_read(DHT_PIN)
    return s_data

def get_temp(s_data):
    """Function to return the temparature."""
    return s_data[0]

def get_hum(s_data):
    """Function to return the relative humitidy"""
    return s_data[1]

def get_date_time():
    """Gets the current time and date."""
    return datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

def gen_rand_data():
    """Generates random data for debug purposes"""
    data["temp"] = randint(15, 40)
    data["humi"] = randint(0, 100)
    data["light"] = randint(0, 1000)

@app.route("/")
def index():
    """The homepage funciton"""
    gen_rand_data()
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)

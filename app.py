"""
Greenhouse authantic task.
Dashboard using Flask and Pymata to display enviroment data of a greenhouse.

Sidney Thiel
PCB-11
"""
# import csv
from datetime import datetime
from random import randint
from flask import Flask, render_template
import sense

data = {}
app = Flask(__name__)

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
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)

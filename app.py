from random import randint
import datetime
from flask import Flask, render_template


data = {}
app = Flask(__name__)

def gen_rand_data():
    """Generates random data for debug purposes"""
    data["temp"] = randint(15, 40)
    data["humi"] = randint(0, 100)
    data["light"] = randint(0, 1000)
    data["dt"] = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

@app.route("/")
def index():
    """The homepage funciton"""
    gen_rand_data()
    return render_template('index.html.jinja', data=data)

if __name__ == "__main__":
    app.run(debug=True)

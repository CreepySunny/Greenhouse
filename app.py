from random import randint
from time import strptime
from flask import Flask, render_template
import datetime

data = {}
app = Flask(__name__)

@app.route("/")
def index():
    """The homepage funciton"""
    data["temp"] = randint(15, 40)
    data["humi"] = randint(0, 100)
    data["light"] = randint(0, 1000)
    data["dt"] = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    return render_template('index.html.jinja', data=data)

if __name__ == "__main__":
    app.run(debug=True)

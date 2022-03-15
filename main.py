from flask import Flask, render_template
from random import randint
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html.jinja', t_sens=randint(20, 36), h_sens=randint(40, 80))

if __name__ == "__main__":
    app.run(debug=True)

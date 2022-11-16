from utils import *

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",
                           get_flags = get_flags())

@app.route("/test")
def test():
    return render_template("test.html")


app.run(host='0.0.0.0', port=81, debug=True)
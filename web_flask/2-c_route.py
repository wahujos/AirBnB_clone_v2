#!/usr/bin/python3
""" C is fun!"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hell0_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    formatted_text = text.replace("_", " ")
    return f"C {formatted_text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

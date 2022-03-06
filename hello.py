from flask import Flask

app = Flask(__name__)

@app.route("/")
def japan():
    return "<p>Hello, Japan!</p>"

@app.route("/japan/<city>")
def tokyo(city):
    return f"<h1>Hello, {city}!</h1>"

# @app.route("/saitama")
# def saitama():
#     return "<p>Hello, America!</p>"

# @app.route("/nara")
# def nara():
#     return "<p>Hello, America!</p>"


@app.route("/world")
def world():
    return "<p>Hello, World!</p>"
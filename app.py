from flask import Flask
app = Flask(__name__)

@app.route("/poc")
def hello():
    return "Subdomain Takeover by pacman_x"

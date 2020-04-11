from flask import Flask, render_template, request
import sys

app = Flask(__name__, static_folder="")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/visualizer", methods=["POST", "GET"])
def visualizer():
    return render_template("visualizer.html")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Invalid arguments")
        print("Usage: 'python app.py host port'")
        print("Ex: python app.py 0.0.0.0 8080")
    else:
        app.run(host=sys.argv[1], port=sys.argv[2], debug=True)

from flask import Flask, render_template, request
import packages

app = Flask(__name__)
debug = True

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

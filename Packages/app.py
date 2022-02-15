from crypt import methods
from flask import Flask, render_template, request
import packages

app = Flask(__name__)
#app.config["DEBUG"] = True


@app.route("/", methods=["GET", "POST"])
def main():
    list1 = {"ala": 1, "kot": 1, "tata": 1}
    list2 = {"ala": 3, "kot": 3, "tata": 3}
    list3 = {"ala": 7, "kot": 7, "tata": 7}
    main_list = [list1, list2, list3]
    return render_template("index.html", context=main_list)


if __name__ == "__main__":
    app.run(debug=True)
from crypt import methods
from flask import Flask, render_template, request
import packages

app = Flask(__name__)
#app.config["DEBUG"] = True


@app.route("/", methods=["GET", "POST"])
def main():

    result_app = [1,2,3,4,5,6]
    # result_app = [final_list, number_of_sent_packages, number_of_kilograms_sent, number_of_empty_kilos,
    #               package_with_max_empty_weight, number_of_package_with_max_empty_weight]

    return render_template("index.html", context=result_app)


if __name__ == "__main__":
    app.run(debug=True)
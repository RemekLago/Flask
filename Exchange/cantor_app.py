from flask import Flask, request

cantor_app = Flask(__name__)


@cantor_app.route("/")
def index():

    print(request.query_string)

    color = "black"
    if "color" in request.args:
        color = request.args["color"]    

    return f'<h1 style="color: {color}" > Wellcome on cantor online </h1>' 
#    '< br / > <h2> Go to .../cantor/enter carrency/enter ammount </h2>'


@cantor_app.route("/cantor/<string:currency>/<int:amount>")
def cantor(currency, amount):
    message = f"<h1> You selected: {currency}<br /> and amount: {amount} </h1>"
    return message

if __name__ == "__main__":
    cantor_app.run()

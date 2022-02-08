from flask import Flask, request

exchange_app = Flask(__name__)


@exchange_app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        body = '''
            <form id="exchange-form" action="/exchange_process" method="POST">
                <label for="currency"> Currency </label> <br>      
                <input type="text" id="currency" name="currency" value="EUR"> <br>
                <br>
                <label for="amount"> Amount! </label> <br>
                <input type="text" id="amount" name="amount" value="100"> <br>
                <br>
                <input type="submit" value="Send">
            </form>
            '''
        return body
    else:
        currency = "EUR"
        if 'currency' in request.form:
            currency = request.form["currency"]

        amount = 1000
        if 'amount' in request.form:
            amount = request.form["amount"]

        body = f"You want to exchange {amount} of {currency}"

        return body

@exchange_app.route("/exchange_process", methods=["POST"])
def exchange_process():
    
    currency = "EUR"
    if 'currency' in request.form:
        currency = request.form["currency"]

    amount = 1000
    if 'amount' in request.form:
        amount = request.form["amount"]

    body = f"You want to exchange {amount} of {currency}"

    return body

@exchange_app.route("/about")
def about():
    color = "blue"
    text1 = f'''<h1 style="color: {color}"> This is app to calculate exchange process </h1>
                <h1> You can change amount and currency value </h1>'''
    return text1


if __name__ == "__main__":
    exchange_app.run()

from flask import Flask
from datetime import datetime

time_app = Flask(__name__)


@time_app.route("/")
def index():
    time_now = datetime.now().strftime("%H:%M:%S")
    return f"""<h1>Hello, current time for Warsaw is: {time_now} </h1> <br />
            <h2> Now you know what time is it :)</h2>"""


@time_app.route("/links")
def links():
    body = '''<a href="http://www.google.com" target = "_blank"> Google </a> <br />
        <a href = "http://www.bing.com" target = "_blank" > Default search engine to find Google</a>'''
    return body

if __name__ == "__main__":
    time_app.run()

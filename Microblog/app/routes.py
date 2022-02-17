from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Remek"}
    posts = [
        {
            "author": {"username": "John"},
            "body": "Beautiful day in Poland"
        },
        {
            "author": {"username": "Anna"},
            "body": "The film was marvellous"
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)

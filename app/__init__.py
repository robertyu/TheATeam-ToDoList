from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

#@app.route('/')
#def homepage():
#    return render_template("main.html")

#if __name__ == "__main__":
#    app.run()

from app import views, models

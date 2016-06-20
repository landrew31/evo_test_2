from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os, requests, json


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Adjective, Name


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sayHello', methods=['POST'])
def sayHello():
    name =  request.form['name'];
    print name
    return json.dumps({'status':'OK','name':name});


if __name__ == '__main__':
    app.run(threaded=True, debug=True)

# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os, requests, json
import random


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
    person = db.session.query(Name).filter_by(name=name).first()
    print person is None
    if person is None:
    	adj_count = Adjective.query.count()
    	new_adj = random.randint(0, adj_count)
    	while db.session.query(Adjective).filter_by(id=new_adj) is None:
    		new_adj = random.randint(0, adj_count)
    	new_person = Name(name, new_adj)
    	db.session.add(new_person)
    	db.session.commit()
    	hello = "Рад тебя видеть, ".decode('utf-8') + db.session.query(Adjective).filter_by(id=new_person.adj_id).first().adj + " " + new_person.name + "!"
    else:
    	hello = "Рад тебя снова видеть, ".decode('utf-8') + db.session.query(Adjective).filter_by(id=person.adj_id).first().adj + " " + person.name + "!"

    return json.dumps({'status':'OK','hello': hello});


if __name__ == '__main__':
    app.run(threaded=True, debug=True)

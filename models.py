from app import db
from sqlalchemy.dialects.postgresql import JSON


class Adjective(db.Model):
    __tablename__ = 'adjective'

    id = db.Column(db.Integer, primary_key=True)
    adj = db.Column(db.String(50))
    name = db.relationship('Name', backref='adjective', uselist=False)

    def  __init__(self, adj):
        self.adj = adj

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Name(db.Model):
    __tablename__ = 'name'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    adj_id = db.Column(db.Integer, db.ForeignKey('adjective.id'))

    def __init__(self,name,adj_id):
        self.name = name
        self.adj_id = adj_id

    def __repr__(self):
        return '<id {}>'.format(self.id)


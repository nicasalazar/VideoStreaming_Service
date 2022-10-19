from db import db


class Vid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vid = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
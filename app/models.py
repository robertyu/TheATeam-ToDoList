from app import db, models

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String(80))
    date = db.Column(db.String(15))

#    def __init__(self, activity, date):
#        self.activity = activity
#        self.date = date


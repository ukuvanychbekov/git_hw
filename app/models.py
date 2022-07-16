from . import db, bcrypt


class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    period = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Integer(), nullable=False)
    status = db.Column(db.String(50))
    unit = db.Column(db.String(50))
    subject = db.Column(db.String(50))


    def __repr__(self):
        return f'Transactions {self.status}'

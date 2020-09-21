from app import db
from datetime import datetime
from app.model.user import Users
from app.model.kelas import Kelass


class Absens(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.BigInteger, db.ForeignKey(Users.id))
    kelas_id = db.Column(db.BigInteger, db.ForeignKey(Kelass.id))
    users = db.relationship("Users", backref="user_id")
    kelass = db.relationship("Kelass", backref="kelas_id")

    def __repr__(self):
        return '<Absen {}>'.format(self.absen)

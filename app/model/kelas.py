from app import db
from datetime import datetime

class Kelass(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nama_kelas = db.Column(db.String(230), nullable=False)
    nama_pengajar = db.Column(db.String(230), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Kelas {}>'.format(self.kelas)

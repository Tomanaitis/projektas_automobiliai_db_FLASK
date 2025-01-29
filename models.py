from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Automobilis(db.Model):
    __tablename__ = "automobiliai"
    id = db.Column(db.Integer, primary_key=True)
    gamintojas = db.Column(db.String)
    modelis = db.Column(db.String)
    spalva = db.Column(db.String)
    kaina = db.Column(db.Float)


    def __repr__(self):
        return f"id: {self.id} {self.gamintojas} {self.modelis} {self.spalva} {self.kaina}"

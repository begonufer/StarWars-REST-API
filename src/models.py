from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    firstname = db.Column(db.String, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'{self.id}'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }
class Favorite(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=True)

    def __repr__(self):
        return f'{self.id}'

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "character_id": self.character_id
        }
class Planets(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    terrain = db.Column(db.String)
    climate = db.Column(db.String)
    population = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    rotation_period = db.Column(db.Integer)
    diameter = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.terrain}'

    def serialize(self):
        return {
            "id": self.id,
            "terrain": self.terrain,
            "climate": self.climate,
            "population": self.population,
            "orbital_period": self.orbital_period,
            "rotation_period": self.rotation_period,
            "diameter": self.diameter
        }
class Characters(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    birth_year = db.Column (db.Integer)
    gender = db.Column (db.String)
    height = db.Column (db.Integer)
    hair_color = db.Column (db.String)
    skin_color = db.Column (db.String)
    eye_color = db.Column (db.String)

    def __repr__(self):
        return f'{self.birth_year}'

    def serialize(self):
        return {
            "id": self.id,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "height": self.height,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color
        }
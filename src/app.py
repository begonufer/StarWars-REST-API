"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Favorite, Planets, Characters

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/users', methods=['GET'])
def get_users():

    return jsonify([user.serialize() for user in User.query.all()]),200

@app.route('/user/favorites', methods=['GET'])
def get_favorites():

    return jsonify([favorites.serialize() for favorites in Favorite.query.all()]),200

@app.route('/planets', methods=['GET'])
def get_planets():

    return jsonify([planets.serialize() for planets in Planets.query.all()]),200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_one_planet(planet_id):
    
    one_planet = Planets.query.get(planet_id)

    return jsonify([one_planet.serialize()]), 200

@app.route('/characters', methods=['GET'])
def get_characters():

    return jsonify([characters.serialize() for characters in Characters.query.all()]),200

@app.route('/characters/<int:character_id>', methods=['GET'])
def get_one_character(character_id):

    one_character = Characters.query.get(character_id)

    return jsonify([one_character.serialize()]), 200

@app.route('/user/favorites/planet', methods=['POST'])
def new_planet_favorite():

    favorite = Favorite()
    favorite.user_id = request.json.get("user_id")
    favorite.planet_id = request.json.get("planet_id", None)
    db.session.add(favorite)
    db.session.commit()

    return jsonify(favorite.serialize()),200

@app.route('/user/favorites/character', methods=['POST'])
def new_character_favorite():

    favorite = Favorite()
    favorite.user_id = request.json.get("user_id")
    favorite.character_id = request.json.get("character_id", None)
    db.session.add(favorite)
    db.session.commit()

    return jsonify(favorite.serialize()),200

@app.route('/user/favorites/planet/<int:planet_id>', methods=['DELETE'])
def delete_planet_favorite(planet_id):
    
    favorite = Favorite.query.filter_by(planet_id=planet_id).first()
    db.session.delete(favorite)
    db.session.commit()

    return jsonify({"mensaje": "Planeta eliminado de la lista de favoritos correctamente"}),200  

@app.route('/user/favorites/character/<int:character_id>', methods=['DELETE'])
def delete_character_favorite(character_id):
    
    favorite = Favorite.query.filter_by(character_id=character_id).first()
    db.session.delete(favorite)
    db.session.commit()

    return jsonify({"mensaje": "Personaje eliminado de la lista de favoritos correctamente"}),200 

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

from flask import Blueprint
from app import db
from app.models.planet import Planet
from flask import request, Blueprint, make_response, jsonify

solar_system_bp = Blueprint("solar_system", __name__, url_prefix='/planets')


@solar_system_bp.route('', methods=['GET', 'POST'])
def handle_books():
    if request.method == 'GET':
        #return full list of planets
        solar_system = Planet.query.all()
        solar_system_response = []
        for planet in solar_system:
            solar_system_response.append({
                'id': planet.id,
                'name': planet.name,
                'description': planet.description
            })
        return jsonify(solar_system_response)
    elif request.method == 'POST':
        #create a planet to the database
        request_body = request.get_json()
        new_planet = Planet(name=request_body['name'],
                        description=request_body['description'])
        db.session.add(new_planet)
        db.session.commit()
        return make_response(f'Planet {new_planet.name} successfully created', 201)
    
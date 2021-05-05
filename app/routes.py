from flask import Blueprint
from app import db
from app.models.planet import Planet
from flask import request, Blueprint, make_response, jsonify

solar_system_bp = Blueprint("solar_system", __name__, url_prefix='/planets')


@solar_system_bp.route('', methods=['GET', 'POST'])
def handle_planets():
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
        #create all planets to the database
        request_body = request.get_json()
        new_planet = Planet(name=request_body['name'],
                        description=request_body['description'])
        db.session.add(new_planet)
        db.session.commit()
        return make_response(f'Planet {new_planet.name} successfully created', 201)


@solar_system_bp.route("/<a_planet_id>", methods=['GET', 'DELETE', 'PUT'])
def handle_planet(a_planet_id):
    planet = Planet.query.get(a_planet_id)
    if not planet:
        return ({
            "message": f"Planet with id {a_planet_id} was not found",
            "success": False
        }, 404)
    if request.method == 'GET':
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description
        }, 200

    elif request.method == 'DELETE':
        db.session.delete(planet)
        db.session.commit()
        return ({
            "message": f"Planet with id {a_planet_id} was deleted",
            "success": True
        }, 200) 

    elif request.method == 'PUT':
        if "name" in request_body:
            planet.name = request_body["name"]
        if "description" in request_body:
            planet.description = request_body["description"]

    
    

    


    
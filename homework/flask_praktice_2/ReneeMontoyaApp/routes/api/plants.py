from app import app, api, db
from models import Plant
from flask import request
from flask_restful import Resource
from utils.helpers import convert_list


class PlantResource(Resource):
    def get(self):
        plants = Plant.query.all()
        return convert_list(plants)

    def post(self):
        data = request.json
        plant = Plant(location=data['location'], name=data['name'])
        db.session.add(plant)
        db.session.commit()
        return plant.serialize


class PlantSingleResource(Resource):
    def get(self, id):
        try:
            plant = Plant.query.get(id)
            return plant.serialize
        except Exception:
            return f"ERROR: The Plant with the ID {id} not found", 404

    def put(self, id):
        data = request.json
        plant = Plant.query.get(id)
        plant.name = data['name'] if data.get('name', False) else plant.name
        plant.location = data['location'] if data.get('location', False) else plant.location
        plant.director_id = data['director_id'] if data.get('director_id', False) else plant.director_id
        db.session.add(plant)
        db.session.commit()
        return plant.serialize

    def delete(self, id):
        try:
            plant = Plant.query.get(id)
            db.session.delete(plant)
            db.session.commit()
            return f"WARNING: The Plant with the ID {id} was destroyed", 204
        except Exception:
            return f"ERROR: The Plant with the ID {id} not found", 404


class PlantDirectorResource(Resource):
    def get(self, id):
        try:
            plant = Plant.get_by_id(id)
            director = Plant.director(plant['director_id'])
            if director is None:
                return "Director Not Found", 404
            return director
        except Exception:
            return "Not Found", 404


api.add_resource(PlantResource, "/api/v1/plants")
api.add_resource(PlantSingleResource, "/api/v1/plants/<int:id>")
api.add_resource(PlantDirectorResource, '/api/v1/plants/<int:id>/director')

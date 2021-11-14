from app import app, api, db
from flask import request, Response
from flask_restful import Resource
from models import Salon
from utils.helpers import convert_list


class SalonResource(Resource):
    def get(self):
        salons = Salon.query.all()
        return convert_list(salons)

    def post(self):
        data = request.json
        salon = Salon(
            name=data['name'],
            city=data['city'],
            address=data['address']
        )
        db.session.add(salon)
        db.session.commit()
        return salon.serialize


class SalonSingleResource(Resource):
    def get(self, id):
        salon = Salon.query.get(id)
        return salon.serialize

    # def put(self, id):
    #     data = request.json
    #     Plant.update_by_id(id, data)
    #     return Plant.get_by_id(id)

    def delete(self, id):
        salon = Salon.query.get(id)
        db.session.delete(salon)
        db.session.commit()
        return "", 204


# class SalonDirectorResource(Resource):
#     def get(self, id):
#         try:
#             salon = Salon.get_by_id(id)
#             director = Salon.director(salon['director_id'])
#             if director is None:
#                 return "Director Not Found", 404
#             return director
#         except Exception:
#             return "Not Found", 404


# api.add_resource(SalonDirectorResource, '/api/v1/salons/<int:id>/director')
api.add_resource(SalonResource, "/api/v1/salons")
api.add_resource(SalonSingleResource, "/api/v1/salons/<int:id>")

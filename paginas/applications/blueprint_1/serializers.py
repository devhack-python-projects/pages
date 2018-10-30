from flask_restful import fields
from flask_restful.reqparse import RequestParser

parser = RequestParser()

parser.add_argument(
    'titulo',
    dest='titulo',
    location='form',
    required=True
)

parser.add_argument(
    'contenido',
    dest='contenido',
    location='form',
    required=True
)

parser.add_argument(
    'propietario',
    dest='propietario',
    location='form',
    required=True
)

pagina_fields = {
    "id": fields.Integer,
    "titulo": fields.String,
    "contenido": fields.String,
    "propietario": fields.String
}
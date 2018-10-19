from flask.views import View
from flask.templating import render_template
from flask.helpers import url_for, request, flash
from flask.globals import g
from werkzeug.utils import redirect
import requests
import json

from . import (
    conf,
    models
)

def tokenIsValid(jwtvalidar):
    valorHeader = {"Authorization":jwtvalidar}
    codigoRespuesta = requests.get(conf.MICRO_AUTH,headers=valorHeader)
    jsonData = json.loads(codigoRespuesta.content)
    if jsonData['status'] == 'OK':
        return True
    return False

class Read(View):
    methods = ["GET"]
    def dispatch_request(self):
        if request.method == "GET":
            jwtValidar = request.headers['Authorization']
            if tokenIsValid(jwtValidar):
                print ("codigo para listar paginas")
            else:
                print ("Token no valido")

            return ""
        return ""


class Create(View):
    methods = ["POST"]
    def dispatch_request(self):
        if request.method == "POST":
            jwtValidar = request.headers['Authorization']
            if tokenIsValid(jwtValidar):
                print ("codigo para CREAR pagina")
            else:
                print ("Token no valido")

            return ""
        return ""


class Delete(View):
    methods = ["POST"]
    def dispatch_request(self):
        if request.method == "POST":
            jwtValidar = request.headers['Authorization']
            if tokenIsValid(jwtValidar):
                print ("codigo para BORRAR pagina")
            else:
                print ("Token no valido")

            return ""
        return ""


class Update(View):
    methods = ["POST"]
    def dispatch_request(self):
        if request.method == "POST":
            jwtValidar = request.headers['Authorization']
            if tokenIsValid(jwtValidar):
                print ("codigo para ACTUALIZAR pagina")
            else:
                print ("Token no valido")

            return ""
        return ""
from flask.views import View
from flask.templating import render_template
from flask.helpers import url_for, request, flash
from flask.globals import g
from werkzeug.utils import redirect
from werkzeug.exceptions import abort
import requests
import json
import jwt
from . import (
    conf,
    models
)


class MixClassValidateToken(object):

    def tokenIsValid(self):
        jwtValidar = request.headers['Authorization']
        valorHeader = {"Authorization": jwtValidar}
        print(jwt.decode(jwtValidar.replace("JWT ", ""), verify=False))
        codigoRespuesta = requests.get(conf.MICRO_AUTH, headers=valorHeader)
        jsonData = json.loads(codigoRespuesta.content)
        if jsonData['status'] == 'OK':
            return True
        return False

    def dispatch_request(self):
        if not self.tokenIsValid():
            abort(401)


class Read(MixClassValidateToken, View):
    methods = ["GET"]
    def dispatch_request(self):

        if request.method == "GET":
            jwtValidar = request.headers['Authorization']
            if self.tokenIsValid():
                print ("codigo para listar paginas")
            else:
                print ("Token no valido")

            return ""
        return ""


class Create(View):
    methods = ["POST"]
    def dispatch_request(self):
        super(Create, self).dispatch_request()
        id = request.form('id')
        username = request.form('username')
        nombres = request.form('nombres')

        usuario = models.Usuario(

        )


class Delete(View):
    methods = ["POST"]
    def dispatch_request(self):
        super(Delete, self).dispatch_request()


class Update(MixClassValidateToken, View ):
    methods = ["POST"]
    def dispatch_request(self):
        super(Update, self).dispatch_request()




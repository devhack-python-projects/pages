from flask.views import View
from flask.templating import render_template
from flask.helpers import url_for, request, flash
from flask.globals import g
from werkzeug.utils import redirect

from . import (
    conf,
    models
)


class Listar(View):
    methods = ["GET", "POST"]
    def dispatch_request(self):
        return render_template('[nombre_plantilla].html', **context)
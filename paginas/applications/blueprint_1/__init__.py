import functools
import os

from flask.blueprints import Blueprint
from . import conf
from flask_restful import Api

bp = Blueprint(
    conf.BLUEPRINT_NAME,
    __name__,
    url_prefix='/',
)

from .urls import load_urls
load_urls()
from . import models

api_bp = Api(bp, "api")
from .urls_api import load_urls as load_urls_api
load_urls_api()

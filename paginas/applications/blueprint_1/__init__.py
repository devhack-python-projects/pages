import functools
import os

from flask.blueprints import Blueprint
from . import conf

bp = Blueprint(
    conf.BLUEPRINT_NAME,
    __name__,
    url_prefix='/',
)

from .urls import load_urls
load_urls()
from . import models

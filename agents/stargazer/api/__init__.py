from sanic import Blueprint

from api.example import example_router
from api.collect import collect_router
from api.monitor import monitor_router

BLUEPRINTS = [collect_router, example_router, monitor_router]

api = Blueprint.group(*BLUEPRINTS, url_prefix="/api")

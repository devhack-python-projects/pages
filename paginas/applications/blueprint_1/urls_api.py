from . import (
    api,
    api_bp
)


def load_urls():
    api_bp.add_resource(api.Pagina, "/pagina/")
    # api_bp.add_resource(api.Pagina, "/api/crear/")
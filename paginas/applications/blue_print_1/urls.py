from . import (
    views,
)

def load_urls():
    bp.add_url_rule(
        "/listar/",
        view_func=views.Listar.as_view(conf.cadena_lista)
    )
from . import (
    bp,
    views,
    conf
)

def load_urls():
    bp.add_url_rule(
        "/crear/",
        view_func=views.Create.as_view(conf.VIEW_CREAR)
    )
    bp.add_url_rule(
        "/listar/",
        view_func=views.Read.as_view(conf.VIEW_LISTAR)
    )
    bp.add_url_rule(
        "/actualizar/",
        view_func=views.Update.as_view(conf.VIEW_ACTUALIZAR)
    )
    bp.add_url_rule(
        "/borrar/",
        view_func=views.Delete.as_view(conf.VIEW_BORRAR)
    )
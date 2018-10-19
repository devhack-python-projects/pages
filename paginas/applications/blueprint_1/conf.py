BLUEPRINT_NAME = "nombreblueprint"
VIEW_LISTAR = "view_listar"
VIEW_CREAR = "view_crear"
VIEW_ACTUALIZAR = "view_actualizar"
VIEW_BORRAR = "view_borrar"
MICRO_AUTH = "http://ma0collazos.pythonanywhere.com/verify/"
TOKEN_PRUEBA = "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTI3ODc0MzUsIm5iZiI6MTUzOTgyNzQzNSwiaXNzIjoiYXV0aC5kZXZoYWNrLXB5dGhvbi0yMDE4LWkiLCJhdWQiOiIqLmRldmhhY2stcHl0aG9uLTIwMTgtaSIsImlhdCI6MTUzOTgyNzQzNSwibmFtZSI6IiAiLCJnaXZlbl9uYW1lIjoiIiwiZmFtaWx5X25hbWUiOiIiLCJlbWFpbCI6IiIsInByZWZlcnJlZF91c2VybmFtZSI6InVzdWFyaW9wYWdpbmFiIn0.m0ERs_CSdSfkPVvH-o4E3GyzC5st1lsIhonyOlTyddA"

def get_prefixed_url(url):
    return "{}.{}".format(BLUEPRINT_NAME, url)
import requests


def main():
    valorHeader = {"Authorization":"JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTI3ODc0MzUsIm5iZiI6MTUzOTgyNzQzNSwiaXNzIjoiYXV0aC5kZXZoYWNrLXB5dGhvbi0yMDE4LWkiLCJhdWQiOiIqLmRldmhhY2stcHl0aG9uLTIwMTgtaSIsImlhdCI6MTUzOTgyNzQzNSwibmFtZSI6IiAiLCJnaXZlbl9uYW1lIjoiIiwiZmFtaWx5X25hbWUiOiIiLCJlbWFpbCI6IiIsInByZWZlcnJlZF91c2VybmFtZSI6InVzdWFyaW9wYWdpbmFiIn0.m0ERs_CSdSfkPVvH-o4E3GyzC5st1lsIhonyOlTyddA"}
    codigoRespuesta = requests.get('http://ma0collazos.pythonanywhere.com/verify/',headers=valorHeader)

    print (codigoRespuesta.content)


if __name__ == '__main__':
    main()

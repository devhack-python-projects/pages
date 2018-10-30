from paginas.database import database


class Usuario(database.Model):
    id = database.Column(
        database.Integer,
        primary_key=True
    )
    username = database.Column(
        database.Text,
        nullable=False
    )
    nombres = database.Column(
        database.Text,
        nullable=False
    )

    def __str__(self):
        return "Soy ".format(self.username)


class Pagina(database.Model):
    id = database.Column(
        database.Integer,
        primary_key=True
    )
    titulo = database.Column(
        database.Text,
        nullable=False
    )
    contenido = database.Column(
        database.Text,
        nullable=False
    )
    propietario = database.Column(
        database.Text,
        database.ForeignKey('usuario.username')
    )

    def __str__(self):
        return "Pagina: {} , creado por {}".format(self.titulo, self.propietario)


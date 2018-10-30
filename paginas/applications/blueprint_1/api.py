from flask_restful import Resource, marshal_with

from . import(
    models,
    serializers,
    views
)

class Pagina(Resource):
    @marshal_with(serializers.pagina_fields)
    def get(self):
        print(models.Pagina.query.all())
        return models.Pagina.query.all()

    @marshal_with(serializers.pagina_fields)
    def post(self):
        super(Pagina, self).dispatch_request()
        args = serializers.parser.parse_args()
        print(args)

        pagina = models.Pagina(
            titulo=args.titulo,
            contenido=args.contenido,
            propietario=args.propietario
        )

        models.database.session.add(pagina)
        models.database.session.commit()
        return pagina


class PaginaWithId(Resource):
    pass

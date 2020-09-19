from flask_marshmallow import Marshmallow
from inflection import camelize

ma = Marshmallow()


class CamelCaseSQLAlchemySchema(ma.SQLAlchemyAutoSchema):

    def on_bind_field(self, field_name, field_obj):
        field_obj.data_key = camelize(field_obj.data_key or field_name, False)

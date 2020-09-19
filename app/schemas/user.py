from app.models.user import User

from . import CamelCaseSQLAlchemySchema


class UserSchema(CamelCaseSQLAlchemySchema):
    class Meta:
        model = User
        exclude = ('password_hash', )

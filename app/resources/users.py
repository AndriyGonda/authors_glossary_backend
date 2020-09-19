from app.helpers.api_resource import APIResource
from app.schemas.user import UserSchema
from app.models.user import User


class Users(APIResource):
    model = User
    schema = UserSchema

    def get(self):
        users = self.model.query.all()
        return self.schema().dump(users, many=True)

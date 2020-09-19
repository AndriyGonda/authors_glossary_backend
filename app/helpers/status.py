
class Status(object):

    @staticmethod
    def _send(status: str, code: int, description=None):
        message = dict(
            status=status,
            description=description
        )
        return message, code

    @classmethod
    def ok(cls, description=None):
        return cls._send('OK', 200, description)

    @classmethod
    def unknown(cls, description=None):
        return cls._send('Unknown error', 500, description)

    @classmethod
    def not_found(cls, description=None):
        return cls._send('Not found', 404, description)

    @classmethod
    def already_exists(cls, description=None):
        return cls._send('Already exists', 400, description)

    @classmethod
    def deleted(cls):
        return cls._send('Deleted', 202)

    @classmethod
    def cannot_login(cls, description=None):
        return cls._send('Cannot login with current credentials', 401, description)

    @classmethod
    def unauthorized(cls, description=None):
        return cls._send('Unauthorized', 401, description)

    @classmethod
    def permission_denied(cls, description=None):
        return cls._send('Permission denied', 400, description)

    @classmethod
    def bad_request(cls, description=None):
        return cls._send('Bad request', 400, description)


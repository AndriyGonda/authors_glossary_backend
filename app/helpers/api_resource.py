from flask_restful import Resource, abort
from .request_parser import RequestParser
from .status import Status

class _BaseMeta(type):
    def __new__(mcs, name, bases, attrs):
        model = attrs.get('model', None)
        schema = attrs.get('schema', None)
        klass = super().__new__(mcs, name, bases, attrs)
        setattr(klass, 'model', model)
        setattr(klass, 'schema', schema)
        return klass


class _ResourceMeta(type(Resource), _BaseMeta):
    pass


def abort_with_status(status_fn, description=None):
    status, code = status_fn(description)
    return abort(code, status=status['status'], description=status['description'])


class APIResource(Resource, metaclass=_ResourceMeta):
    def __init__(self):
        super(APIResource, self).__init__()
        self._parser = RequestParser()

    def get_or_404(self, item_id):
        item = self.model.query.filter_by(id=item_id).first()
        if item is None:
            not_found, code = Status.not_found(f'item with id {item_id} not found')
            return abort(code, status=not_found['status'], description=not_found['description'])
        return item

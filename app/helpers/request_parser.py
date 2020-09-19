from typing import List
from dataclasses import dataclass
from flask_restful import reqparse
from inflection import underscore


@dataclass
class RequestArgument:
    name: str
    type: type = str
    help: str = ''
    required: bool = False
    location: str = 'json'
    action: str = 'store'
    default: str or int = None
    nullable: bool = True


class RequestParser(reqparse.RequestParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_arguments(self, arguments: List[RequestArgument]):
        for argument in arguments:
            if not len(argument.help):
                self.add_argument(
                    argument.name,
                    type=argument.type,
                    required=argument.required,
                    location=argument.location
                )
            else:
                self.add_argument(
                    argument.name,
                    type=argument.type,
                    required=argument.required,
                    help=argument.help,
                    location=argument.location
                )

    def get_not_none_values(self):
        args = self.parse_args()
        return {key: value for key, value in args.items() if value is not None}

    def get_underscore_not_none_values(self):
        args = self.parse_args()
        return {underscore(key): value for key, value in args.items() if value is not None}

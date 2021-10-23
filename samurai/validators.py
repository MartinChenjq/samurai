from cerberus import Validator

schema = {'name': {'type': 'string', 'required': True}}
user_schema = Validator(schema)

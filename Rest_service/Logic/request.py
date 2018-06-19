from jsonschema import validate, ValidationError

from Rest_service.Models.RequestModels.request_schema import request_schema


def validate_request(request_data):
    try:
        validate(request_data, request_schema)
        return True
    except ValidationError:
        return False



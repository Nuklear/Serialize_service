from jsonschema import validate, ValidationError
from src.Models.ResponseModels.response_schema import response_schema


def validate_response(response_data):
    try:
        validate(response_data, response_schema)
        return True
    except ValidationError:
        return False

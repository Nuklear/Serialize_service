from aiohttp import web
from Rest_service.Logic.request import validate_request
from Rest_service.Logic.GetResults import get_data_from_json

routes = web.RouteTableDef()


@routes.get('/')
async def hello(request):
    return web.json_response({})


@routes.post('/')
async def hello(request):
    try:
        data = await request.json()
    except Exception as ex:
        print("request error - {0}", ex)
        return web.json_response({"data": "error"}, status=400)
    if validate_request(data):
        result = get_data_from_json(data)
        return web.json_response(result, status=200)
    else:
        return web.json_response({"data": "validation error"}, status=400)

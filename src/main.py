from aiohttp import web
from src.routes import routes


app = web.Application()
app.add_routes(routes)

web.run_app(app, port=8080)
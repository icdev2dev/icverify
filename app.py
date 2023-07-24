from flask import Flask, send_from_directory, request
import asyncio
import aiohttp

from backend.be_funcs import register_be_funcs

app = Flask(__name__)

@app.route("/")
def index ():
    return send_from_directory("frontend/dist", "index.html")
@app.route("/<path:path>")
def path_to_svelte(path):
    return send_from_directory("frontend/dist", path)


async def run_app():
    await app.run()


if __name__ == "__main__":

    register_be_funcs(app=app)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_app())

#    app.run(debug=True) 


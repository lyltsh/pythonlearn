from sanic import Sanic
from sanic.response import json, text
from my_blueprint import bp


"""
参考：https://sanic.readthedocs.io/en/latest/index.html
"""
app = Sanic()


@app.route("/test")
async def test(request):
    return json({"hello": "world"})


# 增加输入参数
@app.route("/tag/<tag>")
async def tag(request, tag):
    return text('Tag-{}'.format(tag))


# 限定参数类型
@app.route('/number/<integer_arg:int>')
async def integer_handler(request, integer_arg):
    return text('Integer - {}'.format(integer_arg))


@app.route('/number/<number_arg:number>')
async def number_handler(request, number_arg):
    return text('Number - {}'.format(number_arg))


@app.route('/person/<name:[A-z]+>')
async def person_handler(request, name):
    return text('Person - {}'.format(name))


@app.route('/folder/<folder_id:[A-z0-9]{0,4}>')
async def folder_handler(request, folder_id):
    return text('Folder - {}'.format(folder_id))


# 限定methods
@app.route('/post', methods=['POST'])
async def post_handler(request):
    return text('POST request - {}'.format(request.json))


#
# @app.route('/get', methods=['GET'])
# async def get_handler(request):
#     return text('GET request - {}'.format(request.args))


# 限定host
@app.route('/get', methods=['GET'], host='localhost')
async def get_handler(request):
    return text('GET request - {}'.format(request.args))


# if the host header doesn't match example.com, this route will be used
@app.route('/get', methods=['GET'])
async def get_handler(request):
    return text('GET request in default - {}'.format(request.args))
    # return text('GET request in default - {}'.format(request.json))


"""
Middleware And Listeners
Middleware are functions which are executed before or after requests to the server. 
They can be used to modify the request to or response from user-defined handler functions.
Additionally, Sanic provides listeners which allow you to run code at various points of your application's lifecycle.
"""


# not modify the request and response
@app.middleware('request')
async def print_on_request(request):
    print("I print when a request is received by the server")


@app.middleware('response')
async def print_on_response(request, response):
    print("I print when a response is returned by the server")


# modify the request and response
@app.middleware('response')
async def custom_banner(request, response):
    response.headers["Server"] = "Fake-Server"


@app.middleware('response')
async def prevent_xss(request, response):
    response.headers["x-xss-protection"] = "1; mode=block"


"""
Listeners
If you want to execute startup/teardown code as your server starts or closes, you can use the following listeners:
"""


@app.listener('before_server_start')
async def setup_db(app, loop):
    # app.db = await db_setup()
    print('before_server_start')


@app.listener('after_server_start')
async def notify_server_started(app, loop):
    print('Server successfully started!')


@app.listener('before_server_stop')
async def notify_server_stopping(app, loop):
    print('Server shutting down!')


@app.listener('after_server_stop')
async def close_db(app, loop):
    # await app.db.close()
    print('after_server_stop')


"""
Blueprints
Blueprints are objects that can be used for sub-routing within an application. 
Instead of adding routes to the application instance, blueprints define similar methods for adding routes, 
which are then registered with the application in a flexible and pluggable manner.

Blueprints are especially useful for larger applications, where your application logic can be broken down into several 
groups or areas of responsibility.
"""
app.blueprint(bp)


def main():
    app.run(host='0.0.0.0', port=8000)


if __name__ == '__main__':
    main()

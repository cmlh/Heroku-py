import gunicorn
from bottle import request, response, route
import bottle
from sys import argv

@route('/')
def index():
    return 'Hello!'

bottle.run(server='gunicorn', host='0.0.0.0', port=argv[1])
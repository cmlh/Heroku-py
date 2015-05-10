import gunicorn
from bottle import request, response, route
import bottle
from sys import argv

@route('/')
def index():
    return 'Hello!'

@route('/oauth/authorise/basic', method=['GET','POST'])
def oauth_redirect():
    return 'Hello!'
    
@route('/oauth/access/token', method=['GET','POST'])
def oauth_access_token():
    return 'Hello!'

@bottle.route('/oauth/redirect')
def oauth_redirect():
    return 'Hello!'

bottle.run(server='gunicorn', host='0.0.0.0', port=argv[1])
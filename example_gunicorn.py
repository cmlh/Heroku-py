import gunicorn
from bottle import request, response, route
import bottle
from sys import argv

@route('/')
def index():
    return 'Hello!'

@route('/oauth/authorise/basic', method=['GET','POST'])
def instagram_oauth_redirect():
    if request.body.len>0:
        return 'Hello!'
    
@route('/instagram/oauth/access/token', method=['GET','POST'])
def instagram_oauth_access_token():
    if request.body.len>0:
        return 'Hello!'

@bottle.route('/oauth/redirect')
def oauth_redirect():
    return 'Hello!'

bottle.run(server='gunicorn', host='0.0.0.0', port=argv[1])
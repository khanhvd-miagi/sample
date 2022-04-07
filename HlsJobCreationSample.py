from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os

import hashlib
import json

import boto3

def playv(request):
	
    return Response("OK")

if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    with Configurator() as config:
        config.add_route('playv', '/')
        config.add_view(playv, route_name='playv')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()
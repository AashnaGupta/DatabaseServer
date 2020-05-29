import wsgiref.simple_server
import urllib.parse
from database import Simpledb


def application(environ, start_response):
    headers = [('Content-Type', 'text/plain; charset=utf-8')]

    path = environ['PATH_INFO']
    params = urllib.parse.parse_qs(environ['QUERY_STRING'])

    #db = Simpledb('data.txt')

    if path == '/insert':
        start_response('200 OK', headers)
        params1 = params['key'][0]
        params2 = params['value'][0]
        Simpledb.add("data.txt",str(params1),int(params2))    
        return ["INSERTED".encode()]

    elif path == '/select':
        params1 = params['key'][0]
        print (params1)
        s= Simpledb.find("data.txt",str(params1))
        start_response('200 OK', headers)
        if s != None:
        
            return ["RETRIEVED: ".encode() + str(s).encode()]
        else:
            return ['NULL'.encode()]

    elif path == '/delete':
        start_response('200 OK', headers)
        params1 = params['key'][0]
        s= Simpledb.delete("data.txt",str(params1))
        return ["DELETED".encode()]
    
    elif path == '/update':
        params1 = params['key'][0]
        params2 = params['value'][0]
        Simpledb.update("data.txt",str(params1),int(params2)) 
        start_response('200 OK', headers)
        return ["UPDATED".encode()]
    
    else:
        start_response('404 Not Found', headers)
        return ['Status 404: Resource not found'.encode()]


httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()

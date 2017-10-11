
import argparse

import sys
import itertools
import socket
from socket import socket as Socket
from os import curdir, sep

# A simple web server

# Issues:
# Ignores CRLF requirement
# Header must be < 1024 bytes
# ...
# probabaly loads more


def main():

    # Command line arguments. Use a port > 1024 by default so that we can run
    # without sudo, for use as a real server you need to use port 80.
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', '-p', default=2080, type=int,
                        help='Port to use')
    args = parser.parse_args()

    # Create the server socket (to handle tcp requests using ipv4), make sure
    # it is always closed by using with statement.
    #with Socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

    # COMPLETE (1)
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # The socket stays connected even after this script ends. So in order
    # to allow the immediate reuse of the socket (so that we can kill and
    # re-run the server while debugging) we set the following option. This
    # is potentially dangerous in real code: in rare cases you may get junk
    # data arriving at the socket.
    ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # COMPLETE (2)
    endpoint = ('',args.port)
    # COMPLETE (3)
    ss.bind(endpoint)
    ss.listen(5) 

    print("server ready")

    while True:

         cs = ss.accept()[0] 
         request = cs.recv(1024).decode('ascii')
         print(request)
         reply = http_handle(request)
         cs.send(reply)

         print("\n\nReceived request")
         print("======================")
         print(request.rstrip())
         print("======================")


         print("\n\nReplied with")
         print("======================")
         print(reply.rstrip())
         print("======================")


    return 0


def http_handle(request_string):
    """Given a http requst return a response
    Both request and response are unicode strings with platform standard
    line endings.
    """
    
    assert not isinstance(request_string, bytes)

    # Fill in the code to handle the http request here. You will probably want
    # to write additional functions to parse the http request into a nicer data
    # structure (eg a dict), and to easily create http responses.

    try:
        request = request_string.split(" ")
        if (request[1] == "/"):
           request = "index.html"
           myfile = open(request, 'rb')
           data = myfile.read()
           headers = "HTTP/1.1 200 OK\n" + "Content-Type: text/html\n" + "Connection: close\n" + "\n"
           answer = bytes(headers, 'UTF-8') + data
           myfile.close()
           return answer

        elif (request[1].endswith(".jpg")):
           request = request[1][1:] 
           myfile = open(request, 'rb')
           data = myfile.read()
           headers = "HTTP/1.1 200 OK\n" + "Content-Type: image/jpg\n" + "Connection: close\n" + "\n"
           answer = bytes(headers, 'UTF-8') + data
           myfile.close()
           return answer

        elif (request[1].endswith(".html")):
           request = request[1][1:]
           myfile = open(request, 'rb')
           data = myfile.read()
           headers = "HTTP/1.1 200 OK\n" + "Content-Type: text/html\n" + "Connection: close\n" + "\n"
           answer = bytes(headers, 'UTF-8') + data
           myfile.close()
           return answer

        elif (request[1].endswith(".css")):
           request = request[1][1:] 
           myfile = open(request, 'rb')
           data = myfile.read()
           headers = "HTTP/1.1 200 OK\n" + "Content-Type: text/css\n" + "Connection: close\n" + "\n"
           answer = bytes(headers, 'UTF-8') + data
           myfile.close()
           return answer

        elif (request[1].endswith(".gif")):
           request = request[1][1:] 
           myfile = open(request, 'rb')
           data = myfile.read()
           headers = "HTTP/1.1 200 OK\n" + "Content-Type: image/gif\n" + "Connection: close\n" + "\n"
           answer = bytes(headers, 'UTF-8') + data
           myfile.close()
           return answer

        elif (request[1].endswith(".js")):
           request = request[1][1:] 
           myfile = open(request, 'rb')
           data = myfile.read()
           headers = "HTTP/1.1 200 OK\n" + "Content-Type: application/javascript\n" + "Connection: close\n" + "\n"
           answer = bytes(headers, 'UTF-8') + data
           myfile.close()
           return answer
	
        else: 
              request = "error404.html"
              myfile = open(request, 'rb')
              data = myfile.read()
              headers = "HTTP/1.1 404 ERROR\n" + "Content-Type: text/html\n" + "Connection: close\n" + "\n"
              answer = bytes(headers, 'UTF-8') + data
              myfile.close()
              return answer

    except IOError:
       request = "error404.html"
       myfile = open(request, 'rb')
       data = myfile.read()
       headers = "HTTP/1.1 404 ERROR\n" + "Content-Type: text/html\n" + "Connection: close\n" + "\n"
       answer = bytes(headers, 'UTF-8') + data
       myfile.close()
       return answer

    # COMPLETE (4)
    # esta funcion DEBE RETORNAR UNA CADENA que contenga el recurso (archivo)
    # que se consulta desde un navegador e.g. http://localhost:2080/index.html
    # En el ejemplo anterior se esta solicitando por el archivo 'index.html'
    # Referencias que pueden ser de utilidad
    # - https://www.acmesystems.it/python_http, muestra como enviar otros
    #                                           archivos ademas del HTML
    # - https://goo.gl/i7hJYP, muestra como construir un mensaje de respuesta
    #                       

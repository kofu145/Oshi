import socket
import select
import sys

host = "127.0.0.1"
port = 37560

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((host, port))

while True:

    # maintains a list of possible input streams
    sockets_list = [sys.stdin, server]

    """ There are two possible input situations. Either the
    user wants to give manual input to send to other people,
    or the server is sending a message to be printed on the
    screen. Select returns from sockets_list, the stream that
    is reader for input. So for example, if the server wants
    to send a message, then the if condition will hold true
    below.If the user wants to send a message, the else
    condition will evaluate as true"""
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])

    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            print (message)
        else:
            message = input()
            server.send(message.encode())
            print("<You>" + " %s"%message)
            sys.stdout.flush()
server.close()
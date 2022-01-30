import socket
import selectors
import OshiNetCore

host = "127.0.0.1"
port = 37560


# ALL abstractions will happen in oshinetcore.server


sel = selectors.DefaultSelector()

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.bind((host, port))
server_sock.listen()
server_sock.setblocking(False)
print(f"Started server on {host}, {port}")
header_length = 10

print("")

# socket is key, clients is data
clients = {}

sel.register(server_sock, selectors.EVENT_READ, data=None)

def process_msg(sock):

    try:
        msg_hdr = sock.recv(10)

        if not len(msg_hdr):
            return False

        msg_len = int(msg_hdr.decode('utf-8').strip())

        return {'header': msg_hdr, 'data': sock.recv(msg_len)}
    except:
        return False

def accept_connection(clients, sock):

    try:
        conn, addr = sock.accept()
        conn.setblocking(False)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        print("before processing first msg")
        # get first message
        # first message after connection will be
        # username info/otherwise

        data = process_msg(sock)
        print(data)
        if not data:
            return
        print("msg processed")
        clients[sock] = data['header']

        sel.register(conn, events, data=data)
        print(f"Accepted new connection {data['header']} from {addr}")
    except Exception as e:
        print(e)
        print("failed!")

def broadcast(clients, message, sender_sock):
    sender = clients[sender_sock]
    for client in clients:
        if client != sender_sock:
            client.send(sender['header'] + 
                sender['data'] + 
                message['header'] + 
                message['data'])


try:
    while True:
        # blocks until sockets are ready for I/O, returns a list of
        # (key, event) tuples per socket
        events = sel.select(timeout=None)
        for key, mask in events:
            print(repr(key.data))
            # means we have a client to connect
            if key.data is None:
                # accept connection
                # key.fileobj = our socket
                accept_connection(clients, key.fileobj)
                
            # means we have data from a client to manage
            else:
                # process whatever message
                message = process_msg(key.fileobj)
                print(f'Received message from {clients[key.fileobj]["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')


                if message == False:
                    # close socket
                    sel.unregister(key.fileobj)

                    del clients[key.fileobj]

                    continue

                # broadcast message to everyone but sender
                broadcast(clients, message, key.fileobj)

except:
    pass
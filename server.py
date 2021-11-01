import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# this is to avoid an exception for "Address already in use"
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


host = "127.0.0.1"
port = 37560


server.bind((host, port))

server.listen(10)
#server.setblocking(False)


clients = []


def clientthread(conn, addr):

    # sends a message to the client whose user object is conn
    conn.send("Welcome to this chatroom!".encode())

    while True:
        try:
            message = conn.recv(2048)
            if message:

                """prints the message and address of the
                user who just sent the message on the server
                terminal"""
                print ("<" + addr[0] + "> " + message.decode())

                # Calls broadcast function to send message to all
                message_to_send = "<" + addr[0] + "> " + message.decode()
                broadcast(message_to_send.encode(), conn)

            else:
                """message may have no content if the connection
                is broken, in this case we remove the connection"""
                remove(conn)

        except:
            continue

"""Using the below function, we broadcast the message to all
clients who's object is not the same as the one sending
the message """
def broadcast(message, connection):
    for client in list_of_clients:
        if client!=connection:
            try:
                client.send(message)
            except:
                client.close()
 
                # if the link is broken, we remove the client
                remove(client)


"""The following function simply removes the object
from the list that was created at the beginning of
the program"""
def remove(connection):
    if connection in clients:
        clients.remove(connection)


while True:

    """Accepts a connection request and stores two parameters,
    conn which is a socket object for that user, and addr
    which contains the IP address of the client that just
    connected"""
    conn, addr = server.accept()

    """Maintains a list of clients for ease of broadcasting
    a message to all available people in the chatroom"""
    clients.append(conn)

    # prints the address of the user that just connected
    print (addr[0] + " connected")

    # creates and individual thread for every user
    # that connects
    client_thread = threading.Thread(target=clientthread, args=(conn,addr))  

    client_thread.start()

conn.close()
server.close()

# NOTE: Despite being quite planned out, this project has been dropped for a while - plan to pick it back up mid summer 2024

# Oshi
A chat application utilizing various methods (mainly websockets for now) for networking.
Currently, various ones are being developed and tested.

The front-end is based on the Kivy framework, supported by websockets for connections.

## An Overall Look

### Networking Backend
**Utilizing Websockets**

The networking library is just the websockets library - may look into pairing an API as
well as using flask-websockets.

### Accessing the Network
**Making your own client**

It's currently being implemented right now, so nothing here yet.

## How does it all work?

### Handling client connections
Depending on what the user has selected in the ui, in code the user publishes and subscribes accordingly to streams.
These streams represent individual channels of messages, such as a DM, perhaps a channel in a server, etc.
This way, broadcasting messages to all websocket connections becomes as simple as publishing that said message to that stream.

The main implementation of this is that individual clients aren't left processing tons of messages in unrelated channels
they aren't "subscribed" to (any channels of servers per say, or dms) that they are not included in.

### Server architecture

In code, the websocket server is started up, and then when the user connects to the server, the initial message of data
consists of auth credentials. If the initial message checks out, the server will run the handler on the client's websocket.

Handlers will handle anything networking-wise for the client, whether they subscribe to certain streams,
send any relevant data to the client, and then also receive and respond with any data related to the client.
This would simply include sending and receiving messages to the client, as well as managing that client's state in code and in the database.
Handlers are split up as a multitude of functions available in the server-side code. 

Every single client connection will be run on its individual thread; just about everything is programmed to be asynchronous. 

### Circles

"Circle" objects represent individual mini servers that can be privately or publicly made by clients in order to interact
with other clients. Circles will essentially represent collections of streams, a state concerning the storing of user data
individualized to that circle, and any other data concerning that circle.

### Storing and Managing Data

Every single object instantiated in code, when relevant, will have an equivalent schema represented in mongoDB.
This would include user data, logs of messages of every stream, etc. Objects will, accordingly, seamlessly integrate
mongoDB in order to serialize any relevant data, to what needs to be stored in the database.

## Other

### OLD SECTION for decentralized networking solution
**Utilizing Flask**

All in all, this backend just amounts to a simple REST API - it's just HTTP+Json.
While not the fastest nor most efficient method (in comparison to sockets, websockets, etc) it acts as an easy platform
to implement any plans for awesome, powerful systems.

Sessions are saved server-side using Flask-Sessions, and the majority of requests will be GET or PUT.

TODO: documenting the API. LINK:

### Database Solution
All user data is saved on MongoDB. A record of all messages in all rooms is also saved on MongoDB (for now).

TODO:
Basic session creation and handling
Sending messages
Basic UI Implementation
Implement MongoDB
sessions, auth
GET and PUT definitions for messaging


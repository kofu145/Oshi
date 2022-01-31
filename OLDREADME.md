# Oshi
A chat application utilizing HTTP requests to craft a networking protocol.
Currently, various ones are being developed and tested.

The front-end is based on the Kivy framework, while the API is developed using Flask.

### Networking Backend
**Utilizing Flask**

All in all, the backend just amounts to a simple REST API - it's just HTTP+Json.
While not the fastest nor most efficient method (in comparison to sockets, websockets, etc) it acts as an easy platform
to implement any plans for awesome, powerful systems.

Sessions are saved server-side using Flask-Sessions, and the majority of requests will be GET or PUT.

TODO: documenting the API. LINK:

All user data is saved on MongoDB. A record of all messages in all rooms is also saved on MongoDB (for now).

TODO: Implement MongoDB
sessions, auth
GET and PUT definitions for messaging


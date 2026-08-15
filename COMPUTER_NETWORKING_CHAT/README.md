# Simple Chat Application Using Sockets

A simple real-time chat application developed using Python socket programming. The project follows a client-server architecture where one computer works as the server and multiple computers can connect as clients through the same local network.

The application uses the `socket` module for network communication and the `threading` module to handle multiple clients simultaneously. Users enter a nickname and can exchange messages in real time. The server receives messages from clients and broadcasts them to the connected users.

## Technologies Used

* Python 3.x
* Socket Programming
* Threading
* TCP/IP
* VS Code
* Windows

## Files

* `server.py` – Handles client connections and broadcasts messages.
* `client.py` – Connects to the server and sends/receives chat messages.

## Features

* Real-time group chat
* Multiple client support
* Nickname-based identification
* Client-server communication
* Works over a local Wi-Fi/LAN network
* Handles client disconnections

## Learning Outcome

This project helped in understanding socket programming, client-server architecture, IP addresses, ports, TCP/IP communication, and multi-threaded networking.

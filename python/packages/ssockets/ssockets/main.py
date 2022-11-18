from socket import socket, AF_INET, SOCK_STREAM

def main():
    ip = "127.0.0.1"
    port = 1234

    s = socket(AF_INET, SOCK_STREAM)
    s.bind((ip, port))
    s.listen(5)

    print(f"Listening on {ip}:{port} 🎧")

    while True:
        client_socket, address = s.accept()
        print(f"Connection from {address} has been established.")
        client_socket.send(bytes("Welcome!", "utf-8")) # Send data to client socket

if __name__ == "__main__":
    exit(main())

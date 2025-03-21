import socket

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 8000))

    print("server running")
    while True:
        try:
            data,address = server_socket.recvfrom(1024)

            print(data.decode())
            server_socket.sendto("yep hello there".encode(), address)
        except e as exception:
            print(e)
            break

    server_socket.close()

server()
import socket,time

socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    time.sleep(.000001)
    try:
        socketClient.sendto("hi".encode(),('0.0.0.0',8000))
        data, recvr = socketClient.recvfrom(1024)
        print(data.decode())
    except e as exception:
        pass

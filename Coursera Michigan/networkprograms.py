import socket
import time
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()


host = input('Enter the website link: ')
port = 80
mysocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
mysocket.connect((host , port))
mysocket.sendall(b'GET http://data.pr4e.org/cover.jpg HTTP/1.0\n\n')
count = 0 
picture = b''
while True :
    data = mysocket.recv(5120)
    if (len(data) < 1) :
        break 
    time.sleep(0.25)
    count = count + len(data)
    picture = picture + data
    print(count)
mysocket.close()

pos = picture.find(b'\r\n\r\n')
print(pos)
print(picture[: pos].decode())
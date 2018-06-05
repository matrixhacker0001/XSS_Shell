import socket

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 9999))
    print("Listening on port: 9999")
    s.listen(1)

    while True:
        conn, addr = s.accept()
        print(conn.recv(1024))
        cmd = input("Enter >")
        cmd = cmd + "\nlocation.reload()"
        conn.send(str.encode(cmd))
        conn.close()
        s.close()
        connect()

connect()

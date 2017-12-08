import sys
import socket


# 1. get the socket descriptor --->socket.socket(##)
# 2. bind the socket to your ip address and a port (i think you can't pick port numbers less than 1024)
# 3. bind is basically reserving that particular port on your system for this program,
#      and no other program can use it while this program is running
# 4. start listening, --->app.listen in main()
# 5. start accepting connections --->app.accept()
# 6. now you have two things -conn, -addr
# 7. conn is used to communicate with the client (it's a socket object)
# 8. addr is a tuple with IP at index 0, port at index 1


host = '127.0.0.1'
port = 8800


def handle_exception(msg, e):
    print(msg, e)
    sys.exit(1)


class Connection():
    def __init__(self):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Socket Created...')
        try:
            self.socket.bind((host, port))
        except socket.error as e:
            handle_exception('Socket Bind Failed', e)
        print('Binding succesful...')

    def socket_desc(self):
        return self.socket


# NOTE: conn here is the socket object which can be used to communicate with the client
def main():
    app = Connection().socket_desc()
    app.listen(10)
    conn, addr = app.accept()
    # print('conn', conn)
    print('client connected - IP:', addr[0], 'PORT:', port)
    data = conn.recv(1024)
    while data.decode('utf-8') == 'close':
        print('client', data.decode('utf-8'))
        conn.sendall((input('msg: ').encode('utf-8')))


if __name__ == '__main__':
    main()
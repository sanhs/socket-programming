import sys
import socket

# Socket client example

host = "www.google.com"
port = 80
# NOTE: below msg is command to get their main page
send_message = "GET / HTTP/1.1\r\n\r\n"


def handle_exception(msg, e):
    print(msg, e)
    sys.exit(1)


class ClientSocket():
    def __init__(self):
        super().__init__()
        # NOTE: AF_INET - ipv4 ; SOCK_STREAM - TCP protocol
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as e:
            handle_exception('Could not create client Socket\n', e)
        print('client socket created...')

        print('trying', host + '...')
        # NOTE: get ip address of host
        try:
            remote_ip = socket.gethostbyname(host)
        except socket.gaierror as e:
            handle_exception('Could not resolve host\n', e)
        print('Google:', remote_ip)

        # NOTE: connect to remote host
        try:
            self.socket.connect((remote_ip, port))
        except Exception as e:
            handle_exception('', e)
        print('[+]Connection Successful')

        # NOTE: send msg to host
        try:
            self.socket.sendall(send_message.encode('utf-8'))
        except Exception as e:
            handle_exception('Could not send request\n', e)
        print('Request Sent successfully')

        reply = self.socket.recv(4096)
        reply = reply.decode('utf-8')
        print(reply)
        self.socket.close()
        print('Socket Closed\nExiting')
        sys.exit()


def main():
    client = ClientSocket()


if __name__ == '__main__':
    main()


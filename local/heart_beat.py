#!/usr/bin/env python3
import socket
import sys
import time


# First configure
try:
    HOST = ''    # Your remote server IP, the type is string
    PORT =     # Your remote server port, the type is int
except:
    print('Configure Value Error')


def heart_beat():
    count = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        port = int(PORT)
    except ValueError:
        port = socket.getservbyname(PORT, 'udp')
    s.connect((HOST, port))
    s.settimeout(5)

    while True:
        try:
            s.sendall(b'#Hi')
            count += 1
            print('Send a heart beat', count)
            time.sleep(10)    # Set your heart beat delay
        except KeyboardInterrupt:
            sys.exit(1)
        except Exception:
            continue


if __name__ == '__main__':
    print('Start heart beat...')
    heart_beat()

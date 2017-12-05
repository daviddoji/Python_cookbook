#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 22:17:16 2017

@author: david
"""

from socket import socket, AF_INET, SOCK_STREAM
from functools import partial

"""
You want to make your objects support the context-management protocol
(the with statement).
"""


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None


c = LazyConnection(('www.python.org', 80))
# Connection closed
with c as s:
    # c.__enter__() executes: connection open
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    # c.__exit__() executes: connection closed

print('Got %d bytes' % len(resp))
print()


class LazyConnection2:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.connections.pop().close()


conn = LazyConnection2(('www.python.org', 80))
with conn as s:
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))

print('Got %d bytes' % len(resp))

with conn as s1, conn as s2:
    s1.send(b'GET /downloads HTTP/1.0\r\n')
    s2.send(b'GET /index.html HTTP/1.0\r\n')
    s1.send(b'Host: www.python.org\r\n')
    s2.send(b'Host: www.python.org\r\n')
    s1.send(b'\r\n')
    s2.send(b'\r\n')
    resp1 = b''.join(iter(partial(s1.recv, 8192), b''))
    resp2 = b''.join(iter(partial(s2.recv, 8192), b''))

print('resp1 got %d bytes' % len(resp1))
print('resp2 got %d bytes' % len(resp2))

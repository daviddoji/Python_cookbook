#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 19:32:04 2017

@author: david
"""
import os
import sys
from socket import socket, AF_INET, SOCK_STREAM

"""
Problem
-------
You have an integer file descriptor correponding to an already open I/O
channel on the operating system (e.g., file, pipe, socket, etc.), and you
want to wrap a higher-level Python file object around it.
"""

# Open a low-level file descriptor
fd = os.open('data/channel.txt', os.O_WRONLY | os.O_CREAT)
# Turn into a proper file
f = open(fd, 'wt')
f.write('hello world\n')
f.close()
# Create a file object, but don't close underlying fd when done
# f = open(fd, 'wt', closefd=False)

# Create a binary-mode file for stdout
#bstdout = open(sys.stdout.fileno(), 'wb', closefd=False)
#bstdout.write(b'Hello World\n')
#bstdout.flush()

def echo_client(client_sock, addr):
    print("Got connection from", addr)
    # Make text-mode file wrappers for socket reading/writing
    client_in = open(client_sock.fileno(), 'rt', encoding='latin-1',
                     closefd=False)
    client_out = open(client_sock.fileno(), 'wt', encoding='latin-1',
                      closefd=False)

    # Echo lines back to the client using file I/O
    for line in client_in:
        client_out.write(line)
        client_out.flush()
    client_sock.close()


def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)


print('Echo serving running on localhost:25000')
print(echo_server(('', 25000)))

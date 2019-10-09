# import Python's libraries
import socket
import time
from binascii import hexlify

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to all interfaces on some port
port = 1337
s.bind(("", port))

# listen for connections:
s.listen(0)

# accept a connecting client, addr is address of connecting client
c, addr = s.accept()

# set one and zero timings
ZERO = 0.025
ONE = 0.1

msg = "Some message message message message message message message message ..."
n = 0

# convert message to binary
covert = "secret" + "EOF"
covert_bin = ""
for i in covert:
    # convert each character to a full byte
    covert_bin += bin(int(hexlify(i.encode()), 16))[2:].zfill(8)

# send a message, one character at a time with a delay in between characters:
for i in msg:
    c.send(i.encode())
    if (covert_bin[n] == "0"):
        time.sleep(ZERO)
    else:
        time.sleep(ONE)
    n = (n + 1) % len(covert_bin)
c.send("EOF".encode())

# close the connection
c.close()

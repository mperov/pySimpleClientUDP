#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Perov Maxim <coder@frtk.ru>
#

import socket

UDP_IP = "192.168.1.10"
UDP_PORT = 5001
MESSAGE = "Lun"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
len = sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))

print("I've sent " + str(len) + " bytes:")
print(MESSAGE)

data = sock.recvfrom(1024)
print("I got: " + str(data))

sock.close()

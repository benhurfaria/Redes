#!/usr/bin/env python3
import socket

HOST = 'localhost'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen()
print("AGUARDANDO REQUISIÇÃO")
conn, ender = s.accept()

print("CONECTADO EM ", ender)

while True:
    data = conn.recv(1024)
    if not data:
        print("FECHANDO A CONEXÃO")
        conn.close()
        break
    conn.sendall(data)
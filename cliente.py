#!/usr/bin/env python3

# Importando a biblioteca socket
import socket

# define o endereço do servidor e a porta de comunicação
HOST = 'localhost'
PORT = 50000

# cria o objeto socket, especificando a família de protocolos e o tipo de socket (TCP no caso)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# realiza a conexão com o servidor, especificando o endereço e a porta
s.connect((HOST, PORT))

# envia a mensagem 'Hello' ao servidor, após converter a string em uma sequência de bytes (usando a codificação padrão do sistema)
s.sendall(str.encode('Hello'))

# aguarda uma resposta do servidor, recebendo até 1024 bytes
data = s.recv(1024)

# converte a sequência de bytes em uma string e a imprime na tela
print(data.decode())

# aguarda a entrada do usuário para encerrar o programa
input("Pressione Enter para sair...")

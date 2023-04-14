#!/usr/bin/env python3

# Importando a biblioteca socket
import socket

# Definindo o endereço IP e porta de conexão
HOST = 'localhost'
PORT = 50000

# Criando um objeto socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associando o objeto socket ao endereço e porta
s.bind((HOST,PORT))

# Aguardando conexões na porta especificada
s.listen()

# Aguardando a conexão do cliente
print('Aguardando conexão de um cliente')
conn, ender = s.accept()  # A função s.accept() espera até que um cliente se conecte ao servidor
                          #e retorna uma tupla (socket, address), onde socket é um objeto de
                          #soquete conectado ao cliente e address é o endereço do cliente.

# Conexão estabelecida
print('Conectado em', ender)

# Loop para receber e enviar mensagens
while True:
    # Recebe a mensagem enviada pelo cliente
    data = conn.recv(1024) # usado para receber dados de um socket e retorna os
                           # dados recebidos como uma sequência de bytes.
                           # A sequência de bytes pode ser interpretada de diferentes
                           # formas, dependendo do contexto em que é utilizada. Por exemplo,
                           # uma sequência de bytes pode ser interpretada como um número
                           # inteiro, um caractere, uma imagem, um arquivo de áudio, etc.
    # Caso a mensagem seja vazia, encerra a conexão
    if not data:
        print('Fechando a conexão')
        conn.close()
        break
    # Imprime a mensagem recebida
    print(data.decode()) # data.decode() é uma operação que converte uma sequência de bytes (bytes object) em uma string (string object).
    # Envia uma mensagem de resposta ao cliente
    conn.sendall(str.encode('World')) # é um método que converte uma string em uma sequência de bytes usando uma codificação específica.
                                      # No caso desse código, a string 'Word' está sendo codificada em bytes usando a codificação padrão do sistema operacional. 

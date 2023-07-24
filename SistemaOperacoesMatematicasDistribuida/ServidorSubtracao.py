import socket

HOST = 'localhost'
PORTA = 60001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORTA))  # Vincula o servidor de subtração a um endereço e porta específicos.
s.listen(5)  # Inicia a escuta do servidor de subtração por novas conexões.

print("Servidor de Subtração iniciado. Aguardando conexão de um cliente...")

while True:
    conn, endereco = s.accept()  # Aceita a conexão de um novo cliente.
    print("Conectado ao Servidor de Subtração em:", endereco)  # Exibe o endereço do cliente recém-conectado.

    while True:
        mensagem = conn.recv(2048).decode()  # Recebe a mensagem do cliente e a decodifica.

        if mensagem.lower() == 'sair':
            conn.close()  # Fecha a conexão com o cliente.
            print("Cliente desconectado do Servidor de Subtração:", endereco)  # Exibe o endereço do cliente que foi desconectado.
            break

        operandos = mensagem.split(',')[1:]  # Separa os operandos da mensagem.
        resultado = int(operandos[0]) - sum(int(op) for op in operandos[1:])  # Realiza a operação de subtração com os operandos.
        conn.send(str(resultado).encode())  # Envia o resultado da subtração de volta para o cliente.
        break  # Encerra o loop de tratamento de mensagens (considerando que a mensagem enviada pelo cliente contém apenas a operação de subtração).

# Nota: O servidor de subtração também lida com apenas uma única mensagem de cada cliente antes de encerrar a conexão com ele.
# Se fosse desejado que o servidor de subtração continuasse recebendo mais mensagens do mesmo cliente, seria necessário ajustar a lógica do loop aqui.

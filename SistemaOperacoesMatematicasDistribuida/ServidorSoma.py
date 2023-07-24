import socket

HOST = 'localhost'  # Endereço IP do servidor.
PORTA = 60000  # Número da porta que o servidor utilizará para aceitar conexões.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Criação do socket.
s.bind((HOST, PORTA))  # Vincula o servidor ao endereço e porta especificados.
s.listen(5)  # Define o número máximo de conexões em espera.

print("Servidor de Soma iniciado. Aguardando conexão de um cliente...")

while True:
    conn, endereco = s.accept()  # Aceita a conexão do cliente e obtém o endereço do cliente.
    print("Conectado ao Servidor de Soma em:", endereco)

    while True:
        mensagem = conn.recv(2048).decode()  # Recebe a mensagem do servidor distribuido e a decodifica de bytes para string.

        if mensagem.lower() == 'sair':
            conn.close()  # Fecha a conexão com o cliente.
            print("Cliente desconectado do Servidor de Soma:", endereco)
            break

        operandos = mensagem.split(',')[1:]  # Separa os operandos da mensagem.
        resultado = sum(int(op) for op in operandos)  # Realiza a operação de soma.

        conn.send(str(resultado).encode())  # Envia o resultado da soma de volta para o servidor distribuido.
        break  # Encerra a comunicação após enviar o resultado.

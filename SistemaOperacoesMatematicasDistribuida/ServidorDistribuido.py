import socket
import threading

clientes = []  # Lista que armazenará os clientes conectados.

print("Aguardando conexão de clientes...")

# Função para adicionar um novo cliente em uma thread separada.
def novo_cliente():
    while True:
        cliente, endereco = server.accept()  # Aceita a conexão de um novo cliente.
        clientes.append(cliente)  # Adiciona o cliente à lista de clientes conectados.
        print(f"Cliente conectado: {endereco}")  # Exibe o endereço do cliente recém-conectado.
        threading.Thread(target=troca_mensagem, args=(cliente, endereco)).start()  # Inicia uma nova thread para lidar com as mensagens desse cliente.

def troca_mensagem(cliente, endereco):
    while True:
        mensagem_decodificada = cliente.recv(2048).decode()  # Recebe a mensagem do cliente e a decodifica.
        if mensagem_decodificada.lower() == 'sair':
            cliente.send('Desconectando...'.encode())  # Envia uma mensagem de confirmação de desconexão para o cliente.
            cliente.close()  # Fecha a conexão com o cliente.
            clientes.remove(cliente)  # Remove o cliente da lista de clientes conectados.
            print("Cliente desconectado:", endereco)  # Exibe o endereço do cliente que foi desconectado.
            break
        elif mensagem_decodificada.split(',')[0] == '+':
            # Se a operação for adição, chama a função para enviar a mensagem para o servidor de soma.
            servidor_adicao(cliente, mensagem_decodificada)
        elif mensagem_decodificada.split(',')[0] == '-':
            # Se a operação for subtração, chama a função para enviar a mensagem para o servidor de subtração.
            servidor_subtracao(cliente, mensagem_decodificada)
        else:
            cliente.send('Entrada não reconhecida.'.encode())  # Envia uma mensagem de erro para o cliente caso a operação seja inválida.

def servidor_adicao(cliente, msg):
    HOST = 'localhost'
    PORTA = 60000
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORTA))  # Conecta-se ao servidor de soma.
    client.send(msg.encode())  # Envia a mensagem de operação e valores para o servidor de soma.
    mensagem_recebida = client.recv(2048).decode()  # Recebe o resultado da operação do servidor de soma.
    cliente.send(mensagem_recebida.encode())  # Envia o resultado da operação de volta para o cliente.
    client.close()  # Fecha a conexão com o servidor de soma.

def servidor_subtracao(cliente, msg):
    HOST = 'localhost'
    PORTA = 60001
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORTA))  # Conecta-se ao servidor de subtração.
    client.send(msg.encode())  # Envia a mensagem de operação e valores para o servidor de subtração.
    mensagem_recebida = client.recv(2048).decode()  # Recebe o resultado da operação do servidor de subtração.
    cliente.send(mensagem_recebida.encode())  # Envia o resultado da operação de volta para o cliente.
    client.close()  # Fecha a conexão com o servidor de subtração.

if __name__ == '__main__':
    HOST = 'localhost'
    PORTA = 50000
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORTA))  # Vincula o servidor a um endereço e porta específicos.
    server.listen(5)  # Inicia a escuta do servidor por novas conexões.
    threading.Thread(target=novo_cliente).start()  # Inicia uma nova thread para aceitar conexões de clientes.

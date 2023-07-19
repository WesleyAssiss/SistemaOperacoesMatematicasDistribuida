import socket
import threading

clientes = []
temp = ''

print("Aguardando conexão de um cliente")


def novo_cliente():
    while True:
        cliente, endereco = server.accept()
        clientes.append(cliente)
        print("Conectado em:", endereco)
        threading.Thread(target=troca_mensagem, args=(cliente, endereco)).start()


def troca_mensagem(cliente, endereco):
    while True:
        mensagem_decodificada = cliente.recv(2048).decode()
        if mensagem_decodificada.lower() == 'sair':
            cliente.send('Desconectando...'.encode())
            cliente.close()
            clientes.remove(cliente)
            print("Cliente desconectado:", endereco)
            break
        elif mensagem_decodificada.split(',')[0] == '+':
            cliente.send(servidor_adicao(mensagem_decodificada).encode())
        elif mensagem_decodificada.split(',')[0] == '-':
            cliente.send(servidor_subtracao(mensagem_decodificada).encode())
        else:
            cliente.send('Entrada não reconhecida.'.encode())


def servidor_adicao(msg):
    HOST = 'localhost'
    PORTA = 60000
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORTA))
    client.send(msg.encode())
    return client.recv(2048).decode()


def servidor_subtracao(msg):
    HOST = 'localhost'
    PORTA = 60001
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORTA))
    client.send(msg.encode())
    return client.recv(2048).decode()


if __name__ == '__main__':
    HOST = 'localhost'
    PORTA = 50000
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORTA))
    server.listen(5)
    print("Servidor iniciado. Aguardando conexão de clientes...")
    threading.Thread(target=novo_cliente).start()

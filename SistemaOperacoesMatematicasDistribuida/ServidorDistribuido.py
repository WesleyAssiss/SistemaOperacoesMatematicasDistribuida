import socket
import threading

clientes = []  # Lista que armazenará os clientes conectados.

print("Aguardando conexão de clientes...")

# Função para adicionar um novo cliente em uma thread separada.
def novo_cliente():
    while True:
        cliente, endereco = server.accept()  # Aceita a conexão do cliente.
        clientes.append(cliente)  # Adiciona o cliente à lista de clientes conectados.
        print(f"Cliente conectado: {endereco}")
        threading.Thread(target=troca_mensagem, args=(cliente, endereco)).start()  # Cria uma thread para cada cliente conectado.

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

            resultado = servidor_soma(mensagem_decodificada)
            cliente.send(resultado.encode())


        elif mensagem_decodificada.split(',')[0] == '-':

            resultado = servidor_subtracao(mensagem_decodificada)
            cliente.send(resultado.encode())
        else:
            cliente.send('Entrada não reconhecida.'.encode())  # Envia mensagem de erro para o cliente.

# Função que envia a mensagem contendo a operação de adição para o ServidorSoma
def servidor_soma(msg):
    HOST = 'localhost'
    PORTA = 60000
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria o socket para comunicação com o ServidorSoma
    client.connect((HOST, PORTA))  # Conecta ao ServidorSoma através do endereço e porta especificados
    client.send(msg.encode())  # Envia a mensagem codificada para o ServidorSoma
    mensagem_recebida = client.recv(2048).decode()  # Recebe a resposta do ServidorSoma e decodifica a mensagem
    client.close()  # Fecha a conexão com o ServidorSoma
    return mensagem_recebida  # Retorna o resultado da operação de adição.

# Função que envia a mensagem contendo a operação de subtração para o ServidorSubtracao
def servidor_subtracao(msg):
    HOST = 'localhost'
    PORTA = 60001
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria o socket para comunicação com o ServidorSubtracao
    client.connect((HOST, PORTA))  # Conecta ao ServidorSubtracao através do endereço e porta especificados
    client.send(msg.encode())  # Envia a mensagem codificada para o ServidorSubtracao
    mensagem_recebida = client.recv(2048).decode()  # Recebe a resposta do ServidorSubtracao e decodifica a mensagem
    client.close()  # Fecha a conexão com o ServidorSubtracao
    return mensagem_recebida  # Retorna o resultado da operação de subtração.

if __name__ == '__main__':
    HOST = 'localhost'
    PORTA = 50000
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria o socket para o ServidorDistribuido
    server.bind((HOST, PORTA))  # Vincula o servidor ao endereço e porta especificados
    server.listen(5)  # Define o número máximo de conexões em espera
    threading.Thread(target=novo_cliente).start()  # Inicia a thread para aceitar novos clientes e iniciar a função novo_cliente em uma thread separada.

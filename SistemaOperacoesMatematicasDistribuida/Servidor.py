import socket  # Importa o módulo socket para trabalhar com comunicação em rede.
import threading  # Importa o módulo threading para trabalhar com threads (concorrência).

clientes = []  # Lista que armazenará os clientes conectados.
temp = ''  # Variável temporária.

print("Aguardando conexão de um cliente")  # Exibe uma mensagem informando que o servidor está aguardando conexões.

# Função para adicionar um novo cliente em uma thread separada.
def novo_cliente():
    while True:  # Loop infinito para sempre aguardar novas conexões.
        cliente, endereco = server.accept()  # Aceita a conexão do cliente e obtém o endereço do cliente.
        clientes.append(cliente)  # Adiciona o cliente à lista de clientes conectados.
        print("Conectado em:", endereco)  # Exibe o endereço do cliente que se conectou.
        threading.Thread(target=troca_mensagem, args=(cliente, endereco)).start()
        # Inicia uma nova thread para lidar com a troca de mensagens com o cliente conectado.

# Função para troca de mensagens com o cliente.
def troca_mensagem(cliente, endereco):
    while True:  # Loop infinito para sempre aguardar por mensagens do cliente.
        mensagem_decodificada = cliente.recv(2048).decode()  # Recebe a mensagem decodificada do cliente.
        if mensagem_decodificada.lower() == 'sair':  # Verifica se o cliente deseja desconectar.
            cliente.send('Desconectando...'.encode())  # Envia mensagem de desconexão para o cliente.
            cliente.close()  # Fecha a conexão com o cliente.
            clientes.remove(cliente)  # Remove o cliente da lista de clientes conectados.
            print("Cliente desconectado:", endereco)  # Exibe uma mensagem informando a desconexão do cliente.
            break  # Sai do loop, encerrando a comunicação com esse cliente.
        elif mensagem_decodificada.split(',')[0] == '+':  # Verifica se a mensagem é uma operação de adição.
            cliente.send(servidor_adicao(mensagem_decodificada).encode())  # Envia resultado da adição para o cliente.
        elif mensagem_decodificada.split(',')[0] == '-':  # Verifica se a mensagem é uma operação de subtração.
            cliente.send(servidor_subtracao(mensagem_decodificada).encode())  # Envia resultado da subtração.
        else:  # Se a mensagem não corresponder a nenhuma operação válida.
            cliente.send('Entrada não reconhecida.'.encode())  # Envia mensagem de erro para o cliente.

# Função para realizar a operação de adição no servidor.
def servidor_adicao(msg):
    HOST = 'localhost'  # Endereço do servidor local para a operação de adição.
    PORTA = 60000  # Porta do servidor para a operação de adição.
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria um novo socket TCP/IP.
    client.connect((HOST, PORTA))  # Conecta ao servidor local de adição.
    client.send(msg.encode())  # Envia a mensagem para o servidor de adição.
    return client.recv(2048).decode()  # Recebe e retorna a resposta do servidor de adição.

# Função para realizar a operação de subtração no servidor.
def servidor_subtracao(msg):
    HOST = 'localhost'  # Endereço do servidor local para a operação de subtração.
    PORTA = 60001  # Porta do servidor para a operação de subtração.
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria um novo socket TCP/IP.
    client.connect((HOST, PORTA))  # Conecta ao servidor local de subtração.
    client.send(msg.encode())  # Envia a mensagem para o servidor de subtração.
    return client.recv(2048).decode()  # Recebe e retorna a resposta do servidor de subtração.

if __name__ == '__main__':
    HOST = 'localhost'  # Define o endereço do servidor como localhost (máquina local).
    PORTA = 50000  # Define a porta do servidor como 50000.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria um novo socket TCP/IP.
    server.bind((HOST, PORTA))  # Associa o socket ao endereço e porta definidos.
    server.listen(5)  # Inicia o modo de escuta do servidor, permitindo até 5 conexões pendentes.
    print("Servidor iniciado. Aguardando conexão de clientes...")  # Exibe uma mensagem informando o início do servidor.
    threading.Thread(target=novo_cliente).start()
    # Inicia uma nova thread para aguardar conexões de clientes em paralelo com a execução principal.

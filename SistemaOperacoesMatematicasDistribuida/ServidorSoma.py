import socket  # Importa o módulo socket para trabalhar com comunicação em rede.

HOST = 'localhost'  # Define o endereço do servidor como localhost (máquina local).
PORTA = 60000  # Define a porta do servidor como 60000.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria um novo socket TCP/IP.
s.bind((HOST, PORTA))  # Associa o socket ao endereço e porta definidos.
s.listen(5)  # Inicia o modo de escuta do servidor, permitindo até 5 conexões pendentes.

print("Servidor de Soma iniciado. Aguardando conexão de um cliente...")  # Exibe uma mensagem informando o início do servidor.

while True:  # Loop infinito para sempre aguardar por novas conexões de clientes.
    conn, endereco = s.accept()  # Aceita a conexão do cliente e obtém o endereço do cliente.
    print("Conectado ao Servidor de Soma em:", endereco)  # Exibe o endereço do cliente que se conectou.

    while True:  # Loop infinito para receber múltiplas mensagens do cliente.
        mensagem = conn.recv(2048).decode()  # Recebe a mensagem decodificada enviada pelo cliente.

        if mensagem.lower() == 'sair':  # Verifica se o cliente enviou a mensagem 'sair' para desconectar.
            conn.close()  # Fecha a conexão com o cliente.
            print("Cliente desconectado do Servidor de Soma:", endereco)  # Exibe uma mensagem informando a desconexão.
            break  # Sai do loop interno, encerrando a comunicação com esse cliente.

        operandos = mensagem.split(',')[1:]  # Separa os operandos da mensagem recebida, ignorando o primeiro elemento (que é a operação).
        resultado = sum(int(op) for op in operandos)  # Realiza a soma dos operandos convertidos para inteiros.
        conn.send(str(resultado).encode())  # Envia o resultado da soma de volta ao cliente em formato de string codificada em bytes.
        break  # Sai do loop interno após enviar o resultado.

import socket

HOST = 'localhost'
PORTA = 60001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORTA))
s.listen(5)

print("Servidor de Subtração iniciado. Aguardando conexão de um cliente...")

while True:
    conn, endereco = s.accept()
    print("Conectado ao Servidor de Subtração em:", endereco)

    while True:
        mensagem = conn.recv(2048).decode()

        if mensagem.lower() == 'sair':
            conn.close()
            print("Cliente desconectado do Servidor de Subtração:", endereco)
            break

        operandos = mensagem.split(',')[1:]
        resultado = int(operandos[0]) - sum(int(op) for op in operandos[1:])
        conn.send(str(resultado).encode())
        break

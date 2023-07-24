import socket

def get_input(msg):
    while True:
        try:
            entrada = input(msg)  # Exibe uma mensagem e aguarda a entrada do usuário.
            return entrada
        except KeyboardInterrupt:
            print("\nOperação cancelada.")
            return None

def terminal(client):
    while True:
        try:
            operacao = get_input('Informe a operação soma (+) ou subtração (-) ou "sair" para encerrar:\n')
            if operacao is None:
                continue

            if operacao.lower() == 'sair':
                client.send(operacao.encode())  # Envia a mensagem de sair para o servidor.
                print(client.recv(2048).decode())  # Recebe e exibe a mensagem de confirmação do servidor.
                break  # Encerra o loop de envio de mensagens.

            if operacao not in ('+', '-'):
                print('Operação inválida. Use "+" para soma e "-" para subtração.')
                continue

            primeiro_valor = get_input('Digite o primeiro valor: ')
            if primeiro_valor is None:
                continue

            segundo_valor = get_input('Digite o segundo valor: ')
            if segundo_valor is None:
                continue

            entrada = f"{operacao},{primeiro_valor},{segundo_valor}"  # Cria a mensagem a ser enviada ao servidor.
            client.send(entrada.encode())  # Envia a mensagem ao servidor.
            print(client.recv(2048).decode())  # Recebe e exibe o resultado enviado pelo servidor.
        except:
            print('Erro ao publicar mensagem.')

if __name__ == '__main__':
    HOST = 'localhost'
    PORTA = 50000
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria o socket do cliente.
    client.connect((HOST, PORTA))  # Conecta-se ao servidor.
    terminal(client)  # Inicia a função de terminal para interação com o servidor.
    client.close()  # Fecha o socket de conexão com o servidor após encerrar a interação.

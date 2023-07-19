import socket


def get_input(msg):
    while True:
        try:
            entrada = input(msg)
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
                client.send(operacao.encode())
                print(client.recv(2048).decode())
                break

            if operacao not in ('+', '-'):
                print('Operação inválida. Use "+" para soma e "-" para subtração.')
                continue

            primeiro_valor = get_input('Digite o primeiro valor: ')
            if primeiro_valor is None:
                continue

            segundo_valor = get_input('Digite o segundo valor: ')
            if segundo_valor is None:
                continue

            entrada = f"{operacao},{primeiro_valor},{segundo_valor}"
            client.send(entrada.encode())
            print(client.recv(2048).decode())
        except:
            print('Erro ao publicar mensagem.')


if __name__ == '__main__':
    HOST = 'localhost'
    PORTA = 50000
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORTA))
    terminal(client)
    client.close()

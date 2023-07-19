import socket  # Importa o módulo socket para trabalhar com comunicação em rede.

# Função para obter entrada do usuário com tratamento de exceção para KeyboardInterrupt
def get_input(msg):
    while True:
        try:
            entrada = input(msg)  # Solicita uma entrada do usuário com a mensagem 'msg'.
            return entrada  # Retorna a entrada do usuário.
        except KeyboardInterrupt:  # Captura a exceção caso o usuário pressione Ctrl+C (KeyboardInterrupt).
            print("\nOperação cancelada.")  # Exibe uma mensagem informando o cancelamento da operação.
            return None  # Retorna None para indicar que a operação foi cancelada.

# Função principal do terminal para interagir com o servidor
def terminal(client):
    while True:
        try:
            # Obter a operação desejada pelo usuário: soma, subtração ou sair
            operacao = get_input('Informe a operação soma (+) ou subtração (-) ou "sair" para encerrar:\n')
            if operacao is None:  # Verifica se a operação é None (cancelada pelo usuário).
                continue  # Retorna ao início do loop, solicitando novamente a operação.

            if operacao.lower() == 'sair':  # Verifica se a operação é 'sair' (opção para encerrar o programa).
                client.send(operacao.encode())  # Envia a operação para o servidor, convertendo-a em bytes.
                print(client.recv(2048).decode())  # Recebe a resposta do servidor e a imprime na tela.
                break  # Sai do loop, encerrando o programa.

            if operacao not in ('+', '-'):  # Verifica se a operação não é válida (não é soma nem subtração).
                print('Operação inválida. Use "+" para soma e "-" para subtração.')  # Exibe mensagem de erro.
                continue  # Retorna ao início do loop, solicitando novamente a operação.

            primeiro_valor = get_input('Digite o primeiro valor: ')  # Solicita o primeiro valor ao usuário.
            if primeiro_valor is None:  # Verifica se o primeiro valor é None (cancelado pelo usuário).
                continue  # Retorna ao início do loop, solicitando novamente o primeiro valor.

            segundo_valor = get_input('Digite o segundo valor: ')  # Solicita o segundo valor ao usuário.
            if segundo_valor is None:  # Verifica se o segundo valor é None (cancelado pelo usuário).
                continue  # Retorna ao início do loop, solicitando novamente o segundo valor.

            entrada = f"{operacao},{primeiro_valor},{segundo_valor}"  # Concatena a operação e os valores em uma string.
            client.send(entrada.encode())  # Envia a entrada para o servidor, convertendo-a em bytes.
            print(client.recv(2048).decode())  # Recebe a resposta do servidor e a imprime na tela.
        except:  # Captura qualquer exceção não especificada anteriormente.
            print('Erro ao publicar mensagem.')  # Exibe mensagem de erro genérica.

if __name__ == '__main__':
    HOST = 'localhost'  # Define o endereço do servidor como localhost (máquina local).
    PORTA = 50000  # Define a porta do servidor como 50000.
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria um novo socket TCP/IP.
    client.connect((HOST, PORTA))  # Conecta o cliente ao servidor no endereço e porta especificados.
    terminal(client)  # Chama a função terminal, passando o socket do cliente como argumento.
    client.close()  # Fecha a conexão do cliente com o servidor.

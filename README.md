Atividade de Rede de Computadores


Conforme ilustrado na Figura 1, você deverá desenvolver uma calculadora distribuída (também chamado de Sistema de Operações Matemáticas Distribuída). Esse sistema é composto por:
Cliente (Cliente 1 ou Cliente 2): permite a um usuário, através de uma interface de linha de comando (ou console/input), informar a operação e os dois valores. Solicita ao Servidor de Operações Distribuídas a execução da operação, e depois recebe o resultado dessa operação e imprime na tela do cliente;
Servidor de Operações Distribuídas: recebe solicitações de operações (soma ou subtração) de um Cliente (Cliente 1 ou Cliente 2), encaminha a operação ao Servidor de Operação (Soma ou subtração) de acordo com a operação específica solicitada pelo cliente. Recebe o resultado dessa operação do Servidor de Operação e responde ao Cliente;
Servidor de Operação (Soma ou Subtração): recebe solicitações de operações (soma ou subtração) de um Servidor de Operações Distribuídas, resolve a operação (soma ou subtração) e responde o resultado dessa operação para o Servidor de Operações Distribuídas.


Figura 1: Atores e comunicação entre eles.

Para iniciar o desenvolvimento desse sistema, considere algumas instruções iniciais:
Para facilitar o início do desenvolvimento, considere um cenário de apenas os atores “Cliente 2”, “Servidor de Operações Distribuídas” e “Servidor de Soma”. Após implementar esse cenário, implemente o cenário completo adicionando ao primeiro cenário os atores “Cliente 1” e “Servidor de Subtração”;
Para a implementação dos cenários, considere as seguintes instruções:
Replique o código Cliente.java para cada ator “Cliente”;
Cada ator “Cliente” tem que se conectar ao respectivo “Servidor”, conforme ilustrado na Figura 1 através de porta específica.
Replique os códigos Servidor.java e TrataCliente.java para cada ator “Servidor”;
Defina portas diferentes para cada “Servidor”;
Utilize as ideias da atividade prática 4 para trabalhar as strings (ex, função split, vetor de strings, etc).

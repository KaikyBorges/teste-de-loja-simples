🛍️ Loja HAMKEW — Simulador de Compras em Python

Este projeto é um simulador de loja em terminal, desenvolvido em Python, no qual o usuário pode comprar roupas, visualizar preços aleatórios, remover itens da sacola caso não tenha saldo suficiente e até participar de um mini-quiz para ganhar dinheiro.

O programa utiliza colorama para estilizar o texto no terminal e oferece uma experiência interativa dinâmica.

🛒 Sistema de Loja

Exibe 25 produtos aleatórios entre uma lista de mais de 40 opções.

Permite comprar um ou vários itens por vez.

Evita repetição de produtos já comprados.

Mostra lista de compras e total a pagar.

Impede compras acima do saldo do usuário.

Permite remover itens até que o valor total caiba no orçamento.

Calcula e exibe troco ou saldo zerado.

💰 Sistema de Ganho de Dinheiro

Se o usuário estiver sem saldo, pode responder perguntas de programação (futuro quiz).

Garante progressão do jogo.

Respostas corretas aumentam o saldo.

🧠 Tecnologias Utilizadas

Python 3

Colorama (para colorir o terminal)

Random

Time

OS

📦 Como Executar

Tenha Python 3 instalado.

Instale a biblioteca colorama, caso ainda não tenha:

pip install colorama

📂 Estrutura do Código

loja()
Exibe a loja, trata compras, remoção de itens e pagamento.

ganhar()
Inicia o processo de ganho de dinheiro caso o saldo esteja baixo.

Variáveis globais:

dinheiro = 200 (saldo inicial)

📝 Exemplo de Uso

Ao iniciar o programa, você verá:

A lista de produtos

Preços variados

Perguntas sobre quais itens deseja comprar

Mensagens coloridas indicando erros, confirmações e pagamentos

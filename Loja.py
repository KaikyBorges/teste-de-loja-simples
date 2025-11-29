import random
import time
import os
from colorama import Fore, init

init(strip=False, convert=False, autoreset=True)

dinheiro = 200


def loja():
    produtos_loja = {
        "camiseta": 49.90, "calça jeans": 119.90, "jaqueta": 199.90, "blusa": 79.90,
        "moletom": 149.90, "bermuda": 89.90, "shorts": 69.90, "camisa social": 99.90,
        "regata": 39.90, "vestido": 129.90, "saia": 89.90, "meia": 14.90,
        "tênis": 249.90, "sandália": 99.90, "chinelo": 29.90, "casaco": 179.90,
        "roupão": 109.90, "legging": 59.90, "top": 44.90, "boné": 34.90,
        "touca": 24.90, "cinto": 39.90, "luva": 19.90, "cachecol": 49.90,
        "pijama": 89.90, "camisola": 79.90, "sutiã": 59.90, "cueca": 24.90,
        "sapato": 199.90, "jaqueta jeans": 189.90, "camiseta polo": 69.90,
        "cropped": 54.90, "macacão": 139.90, "macaquinho": 119.90, "blazer": 159.90,
        "terno": 299.90, "colete": 89.90, "body": 49.90, "pantufa": 39.90,
        "meia-calça": 29.90, "calça social": 109.90, "botas": 229.90,
        "blusa de lã": 99.90, "anorak": 249.90, "gorro": 19.90,
        "mochila": 119.90, "bolsa": 149.90, "óculos de sol": 99.90
    }

    produtos_disponiveis = dict(random.sample(list(produtos_loja.items()), 25))
    os.system('clear')

    print(Fore.BLUE + "\nBem-vindo à loja da HAMKEW!\n" + Fore.RESET)
    time.sleep(1)
    print("Hoje temos os seguintes produtos disponíveis:\n")

    for produto, preco in produtos_disponiveis.items():
        time.sleep(0.2)
        print(f"{produto.title()}: R$ {preco:.2f}")

    produtos_vendidos = {}
    lista_compras = []

    while True:
        entrada = input(
            "\nDigite o(s) nome(s) do(s) produto(s) que deseja comprar (ou 'sair' para encerrar): ").strip().lower()

        if entrada == "sair":
            break

        itens_digitados = [item.strip() for item in entrada.replace(",", " ").split()]
        nenhum_valido = True

        for escolha in itens_digitados:
            if escolha in produtos_disponiveis:
                preco = produtos_disponiveis.pop(escolha)
                produtos_vendidos[escolha] = preco
                lista_compras.append(escolha)
                print(Fore.GREEN + f"{escolha.title()} adicionado à sua sacola!" + Fore.RESET)
                nenhum_valido = False
            else:
                print(Fore.RED + f"{escolha.title()} não está disponível ou já foi vendido." + Fore.RESET)

        if nenhum_valido:
            print(Fore.YELLOW + "Nenhum item válido foi adicionado. Tente novamente." + Fore.RESET)

    if not produtos_vendidos:
        print(Fore.YELLOW + "\nNenhum produto foi comprado. Volte sempre!" + Fore.RESET)
        return

    print("\nFinalizando compra...")
    time.sleep(1)
    print("\nProdutos comprados:")
    for item, preco in produtos_vendidos.items():
        print(f"- {item.title()}: R$ {preco:.2f}")

    total = sum(produtos_vendidos.values())
    print(Fore.CYAN + f"\nTotal a pagar: R$ {total:.2f}" + Fore.RESET)

    if dinheiro < total:
        while dinheiro < total and produtos_vendidos:
            print(
                Fore.RED + f"\nSaldo insuficiente! Seu limite é R$ {dinheiro:.2f} e sua compra deu R$ {total:.2f}" + Fore.RESET)
            print("Itens na sacola:")
            for item, preco in produtos_vendidos.items():
                print(f"- {item.title()}: R$ {preco:.2f}")

            retirada = input(
                "\nDigite o nome do item que deseja remover (ou aperte Enter para cancelar a compra): ").strip().lower()

            if retirada == "":
                print(Fore.YELLOW + "Compra cancelada. Volte sempre!" + Fore.RESET)
                return

            if retirada in produtos_vendidos:
                produtos_vendidos.pop(retirada)
                total = sum(produtos_vendidos.values())
                print(Fore.GREEN + f"{retirada.title()} removido da sacola." + Fore.RESET)
            else:
                print(Fore.RED + "Item não encontrado na sacola." + Fore.RESET)

        if not produtos_vendidos:
            print(Fore.YELLOW + "Sua sacola está vazia. Compra encerrada." + Fore.RESET)
            return
        elif dinheiro == total:
            print(Fore.GREEN + "\nPagamento concluído com sucesso. Saldo zerado!" + Fore.RESET)
        else:
            troco = dinheiro - total
            print(Fore.GREEN + f"\nPagamento concluído! Seu troco é de R$ {troco:.2f}" + Fore.RESET)

    elif dinheiro == total:
        print(Fore.GREEN + "\nPagamento concluído com sucesso. Saldo zerado!" + Fore.RESET)
    else:
        troco = dinheiro - total
        print(Fore.GREEN + f"\nPagamento concluído! Seu troco é de R$ {troco:.2f}" + Fore.RESET)
        print("\nTenha um ótimo dia e obrigado por comprar na HAMKEW!")



def ganhar():
    global dinheiro
    os.system('clear')
    print(f"Pelo que parece você esta sem dinheiro não é ? Seu saldo é de {dinheiro} ")
    print("Para ganhar mais dinheiro, você deverá responde perguntas que irão desafiar seus conhecimentos na área da programação")
    pessoa = input("Deseja mesmo seguir ?")
    if pessoa.lower() == "sim":
        print("Então ", end = "")
        time.sleep(1)
        print("VAMOS ", end = "")
        time.sleep(1)
        print(Fore.RED+ "COMEÇAR"+Fore.RESET)
    else:
        print("Fique pobre então")
        time.sleep(2)
        exit()

ganhar()

from typing import List
from time import sleep
from models.cliente import Cliente
from models.conta import Conta


contas: List[Conta] = []
def main() -> None:
    menu()

def menu() -> None:
    print('####################################')
    print('############## BRASIL ##############')
    print('############# BANCOTEC #############')
    print('####################################')

    print('Selecione uma das opções: ')
    print('1 - Criar Conta')
    print('2 - Saque')
    print('3 - Depósito')
    print('4 - Transferência')
    print('5 - Listar Contas')
    print('6 - Sair do Sistema')

    opcao: int = int(input())

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transf()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Obrigado por utilizar nosso sistema. Volte sempre.')
        sleep(2)
        exit(0)
    else:
        print('Digite uma opção válida.')
        sleep(2)
        menu()


def criar_conta() -> None:
    print('Insira os dados: ')

    nome: str = input('Nome completo: ')
    email: str = input('E-mail: ')
    cpf: str = input('CPF: ')
    data_nasc: str = input('Data de Nascimento: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nasc)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Conta criada com sucesso!')
    print('Dados da conta: ')
    print()
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da conta: '))
        conta: Conta = buscar_conta_por_num(numero)

        if conta:
            valor: float = float(input('Insira o valor do saque: R$ '))
            conta.sacar(valor)
        else:
            print(f'Conta {numero} não existe.')
    else:
        print('Não há contas cadastradas.')
    sleep(2)
    menu()

def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Insira o número da conta: '))
        conta: Conta = buscar_conta_por_num(numero)

        if conta:
            valor: float = float(input('Informe o valor do depósito: R$ '))
            conta.depositar(valor)
        else:
            print(f'Conta {numero} não encontrada.')
    else:
        print('Não há contas cadastradas.')
    sleep(2)
    menu()

def efetuar_transf() -> None:
    if len(contas) > 0:
        numero_orig: int = int(input('Insira o número da conta: '))
        conta_orig: Conta = buscar_conta_por_num(numero_orig)

        if conta_orig:
            numero_dest: int = int(input('Conta destino: '))
            conta_dest: Conta = buscar_conta_por_num(numero_dest)

            if conta_dest:
                valor: float = float(input('Valor da transferência: R$ '))
                conta_orig.transferir(conta_dest, valor)
            else:
                print(f'Conta {numero_dest} não existe.')
        else:
            print(f'Conta {numero_orig} não encontrada.')
    else:
        print('Não há contas cadastradas.')
    sleep(2)
    menu()

def listar_contas() -> None:
    if len(contas) > 0:
        print('Listar Contas')
        for conta in contas:
            print(conta)
            print()
            sleep(1)
    else:
        print('Não há contas cadastradas.')
    sleep(2)
    menu()

def buscar_conta_por_num(numero: int) -> Conta:
    ct: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                ct = conta
    return ct

if __name__ == '__main__':
    main()

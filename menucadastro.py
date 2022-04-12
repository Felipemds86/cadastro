from time import sleep
from typing import List

from models.usuario import Usuario

usuario: List[Usuario] = []


def main() -> usuario:
    menu()


def menu() -> usuario:
    print('===================================')
    print('=========== Bem-vindo(a) ==========')
    print('===================================')

    print('Selecione uma opção abaixo: ')
    print('1 - Cadastrar usuario')
    print('2 - Listar usuario')
    print('3 - Sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_usuario()
    elif opcao == 2:
        listar_usuario()
    elif opcao == 3:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida!')
        sleep(1)
        menu()


def cadastrar_usuario();
    print('Cadastrar usuario')
    print('===================')

    nome: str = input('Informe o nome: ')
    nome: str = input('Informe o sobrenome:')
    cpf: float = float(input('Informe o seu cpf: '))
    idade: int = (input('Qual sua idade?'))
    Datanascimento: float = float(input('Qual sua data de nascimento: '))

    usuario: suario = usuario

    usuario.append(usuario)

    print(f'O produto {usuario.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()


def listar_usuario() -> usuario:
    if len(usuario) > 0:
        print('Listagem de usuario')
        print('--------------------')
        for produto in usuario:
            print(usuario)
            print('----------------')
            sleep(1)
    else:
        print('Ainda não existem usuario.')
    sleep(2)
    menu()

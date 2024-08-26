# importação
import os

# exibir menu
def exibir_menu():
    print('1 - Ler arquivo.')
    print('2 - Gravar novos dados no arquivo.')
    print('3 - Sair')

# função gravar novos dados
def gravar_arquivos(dados, nome, email, profissão):
    dados += f'\n\n{'-'*30}\n\nNome: {nome}\nE-mail: {email}\nProfissão: {profissão}'
    with open('arquivo.txt', 'w', encoding= 'utf-8') as arquivo: arquivo.write(dados)

# função de leita de arquivo
def ler_arquivo():
    with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
        dados = arquivo.read()
    return dados

# programa principal
if __name__ == '__main__':
    while True:
        dados = ler_arquivo()
        exibir_menu()
        opcao = input('Opção desejada: ')
        os.system('cls')
        match opcao:
            case '1':
                print(f'\n{dados}\n')
                continue
            case '2':
                print('NOVO CADASTRO:\n')
                novo_nome = input('Informe o nome de úsuario: ')
                nova_turma = input('Informe a nova turma: ')
                novo_numero = input('Informe o novo número: ')
                gravar_arquivos(dados, novo_nome, nova_turma, novo_numero)
                continue
            case '3':
                print('Saindo...')
                break
            case _:
                print('Opção inválida. Tente novamente.')
                continue
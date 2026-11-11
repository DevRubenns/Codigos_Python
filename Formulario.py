import requests
import json

menu = False
while menu != True:
    print(''
    '+-------------------------------+'
    '\n| Digite a opção desejada:      |'
    '\n| 1 - Cadastrar                 |'
    '\n| 2 - Buscar                    | '
    '\n| 3 - Sair                      |'
    '\n+-------------------------------+\n')
    operacao = int(input('Digite a opção desejada: '))

    if operacao == 1 or operacao == 2 or operacao == 3:
        menu = True
    else:
        print('\nOpção inválida\n')
        menu = False

    if operacao == 1:
        Nome = input('Digite seu nome: ')
        CPF = input('Digite seu CPF: ')
        Idade = int(input('Digite sua idade: '))
        CEP = input('Digite seu CEP: ')
        Lote = input('Digite seu Lote: ')
        Telefone = input('Digite seu telefone: ')
        Email = input('Digite seu email: ')

        dados = requests.get(f'https://viacep.com.br/ws/{CEP}/json/')
        dados_json = json.loads(dados.text)
        ENDERECO = dados_json['logradouro'] + ', ' + dados_json['bairro'] + ', ' + dados_json['localidade'] + ' - ' + dados_json['uf']

        # Abrindo o arquivo e escrevendo as informações nele
        with open(f'{CPF}.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write('\n --- Novo Cadastro ---\n')
            arquivo.write(f'Nome: {Nome}\n')
            arquivo.write(f'CPF: {CPF}\n')
            arquivo.write(f'Idade: {Idade}\n')
            arquivo.write(f'CEP: {CEP}\n')
            arquivo.write(f'Lote: {Lote}\n')
            arquivo.write(f'Endereco: {ENDERECO}\n')
            arquivo.write(f'Telefone: {Telefone}\n')
            arquivo.write(f'Email: {Email}\n')
            arquivo.write('----------------------\n\n')

        print(f'\nCadastro de {Nome} realizado e salvo com sucesso!\n')
        menu = False

    elif operacao == 2:
        validador_cpf = False
        while validador_cpf != True:
          print('Busca de Cadastros')
          vCpf = input('Digite o CPF: ')

          if CPF != vCpf:
            print('CPF não encontrado\n')
            validador_cpf = False
          else:
            validador_cpf = True
            try:
              with open(f'{vCpf}.txt', 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
            finally:
              menu = False
              validador_cpf = True
            print(conteudo)
            menu = False

    elif operacao == 3:
        print('\nSaindo do sistema...')
        menu = True
#
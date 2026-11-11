#laço de repetição para selecionar operações
opcao_valida = False
while opcao_valida != True:
    operacao = int(input(''
    '+-------------------------------------+'
    '\n| Digite qual Operação vai ser Feita: |'
    '\n| 1 - Soma                            |'
    '\n| 2 - Diminuir                        |'
    '\n| 3 - Multiplicar                     |'
    '\n| 4 - Dividir                         |'
    '\n| 0 - Sair                            |'
    '\n+-------------------------------------+\n'
    '\n'
    'Opção: '))


    print(f'\nOpção Selecionada: {operacao}\n')

    if operacao >= 0 and operacao <=4:
        opcao_valida = True
    else:
        opcao_valida = False
        print('Opção Invalida')

#Validar quando é divição com 0 / pegar numeros para calculo
valido = False
while valido != True:
    n1 = float(input('Digite o Primeiro Numero:'))
    n2 = float(input('Digite o Segundo Numero:'))

    if operacao == 3:
      if n1 == 0 or n2 == 0:
        print('Não é possivel dividir por 0')
        valido = False
    else:
      valido = True

#resultados calculos
if operacao == 1:
    print(f'\nO calculo de {n1} + {n2} é {n1+n2}')
elif operacao == 2:
    print(f'\nO calculo de {n1} - {n2} é {n1-n2}')
elif operacao == 3:
    print(f'\nO calculo de {n1} * {n2} é {n1*n2}')
elif operacao == 4:
    print(f'\nO calculo de {n1} / {n2} é {n1/n2}')
elif operacao == 0:
    print('Saindo..')
else:
    print('Opção Invalida')
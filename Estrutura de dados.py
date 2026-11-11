soma = 0
media = 0

notas = []
alunos = {"Nome":"","Media":"", "Turma":""}

menu = False
while menu != True:
    print('-'*20,''
    '\n1 - Cadastro'
    '\n2 - Consultar'
    '\n3 - Sair'
    '-'*20)

    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1 and opcao == 2 and opcao == 3:
        menu = True
    else:
        print('Opção inválida')

    #Opções Menu
    if opcao == 1:
        alunos["Nome"] = input(f"Digite o nome do {i}º aluno: ")
        alunos["Turma"] = input(f"Digite a turma do {i}º aluno: ")
        for i in range(0, 4):
            notas.append(float(input(f"Digite a nota do {i+1} bimeste: ")))

    elif opcao == 3:
        print('Saindo do sistema...')
        menu = True


import subprocess
import os

# Função para limpar o console/tela de forma multiplataforma (Windows/Linux/OSX)
def limpar():
    subprocess.call('clear' if os.name != 'nt' else 'cls', shell=True)

# Definição do total máximo de aulas que o curso possui (usado no cálculo de faltas e frequência)
total_aulas_curso = 40.0

# Banco de dados simulado em memória contendo a lista dos alunos cadastrados,
# agora utilizando 'FaltasAluno' para registrar as faltas de cada um.
dados_alunos = [
    {"NomeAluno": "bruno", "MatriculaAluno": "1234", "TurmaAluno": "53", "FaltasAluno": 5.0, "Nota1": 10.0, "Nota2": 10.0},
    {"NomeAluno": "joao", "MatriculaAluno": "5678", "TurmaAluno": "53", "FaltasAluno": 0.0, "Nota1": 2.0, "Nota2": 3.0},
    {"NomeAluno": "arthur", "MatriculaAluno": "9123", "TurmaAluno": "53", "FaltasAluno": 15.0, "Nota1": 8.0, "Nota2": 7.0},
    {"NomeAluno": "pedro", "MatriculaAluno": "4567", "TurmaAluno": "53", "FaltasAluno": 2.0, "Nota1": 6.0, "Nota2": 5.5},
    {"NomeAluno": "marcelo", "MatriculaAluno": "8912", "TurmaAluno": "53", "FaltasAluno": 1.0, "Nota1": 4.0, "Nota2": 5.0},
    {"NomeAluno": "joao pedro", "MatriculaAluno": "3456", "TurmaAluno": "53", "FaltasAluno": 10.0, "Nota1": 7.5, "Nota2": 8.0},
    {"NomeAluno": "rubenns", "MatriculaAluno": "7891", "TurmaAluno": "53", "FaltasAluno": 8.0, "Nota1": 9.0, "Nota2": 9.5},
    {"NomeAluno": "theneds", "MatriculaAluno": "2345", "TurmaAluno": "53", "FaltasAluno": 20.0, "Nota1": 3.0, "Nota2": 2.5}
]

# Função que calcula a média, a porcentagem de presença e define o status acadêmico do aluno
def calcular_status(nota1, nota2, faltas):
    # As presenças são deduzidas subtraindo as faltas registradas do total de aulas
    presencas = max(0.0, total_aulas_curso - faltas)
    # Calcula a proporção percentual de presença para avaliar se atinge o mínimo de 75%
    porcentagem_presenca = (presencas / total_aulas_curso) * 100

    # Se a presença for inferior a 75%, o aluno é reprovado direto por falta
    if porcentagem_presenca < 75.0:
        return (nota1 + nota2) / 2 if (nota1 is not None and nota2 is not None) else None, "Reprovado por Falta", porcentagem_presenca

    # Se as notas ainda não foram totalmente informadas
    if nota1 is None or nota2 is None:
        return None, "Sem Notas", porcentagem_presenca

    # Cálculo da média aritmética simples das notas
    media = (nota1 + nota2) / 2
    # Determinação do status baseado na média
    if media >= 7.0:
        status = "Aprovado"
    elif media >= 5.0:
        status = "Recuperação"
    else:
        status = "Reprovado"
    return media, status, porcentagem_presenca

# Função auxiliar para renderizar as informações completas de um aluno na tela
def exibir_aluno(aluno):
    nota1 = aluno.get("Nota1")
    nota2 = aluno.get("Nota2")
    faltas = aluno.get("FaltasAluno", 0.0)
    presencas = max(0.0, total_aulas_curso - faltas)
    media, status, pct_presenca = calcular_status(nota1, nota2, faltas)

    print(f'Nome: {aluno["NomeAluno"]} | Matrícula: {aluno["MatriculaAluno"]} | Turma: {aluno["TurmaAluno"]}')
    print(f'Faltas: {faltas} | Presenças: {presencas}/{total_aulas_curso} ({pct_presenca:.1f}% de Frequência)')
    if nota1 is not None and nota2 is not None:
        print(f'Nota 1: {nota1} | Nota 2: {nota2} | Média: {media:.1f} | Status Final: {status}')
    else:
        print(f'Notas: Não lançadas ainda | Status Final: {status}')
    print('-' * 60)

# Loop principal do Menu do Sistema
menu = False
while menu != True:
    limpar()
    print(f''
    '\n+---------------------------------+'
    f'\n| Total de Aulas do Curso: {int(total_aulas_curso)}  |'
    '\n| Digite a opção desejada:      |'
    '\n| 1 - Cadastrar Aluno           |'
    '\n| 2 - Buscar/Gerenciar Alunos   |'
    '\n| 3 - Relatórios por Turma      |'
    '\n| 4 - Definir Total de Aulas    |'
    '\n| 9 - Sair                      |'
    '\n+-------------------------------+\n')
    operacao = int(input('Digite a opção desejada: '))

    # Validação preliminar da escolha do menu principal
    if operacao in [1, 2, 3, 4, 9]:
        menu = True
    else:
        print('\nOpção inválida\n')
        input('Pressione Enter para continuar...')
        menu = False

    # BLOCO 1: Cadastro de novo aluno
    if operacao == 1:
        limpar()
        print('\nCadastro de Aluno!')

        # Validação de matrícula duplicada no cadastro de novos alunos
        while True:
            matricula = input('Digite a Matrícula do Aluno: ')
            matricula_existe = False
            for aluno in dados_alunos:
                if aluno["MatriculaAluno"] == matricula:
                    matricula_existe = True
                    break
            if not matricula_existe:
                break
            print('Erro: Já existe um aluno cadastrado com esta matrícula. Tente outra.')

        nome = input('Digite o Nome do Aluno: ')
        turma = input('Digite a Turma do Aluno: ')

        # O aluno é inicializado com 0 faltas e sem notas cadastradas
        dados_aluno = {
            "NomeAluno": nome,
            "MatriculaAluno": matricula,
            "TurmaAluno": turma,
            "FaltasAluno": 0.0,
            "Nota1": None,
            "Nota2": None
        }
        dados_alunos.append(dados_aluno)
        print(f'Aluno cadastrado com sucesso! Nome: {nome}')
        input('Pressione Enter para voltar ao menu...')
        menu = False

    # BLOCO 2: Submenu de Gerenciamento e Consultas de Alunos
    elif operacao == 2:
        menuConsulta = False
        while menuConsulta != True:
            limpar()
            print(''
            '\n+-------------------------------------+'
            '\n| Digite a opção desejada:            |'
            '\n| 1 - Mostrar todos os Alunos         |'
            '\n| 2 - Buscar Aluno por Nome           |'
            '\n| 3 - Buscar Aluno por Matricula      |'
            '\n| 4 - Excluir Aluno por Matricula     |'
            '\n| 5 - Lançar Notas de Aluno           |'
            '\n| 6 - Lançar Faltas de Aluno          |'
            '\n| 9 - Voltar                          |'
            '\n| 0 - Sair                            |'
            '\n+-------------------------------------+\n')
            operacaoConsulta = int(input('Digite a opção desejada: '))

            # Validação das opções internas de consulta
            if operacaoConsulta in [1, 2, 3, 4, 5, 6, 9]:
                if operacaoConsulta == 9:
                    menuConsulta = True
                    menu = False
                else:
                    menuConsulta = False
            else:
                print('\nOpção inválida\n')
                input('Pressione Enter para continuar...')
                menuConsulta = False

            # Exibe todos os alunos cadastrados
            if operacaoConsulta == 1:
                limpar()
                print('\n--- Lista de Todos os Alunos ---')
                for aluno in dados_alunos:
                    exibir_aluno(aluno)
                input('Pressione Enter para voltar...')

            # Busca e filtra os alunos por aproximação de nome
            elif operacaoConsulta == 2:
                limpar()
                buscar_nome = input('digite o nome do aluno: ')
                encontrou_aluno = False
                print('\n--- Resultado da Busca ---')
                for aluno in dados_alunos:
                    if buscar_nome.lower() in aluno['NomeAluno'].lower():
                        exibir_aluno(aluno)
                        encontrou_aluno = True
                if not encontrou_aluno:
                    print('Nenhum aluno encontrado com esse nome.')
                print('--------------------------')
                input('Pressione Enter para voltar...')

            # Busca exata de aluno por número de matrícula
            elif operacaoConsulta == 3:
                limpar()
                buscar_matricula = input('digite a matricula do aluno: ')
                encontrou_aluno = False
                print('\n--- Resultado da Busca ---')
                for aluno in dados_alunos:
                    if buscar_matricula in aluno['MatriculaAluno']:
                        exibir_aluno(aluno)
                        encontrou_aluno = True
                if not encontrou_aluno:
                    print('Nenhum aluno encontrado com essa matrícula.')
                print('--------------------------')
                input('Pressione Enter para voltar...')

            # Exclui o aluno correspondente à matrícula informada
            elif operacaoConsulta == 4:
                limpar()
                matricula_excluir = input('Digite a matrícula do aluno que deseja excluir: ')
                encontrou_aluno = False
                print('\n--- Processo de Exclusão ---')
                for aluno in dados_alunos:
                    if aluno['MatriculaAluno'] == matricula_excluir:
                        dados_alunos.remove(aluno)
                        print(f'Aluno de matrícula {matricula_excluir} ({aluno["NomeAluno"]}) foi excluído com sucesso!')
                        encontrou_aluno = True
                        break
                if not encontrou_aluno:
                    print('Nenhum aluno encontrado com essa matrícula para exclusão.')
                print('----------------------------')
                input('Pressione Enter para voltar...')

            # Lançamento de notas com validação de limite máximo (nota não pode passar de 10)
            elif operacaoConsulta == 5:
                limpar()
                matricula_notas = input('Digite a matrícula do aluno para lançar as notas: ')
                encontrou_aluno = False
                for aluno in dados_alunos:
                    if aluno['MatriculaAluno'] == matricula_notas:
                        print(f'Lançando notas para: {aluno["NomeAluno"]}')

                        # Validação para Nota 1 não passar de 10 ou ser negativa
                        while True:
                            n1 = float(input('Digite a Nota 1 (0 a 10): '))
                            if 0 <= n1 <= 10:
                                aluno['Nota1'] = n1
                                break
                            print('Erro: A nota não pode ser maior que 10 ou menor que 0.')

                        # Validação para Nota 2 não passar de 10 ou ser negativa
                        while True:
                            n2 = float(input('Digite a Nota 2 (0 a 10): '))
                            if 0 <= n2 <= 10:
                                aluno['Nota2'] = n2
                                break
                            print('Erro: A nota não pode ser maior que 10 ou menor que 0.')

                        print(f'Notas do Aluno {aluno["NomeAluno"]} foram inseridas com sucesso!')
                        encontrou_aluno = True
                        break
                if not encontrou_aluno:
                    print('Nenhum aluno encontrado com essa matrícula.')
                input('Pressione Enter para voltar...')

            # Lançamento individual de faltas (não pode exceder o limite do total de aulas)
            elif operacaoConsulta == 6:
                limpar()
                matricula_faltas = input('Digite a matrícula do aluno para lançar faltas: ')
                encontrou_aluno = False
                for aluno in dados_alunos:
                    if aluno['MatriculaAluno'] == matricula_faltas:
                        print(f'Lançando faltas para: {aluno["NomeAluno"]}')
                        while True:
                            faltas_lançadas = float(input(f'Digite a quantidade de Faltas (Max {int(total_aulas_curso)}): '))
                            if 0 <= faltas_lançadas <= total_aulas_curso:
                                aluno['FaltasAluno'] = faltas_lançadas
                                print(f'Faltas do Aluno {aluno["NomeAluno"]} atualizadas para {faltas_lançadas}!')
                                break
                            print(f'Erro: O número de faltas não pode passar do total de aulas ({int(total_aulas_curso)}) ou ser negativo.')
                        encontrou_aluno = True
                        break
                if not encontrou_aluno:
                    print('Nenhum aluno encontrado com essa matrícula.')
                input('Pressione Enter para voltar...')

            elif operacaoConsulta == 9:
                encontrou_aluno = True

            elif operacaoConsulta == 0:
                print("Saindo do sistema...")
                menu = True
                encontrou_aluno = True

    # BLOCO 3: Submenu para emissão de Relatórios Consolidados
    elif operacao == 3:
        menuRelatorio = False
        while menuRelatorio != True:
            limpar()
            print(''
            '\n+-------------------------------------+'
            '\n| Digite o Relatório desejado:        |'
            '\n| 1 - Média da Frequência por Turma   |'
            '\n| 2 - Média de Notas por Turma        |'
            '\n| 9 - Voltar                          |'
            '\n+-------------------------------------+\n')
            operacaoRelatorio = int(input('Digite a opção desejada: '))

            if operacaoRelatorio in [1, 2, 9]:
                if operacaoRelatorio == 9:
                    menuRelatorio = True
                    menu = False
                else:
                    menuRelatorio = False
            else:
                print('\nOpção inválida\n')
                input('Pressione Enter para continuar...')
                menuRelatorio = False

            # Relatório: Média de frequência/presença dos alunos de uma determinada turma
            if operacaoRelatorio == 1:
                limpar()
                media_frequencia = input('Digite a turma para ter a Média da Frequência: ')
                encontrou_aluno = False
                soma_frequencia = 0
                contador = 0
                for aluno in dados_alunos:
                    if aluno['TurmaAluno'] == media_frequencia:
                        faltas = aluno.get('FaltasAluno', 0.0)
                        presencas = max(0.0, total_aulas_curso - faltas)
                        soma_frequencia += presencas
                        contador += 1
                        encontrou_aluno = True
                if encontrou_aluno:
                    media = (soma_frequencia / contador)
                    media_porcentagem = (media / total_aulas_curso) * 100
                    print(f'\n--- Relatório de Frequência (Turma {media_frequencia}) ---')
                    print(f'Média de presenças da turma: {media:.1f} aulas de {int(total_aulas_curso)} ({media_porcentagem:.1f}%)')
                    print('------------------------------------------------')
                else:
                    print(f'Nenhum aluno encontrado na turma {media_frequencia}.')
                input('Pressione Enter para voltar...')

            # Relatório: Média aritmética das notas globais de uma turma específica
            elif operacaoRelatorio == 2:
                limpar()
                media_frequencia = input('Digite a turma para ter a Média de Notas: ')
                encontrou_aluno = False
                soma_notas = 0
                total_notas_lancadas = 0
                for aluno in dados_alunos:
                    if aluno['TurmaAluno'] == media_frequencia:
                        n1 = aluno.get('Nota1')
                        n2 = aluno.get('Nota2')
                        if n1 is not None and n2 is not None:
                            soma_notas += (n1 + n2) / 2
                            total_notas_lancadas += 1
                        encontrou_aluno = True
                if encontrou_aluno:
                    if total_notas_lancadas > 0:
                        media_geral = soma_notas / total_notas_lancadas
                        print(f'\n--- Relatório de Notas (Turma {media_frequencia}) ---')
                        print(f'Média das notas da turma: {media_geral:.2f} (baseado em {total_notas_lancadas} alunos com notas)')
                        print('-------------------------------------------')
                    else:
                        print(f'Alunos encontrados na turma {media_frequencia}, mas nenhum possui notas lançadas.')
                else:
                    print(f'Nenhum aluno encontrado na turma {media_frequencia}.')
                input('Pressione Enter para voltar...')

    # BLOCO 4: Permite redefinir dinamicamente a quantidade total de aulas do curso
    elif operacao == 4:
        limpar()
        total_aulas_curso = float(input('Digite a nova quantidade total de aulas do curso: '))
        print(f'Total de aulas atualizado para: {int(total_aulas_curso)}')
        input('Pressione Enter para voltar ao menu...')
        menu = False

    # Encerra o programa definindo o controle do loop principal como True
    elif operacao == 9:
        print("Saindo do sistema...")
        menu = True
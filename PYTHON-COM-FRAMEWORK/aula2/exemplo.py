# Lógica de programação:
# cadastrar o aluno
# cadastrar as notas do aluno
# trazer média
# trazer média da sala
# verificar qual a melhor média
# verificar qual a pior média
# verificar se o aluno passou ou não

dados_escola = {}

nome_1 = input('Digite o nome:')
nome_2 = input('Digite o nome:')
nome_3 = input('Digite o nome:')
nome_4 = input('Digite o nome:')

dados_escola['alunos'] = []
dados_escola['alunos'].extend([nome_1, nome_2, nome_3,nome_4])

nota_aluno_1 = [float(input('Nota1 : ')), float(input('Nota2 : ')), float(input('Nota3 : '))]
nota_aluno_2 = [float(input('Nota1 : ')), float(input('Nota2 : ')), float(input('Nota3 : '))]
nota_aluno_3 = [float(input('Nota1 : ')), float(input('Nota2 : ')), float(input('Nota3 : '))]
nota_aluno_4 = [float(input('Nota1 : ')), float(input('Nota2 : ')), float(input('Nota3 : '))]

dados_escola['notas'] = []
dados_escola['notas'].extend([nota_aluno_1, nota_aluno_2, nota_aluno_3, nota_aluno_4])

media_aluno_1 =  sum(dados_escola['notas'][0])/len(dados_escola['notas'][0])
media_aluno_2 = sum(dados_escola['notas'][1])/len(dados_escola['notas'][1])
media_aluno_3 =sum(dados_escola['notas'][2])/len(dados_escola['notas'][2])
media_aluno_4 = sum(dados_escola['notas'][3])/len(dados_escola['notas'][3])

print('Media aluno', dados_escola['alunos'].index(nome_1), media_aluno_1)
print('Media aluno', dados_escola['alunos'].index(nome_2), media_aluno_2)
print('Media aluno', dados_escola['alunos'].index(nome_3), media_aluno_3)
print('Media aluno', dados_escola['alunos'].index(nome_4), media_aluno_4)

dados_escola['media_sala'] = []
dados_escola['media_sala'].extend([media_aluno_1, media_aluno_2, media_aluno_3,media_aluno_4])

print('Medias da sala', dados_escola['media_sala'])

maior = max(dados_escola['media_sala'])
menor = min(dados_escola['media_sala'])
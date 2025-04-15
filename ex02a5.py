alunos= 0
qntalunos= int(input("difite a quantidade de alunos na turma"))
soma= 0
while alunos <qntalunos:
    notasalunos= int(input("digite as notas: "))
    soma += notasalunos
    alunos += 1
media = soma/alunos
print(f"a média aritmétrica da turma é: {media}")
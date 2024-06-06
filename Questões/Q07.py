aluno = input("Nome: ")
disciplina = input("Disciplina: ")
nota1 = int(input("Nota1: "))
nota2 = int(input("Nota2: "))
media = (nota1 + nota2) / 2 
if media >= 6: 
    print(f'{aluno} está aprovado em {disciplina}')
else: 
    print(f'{aluno} está reprovado em {disciplina}')

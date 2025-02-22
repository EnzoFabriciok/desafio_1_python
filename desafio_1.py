#Missão 1: Restaurando as Regras Escolares 📝 
#O vírus apagou os critérios de aprovação dos alunos! Para ajudar o Professor Byte a organizar o sistema, sua tarefa é criar um programa que verifique se um aluno foi aprovado (nota maior ou igual à 6) ou reprovado (nota menor ou igual à 5).

nota_aluno = float(input("Digite a nota do aluno"))

if nota_aluno >= 6:
    print('Aluno Aprovado!')
elif nota_aluno <= 5:
    print('Aluno Reprovado!')


# Missão 2: O Sistema Eleitoral Secreto 📝 
# O grêmio estudantil da escola realiza votações para decidir melhorias e inovações, mas o vírus desativou a verificação de elegibilidade para votar! Sua tarefa é criar um programa que pergunte a idade do usuário e informe se ele pode votar (mínimo: 16 anos).

idade = float(input("Qual sua idade?"))

if idade >= 16:
    print(f'Você PODE votar, Você tem {idade} anos.')
else:
    print(f'Você NÃO pode votar, Você tem {idade} anos.')
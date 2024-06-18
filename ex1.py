nome = input('digite o nome: ')     
nota1 = float(input('digite a nota 1: '))
nota2 = float(input('digite a nota 2: '))


media = (nota1 + nota2) / 2

print('nome: ', nome)
print('Média: ', media)

if media >=6:
    print('aprovado')
elif media >=4 <6:
    print('recuperação')
else:
    print('reprovado')


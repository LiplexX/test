sexo = input('digite seu sexo: ')
altura = float(input('digite sua altura: '))
peso = float(input('digite sua peso: '))

pesoIdeal = 0.0

if sexo.upper() == 'H': #lower
    pesoIdeal = (72.7*altura)-58

elif(sexo.upper() == 'M'):
    pesoIdeal = (62.1*altura)-44.7
else:
    print('O sexo informado deve ser H para Homem ou M pra mulher.')

if(pesoIdeal > 0):
    print('O sexo informado foi: ', sexo.upper())
    print('Seu peso ideal é: ', round(pesoIdeal, 2))

imc = round(peso/altura**2 ,1)


if imc < 18.5:
    print('seu IMC é: ', imc, ': abaixo do peso')
elif imc < 25:
    print('seu IMC é: ', imc, ': peso normal')
elif imc < 30:
    print('seu IMC é: ', imc, ': sobrepeso')
elif imc < 35:
    print('seu IMC é: ', imc, ': obesidade grau 1')
elif imc < 40:
    print('seu IMC é: ', imc, ': obeisdade grau 2')
else:
    print('seu IMC é: ', imc, ': obesidade grau 3')

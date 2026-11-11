print('+---------------------------+')
print('| Calculo de EMC            |')
print('+---------------------------+')

peso = float(input('Digite seu Peso: '))
altura = float(input('Digite sua Altura: '))

emc = peso / altura ** 2

print('Seu IMC é: ', emc)

if emc < 18.5:
    print('Abaixo do Peso')
elif emc >= 18.5 and emc < 25:
    print('Peso Normal')
elif emc >= 25 and emc < 30:
    print('Sobrepeso')
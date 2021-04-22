print('''========================================
Olá, eu sou a super calculadora!
========================================
[1] Adição
[2] Subtração
[3] Divisão
[4] Multiplicação
========================================''')
opera = int(input('Escolha uma operação:'))
if opera == 1:
    escolha = 'Adição'
elif opera == 2:
    escolha = 'Subtração'
elif opera == 3:
    escolha = 'Divisão'
elif opera == 4:
    escolha = 'Multiplicação'
print('Você escolheu {}!'.format(escolha))
print('========================================')
num1 = int(input('Escolha o primeiro número:'))
num2 = int(input('Escolha o segundo número:'))
if opera == 1:
    resul = (num1 + num2)
elif opera == 2:
    resul = (num1 - num2)
elif opera == 3:
    resul = (num1 / num2)
elif opera == 4:
    resul = (num1 * num2)
print('O resultado final foi {}'.format(resul))

import random
maximo = random.randint(0, 100)
print(" O máximo actual é : ", maximo)
leitura = int(input('Insira o valor da leitura: '))
if leitura > maximo:
    maximum = leitura
    print('Obtivemos um novo record ', maximo)
else :
    print("Não temos nunhum recorde no momento")

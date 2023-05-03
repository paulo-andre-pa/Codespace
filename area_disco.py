import math
#Aplicação para calcular a area e a circunfârencia de um disco
raio = int(input('Insira o valor do raio do disco : '))
print("O valor do raio é :", raio)
area_disco = math.pi * (raio ** 2)
print('A área do seu disco de raio :', raio, ": é", area_disco)
diametro_disco = 2 * math.pi
print ('A diâmetro do seu disco de raio', raio, ': é : ', diametro_disco)

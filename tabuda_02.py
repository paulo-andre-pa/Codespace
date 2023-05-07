#Vamos criar uma Tabela onde vamos adicionar cada resultado da multiplicação
# Para adicionar 
def tabuada(termo_primeiro, base, termo_ultimo):
    resultado = []
    while termo_primeiro < termo_ultimo : 
        termo = termo_primeiro * base
        termo_primeiro = termo_primeiro + 1
        resultado.append(termo) 
tabuadaMult = tabuada(int(input('Insira o seu primeiro termo :')), int(input('Insira a base da multipicação : ')), int(input('Insira o último termo da multiplicação : ')))
print(tabuadaMult)

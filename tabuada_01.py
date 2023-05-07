def tabuda(base): 
    resultado = [] # O resultado é primeiramente uma lista vázia
    n = 1
    while n < 11 :
        b = n * base
        resultado.append(b)
        n += 1
    return resultado
tab9 = tabuda(9)
print(tab9)

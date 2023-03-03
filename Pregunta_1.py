def preimagen(f, E, I, D):
    resultados = []
    for x in D:
        if f(x) in I:
            if f(x) in E:
                resultados.append(x)
        else:
            continue
    return resultados

def f(x):
    return x**2

D = {-4,-3,-2,-1,0,1,2,3,4,5,6}
I = {0,1,4,9,16}
E = {1}

resultado = preimagen(f, E, I, D)
print(resultado)


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


def es_continua(f, TD, TI, I, D):
    for A in TI:
        preimg = preimagen(f, A, I, D)
        if preimg not in TD:
            return "No continua"
        return "Continua"


D = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
I = [0, 1, 4, 9, 16]

#2
TD = [[],[0], [-3,-1, 1, 3], [-4, -2, 2, 4], [-3, -1, 0, 1, 3], [-4, -2, 0, 2, 4], [-4, -3, -2, -1, 1, 2, 3, 4], [-4, -3, -2, -1, 0, 1, 2, 3, 4]]
TI = [[0], [1, 9], [4, 16], [0, 1, 9], [0, 4, 16], [1, 4, 9, 16], [0, 1, 4, 9, 16]]
print("La pregunta 2 es:", es_continua(f, TD, TI, I, D))

#3
#A
TD = [[], D]
TI = [[], I]

print("El inciso A de la pregunta 3 es:", es_continua(f, TD, TI, I, D))

#B
def f(x):
    return 0

def power_set(S):
    if not S:
        return [[]]
    else:
        x = S.pop()
        p = power_set(S)
        return p + [[x] + s for s in p]


I_set = set(I)
I_power_set = power_set(I_set)

print("El inciso B de la pregunta 3 es:", es_continua(f, I_power_set, I_power_set, I, I))

#C
def f(x):
    return -x


I_set = set(D)
I_power_set = power_set(I_set)

print("El inciso C de la pregunta 3 es:", es_continua(f, I_power_set, I_power_set, D, D))

#D
TD = [[],[0],[-4,-3,-2,-1],[1,2,3,4],[0,1,2,3,4],[0,-1,-2,-3,-4],[-4,-3,-2,-1,1,2,3,4],D]
print("El inciso D de la pregunta 3 es:", es_continua(f, TD, TD, D, D))

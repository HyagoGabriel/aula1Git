import time

tupla = tuple()

tupla = (1)

tupla = (1,)

tupla = 1, 2, 3

print(tupla)

print(tupla[1])

# tupla[0] = 100 #erro pois nao é possivel alterar um tupla 

#Manipulando dicionario:
dic = {"semMundial" : "Palmeiras", "1Mundial" :"Corinthians", "2Mundial" : "SaoPaulo"}

print(dic['semMundial'])

notas = {"}mat":5, "lp":10, "ef":8}

print(notas)
print(notas["lp"])

# print(notas["bio"])

print(dir(notas))

print(notas.values())

print(notas.keys())

print(len(notas))

for disciplina in notas.keys():
    print(disciplina)




time.sleep(0.1)
frutas = ["laranja", "maca", "uva"]

nomes = []

letras = list("python")

numeros = list(range(10))

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "Sao Paulo", True]

#acesso direto
print(frutas[0])
print(frutas[2])

#indices negativos
print(frutas[-1])
print(frutas[-2])

#listas aninhadas
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"],
]

print(matriz[0]) #primeira linha 1, a, 2
print(matriz[0][0]) #item da primeira linha, primeira coluna
print(matriz[0][-1]) #2
print(matriz[-1][-1]) #c

#fatiamento
lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:]) # thon
print(lista[:2]) # py
print(lista[1:3]) # yt
print(lista[0:3:2]) #pt
print(lista[::]) # python
print(lista[::-1]) #nohtyp

#iterar lista
carros = ["gol", "celta", "palio"]

for modelo in carros:
    print(modelo)

#função enumerate
for indice, modelo in enumerate(carros):
    print(f"{indice}: {modelo}")

#compreensão de listas
numeros = [1, 30, 21, 2, 9, 65, 34]

#filtro versao 1
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

#filtro versao 2
pares2 = [numero for numero in numeros if numero % 2 == 0]
#numero = o que será gerado
#for numero in numeros = for
#opcional: if numeros % 2 == 0
print(pares2)

#modificando valores versão 1
quadrado = []
for numero in numeros:
    quadrado.append(numero ** 2)
print(quadrado)

quadrado2 = [numero ** 2 for numero in numeros]
print(quadrado2)

frutas = ("laranja", "pera", "uva", )

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil", )

#acesso direto 
print(frutas[0])
print(frutas[-1])

#tupla aninhada
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

#fatiamento
tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[2:]) # thon
print(tupla[:2]) # py
print(tupla[1:3]) # yt
print(tupla[0:3:2]) #pt
print(tupla[::]) # python
print(tupla[::-1]) #nohtyp

#iterar tupla
carros = ("gol", "celta", "palio")

for carro in carros:
    print(carro)

#enumerate
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")



numeros = set([1,2,3,1,3,4])
letras = set("abacaxi")
carros = set(("palio", "gol", "celta", "palio"))

print(numeros)
print(letras)
print(carros)

linguagens = {"python", "java", "python"}
print(linguagens)

#acessando os dados
num = {1, 2, 3, 2}
num = list(num) #transformar em lista
print(num[0])

#iterar
carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

#enumerate
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

    



texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()


for numero in range(0, 51, 5):
    print(numero, end=" ")


for numero in range(100):

    if numero % 2 == 0:
        continue

    print(numero, end=" ")
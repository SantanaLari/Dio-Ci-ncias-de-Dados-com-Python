#[].append
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)

#[].clear
lista.clear()

print(lista)

#[].copy
lista = [1,2,3]
l2 = lista.copy()

print(lista)
print(id(l2), id(lista))

#[].count
cores = ["vermelho", "azul", "verde", "azul"]
print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))

#[].extend (juntar outra lista com a primeira lista)
linguagens = ["python", "js", "c"]

print(linguagens)

linguagens.extend(["java", "csharp"])

print(linguagens)

#[].index
linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))
print(linguagens.index("python"))

#[].pop - passa o indice do objeto ou remove o ultimo
linguagens.pop()
linguagens.pop()

print(linguagens)

linguagens.pop(0)

print(linguagens)

#[].remove - passa o nome do objeto
linguagens.remove("c")

print(linguagens)

#[].reverse - espelhamento
linguagens = ["java", "python", "c"]

linguagens.reverse()

print(linguagens)

#[].sort
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort() #ordem alfabetica
print(linguagens)

linguagens.sort(reverse=True) #ao contrario
print(linguagens)

linguagens.sort(key=lambda x: len(x)) #ordenar por tamanho
print(linguagens)

linguagens.sort(key=lambda x: len(x), reverse=True) #ordenar por tamanho ao contrario
print(linguagens)

#len
print(len(linguagens))

#sorted
print(sorted(linguagens, key=lambda x: len(x)))
print(sorted(linguagens, key=lambda x: len(x), reverse=True))
print(sorted(linguagens))



numeros = [1, 30, 21, 2, 9, 65, 34]

pares2 = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]

print(pares2)




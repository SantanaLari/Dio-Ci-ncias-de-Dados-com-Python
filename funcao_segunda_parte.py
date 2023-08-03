#parametros especiais
#def f(pos1, pos2 / pos_or_kwd, *, kwd1, kwd2)
#      position only   position or keyword,  keyword only

#Positional only
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0",
combustivel="Gasolina")

#Keyword only
def criar_carro2(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro2(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat",
motor="1.0", combustivel="Gasolina")

#keyword and positional only
def criar_carro3(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro3("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0",
combustivel="Gasolina")

#objetos de primeira classe
def somar(a, b):
    return a + b

def substracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")

exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, substracao)
exibir_resultado(10, 10, multiplicacao)

op = somar

print(op(1, 23))

#Escopo local e escopo global
salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))

#exemplo:
def salario_bonus(lista):
    lista.append(2)

lista = [1]
print(lista)
salario_bonus(lista)
print(lista)


def salario_bonus2(lista):
    lista_aux = lista.copy()
    lista_aux.append(3)
    print(lista_aux)


lista2 = [1]
print(lista2)
salario_bonus2(lista2)


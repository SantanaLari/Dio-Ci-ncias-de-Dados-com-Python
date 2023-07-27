#{}.clear

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melanie", "telefone": "3333-7766", "extra": {"a": 1}},
}

contatos.clear()
print(contatos)

#{}.copy
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

contatos["guilherme@gmail.com"]

copia["guilherme@gmail.com"]

#{}.fromkeys
dict.fromkeys(["nome", "telefone"])
dict.fromkeys(["nome", "telefone"], "vazio")

#{}.get
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

contatos["chave"]

contatos.get("chave")
contatos.get("chave", {})
contatos.get("gulherme@gmail.com", {})

#{}.items
contatos.items()

#{}.keys
contatos.keys()

#{}.pop
contatos.pop("guilherme@gmail.com")

#{}.popitem
contatos.popitem()

#{}.setdefault
contatos.setdefault("nome", "Giovanna")

#{}.update
contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})

#{}.values
contatos.values()

#in
"guilherme@gmail.com" in contatos

#del
del contatos["guilherme@gmail.com"]["telefone"]





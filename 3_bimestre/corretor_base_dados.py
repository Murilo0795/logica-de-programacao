dados_brutos = [
    " JOAO.SILVA@ESCOLA.COM ",
    " 000.111.222-33 ",
    " Rua das Flores, No 123 ",
    " MARIA@EMAIL.COM ",
    " 111.222.333-44 ",
    " Avenida Brasil, No 456 "
]

dados_limpos = []

for item in dados_brutos:
    item = item.strip()

    if "@" in item:
        item = item.lower()
      
    if "No" in item:
        item = item.replace("No", "Número")

    if len(item) == 14 and "." in item and "-" in item:
        item = item.replace(".", "").replace("-", "")

    dados_limpos.append(item)

print("Dados limpos:")
print(dados_limpos)

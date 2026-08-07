quantidade = int(input("Quantidade de itens: "))

total = 0.0

for item in range(1, quantidade + 1):
    preco = float(input(f"Preço do item {item}: R$ "))
    total += preco

if quantidade > 0:
    media = total / quantidade
else:
    media = 0.0

print(f"\nTotal da compra: R$ {total:.2f}")
print(f"Média por item: R$ {media:.2f}")
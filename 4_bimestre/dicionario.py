produto = {
    "codigo": 101,
    "nome": "Teclado Mecânico Gamer",
    "preco": 250.0,
    "estoque": 14
}

print("===Produto Cadastrado===")
print(produto)
print(f"Nome do produto: {produto['nome']}")
print(f"Preço unitário: R$ {produto['preco']:.2f}")
print("-" * 40)

produto["preco"] = 220
produto["estoque"] = produto["estoque"] + 6
produto["categoria"] = "Periféricos"
print("===Produto Atualizado===")
print(produto)
print(f"Novo estoque total: {produto['estoque']} unidades")
print("-" * 40)

usuario = {
    "nome": "João Silva",
    "nivel": "Administrador",
    "ativo": True
}

print("===INSPEÇÃO DE REGISTRO DO USUÁRIO===")
print("Chaves de registro", usuario.keys())
print("Valores de registro", usuario.values())
print("-" * 40)

matriz = [
    [3, 8, 1],
    [4, 9, 6],
    [2, 7, 5]
]

print("Exibição da matriz em forma de grade")
for i in range(3):
    for c in range(3):
        print(f"{matriz[i][c]}", end=" ")
        print()
        print("-" * 45)
        print(f"Elemento na linha 0 e coluna 1: {matriz[0][1]}")
        print(f"Elemento na linha 2 e coluna 2: {matriz[2][2]}")

        soma_diagonal = 0

        for i in range(3):
            for c in range(3):
                if i == c:
                    soma_diagonal += matriz[i][c]

                    print(f"Soma dos elementos da diagonal principal: {soma_diagonal}")

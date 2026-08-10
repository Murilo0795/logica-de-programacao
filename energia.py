consumo_total = 0
dias_alto_consumo = 0

for dia in range(1, 8):
    consumo = float(input(f"Informe o consumo do dia {dia} (kWh): "))

    consumo_total += consumo

    if consumo > 20:
        dias_alto_consumo += 1

print("\n===== RELATÓRIO SEMANAL =====")
print(f"Consumo total: {consumo_total:.2f} kWh")
print(f"Dias acima de 20 kWh: {dias_alto_consumo}")

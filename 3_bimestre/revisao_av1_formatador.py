# ==============================================================================
# REVISAO PARA A AV1: MODULARIZACAO E MANIPULACAO DE STRINGS
# ARQUIVO: revisao_av1_formatador.py
# Nome do Aluno:
# Data:
# ==============================================================================

# 1. FUNCAO PARA CITACAO BIBLIOGRAFICA
def formatar_citacao(nome_completo):
    # Separa o nome em partes
    partes = nome_completo.split()

    # Pega o ultimo sobrenome e converte para maiusculas
    sobrenome = partes[-1].upper()

    # Junta os nomes anteriores ao sobrenome
    nome = " ".join(partes[:-1])

    # Retorna no formato "SOBRENOME, Nome"
    return f"{sobrenome}, {nome}"


# 2. FUNCAO PARA GERAR CODIGO/MATRICULA
def gerar_codigo(ano, cpf):
    # Remove espacos extras do CPF
    cpf = cpf.strip()

    # Pega os 3 primeiros caracteres do CPF
    tres_digitos = cpf[:3]

    # Retorna a matricula formatada
    return f"ALU-{ano}-{tres_digitos}"


# --- TESTE DAS FUNCOES (FLUXO PRINCIPAL) ---

autor = "Carlos Eduardo Andrade"
citacao_formatada = formatar_citacao(autor)
print("Citacao Bibliografica:", citacao_formatada)

matricula = gerar_codigo("2026", "456.789.123-00")
print("Matricula Gerada     :", matricula)

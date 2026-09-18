# ==============================================================================
# PROVA PRÁTICA AV2 - 3º BIMESTRE
# ARQUIVO: av2_sistema_modular.py
# Nome do Aluno:
# Data:
# Link do Repositório:
# ==============================================================================

# Lista inicial de dados brutos
# Formato: "nome_completo;cargo_ou_setor;telefone_ou_cpf"
dados_brutos = [
    "  carlos eduardo silva;desenvolvedor;11988887777  ",
    "  ana paula mendes;analista de rh;21977776666  ",
    "  roberto carlos oliveira;gerente de projetos;31966665555  "
]


# ------------------------------------------------------------------------------
# 1. FUNÇÕES DO SISTEMA
# ------------------------------------------------------------------------------

def limpar_e_formatar_texto(texto):
    """
    FUNÇÃO 1:
    Remove espaços das pontas e converte o texto para letras maiúsculas.
    """
    texto_formatado = texto.strip().upper()
    return texto_formatado


def extrair_codigo_ou_ddd(dado):
    """
    FUNÇÃO 2:
    Remove espaços das pontas e utiliza fatiamento para
    extrair os dois primeiros dígitos do telefone.
    """
    dado_limpo = dado.strip()
    ddd = dado_limpo[0:2]
    return ddd


def processar_e_exibir_cadastros(lista_dados):
    """
    FUNÇÃO 3:
    Percorre a lista de cadastros utilizando FOR,
    separa os dados com SPLIT, chama as outras funções
    e exibe os resultados.
    """
    total_processado = 0

    for cadastro in lista_dados:
        # Separa os dados utilizando o ponto e vírgula
        partes = cadastro.split(";")

        # Obtém cada informação do cadastro
        nome = partes[0]
        cargo = partes[1]
        telefone = partes[2]

        # Utiliza as funções para formatar os dados
        nome_formatado = limpar_e_formatar_texto(nome)
        cargo_formatado = limpar_e_formatar_texto(cargo)
        ddd = extrair_codigo_ou_ddd(telefone)

        # Exibe o cadastro formatado
        print("-----------------------------------------------")
        print(f"Nome: {nome_formatado}")
        print(f"Cargo/Setor: {cargo_formatado}")
        print(f"DDD/Código: {ddd}")

        # Conta o registro processado
        total_processado += 1

    return total_processado


# ------------------------------------------------------------------------------
# 2. PROGRAMA PRINCIPAL
# ------------------------------------------------------------------------------

def main():
    print("==================================================")
    print("     SISTEMA DE GESTÃO MODULARIZADO - AV2        ")
    print("==================================================\n")

    print("Iniciando o processamento dos dados...\n")

    # Chama a Função 3 passando a lista de dados
    total_processado = processar_e_exibir_cadastros(dados_brutos)

    # Exibe a quantidade total de registros processados
    print("\nQuantidade total de registros processados:",
          total_processado)

    print("\n==================================================")
    print("             PROCESSAMENTO CONCLUÍDO              ")
    print("==================================================")


# Execução do programa
if __name__ == "__main__":
    main()

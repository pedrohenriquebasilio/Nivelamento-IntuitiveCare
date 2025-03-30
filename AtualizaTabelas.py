import pdfplumber
import csv
import os

# Define o diretório base de forma relativa
base_dir = r"C:\ROBOS\AtualizaTabelasproced\anexos"

# Caminho do PDF
caminho_pdf = os.path.join(base_dir, "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf")

# Nome do arquivo CSV de saída no mesmo diretório do PDF
arquivo_csv = os.path.join(base_dir, "dados_extraidos_corrigidos.csv")

# Variável para armazenar o cabeçalho e evitar duplicação
cabecalho_salvo = None

# Verifica se o arquivo existe antes de processar
if not os.path.exists(caminho_pdf):
    print(f"❌ Arquivo não encontrado: {caminho_pdf}")
else:
    with pdfplumber.open(caminho_pdf) as pdf:
        with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            for pagina in pdf.pages:
                tabelas = pagina.extract_table()  # Tenta extrair as tabelas da página

                if tabelas:  # Se houver tabelas na página
                    for i, linha in enumerate(tabelas):
                        if i == 0:  # Primeira linha da tabela pode ser o cabeçalho
                            if cabecalho_salvo is None:
                                # Substitui valores no cabeçalho
                                cabecalho_salvo = [col.replace("OD", "Seg. Odontologica").replace("AMB", "Seg. Ambulatorial") for col in linha]
                                writer.writerow(cabecalho_salvo)  # Escreve no CSV
                        else:
                            writer.writerow(linha)  # Adiciona as linhas de dados normalmente

    print(f"✅ Extração refinada concluída! Arquivo salvo em {arquivo_csv}")

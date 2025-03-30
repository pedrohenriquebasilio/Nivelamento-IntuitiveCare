import pdfplumber
import csv
import os


base_dir = r"C:\ROBOS\AtualizaTabelasproced\anexos"


caminho_pdf = os.path.join(base_dir, "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf")


arquivo_csv = os.path.join(base_dir, "dados_extraidos_corrigidos.csv")


cabecalho_salvo = None


if not os.path.exists(caminho_pdf):
    print(f"❌ Arquivo não encontrado: {caminho_pdf}")
else:
    with pdfplumber.open(caminho_pdf) as pdf:
        with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

  

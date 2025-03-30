import pdfplumber
import csv
import os


base_dir = r"C:\ROBOS\AtualizaTabelasproced\anexos"


caminho_pdf = os.path.join(base_dir, "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf")


arquivo_csv = os.path.join(base_dir, "dados_extraidos_corrigidos.csv")

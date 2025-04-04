import pdfplumber
import csv
import os
import zipfile

# Diretório base
base_dir = r"C:\ROBOS\AtualizaTabelasproced\anexos"

# Caminho do PDF e do CSV
caminho_pdf = os.path.join(base_dir, "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf")
arquivo_csv = os.path.join(base_dir, "dados_extraidos_corrigidos.csv")

# Caminho do ZIP final
zip_path = os.path.join(base_dir, "Teste[Pedro Henrique Basilio].zip")

# Variável para armazenar o cabeçalho e evitar duplicação
cabecalho_salvo = None

if not os.path.exists(caminho_pdf):
    print(f"❌ Arquivo não encontrado: {caminho_pdf}")
else:
    with pdfplumber.open(caminho_pdf) as pdf:
        with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            for pagina in pdf.pages:
                tabelas = pagina.extract_table()

                if tabelas:
                    for i, linha in enumerate(tabelas):
                        if i == 0:
                            if cabecalho_salvo is None:
                                # Substitui valores no cabeçalho
                                cabecalho_salvo = [
                                    col.replace("OD", "Seg. Odontologica").replace("AMB", "Seg. Ambulatorial")
                                    for col in linha
                                ]
                                writer.writerow(cabecalho_salvo)
                        else:
                            writer.writerow(linha)

    print(f"✅ Extração do arquivo concluída! Arquivo salvo em {arquivo_csv}")

    # Criar o arquivo ZIP
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(arquivo_csv, os.path.basename(arquivo_csv))

    print(f"✅ Arquivo compactado com sucesso! Arquivo salvo em {zip_path}")
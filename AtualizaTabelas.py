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

            
          for pagina in pdf.pages:
                tabelas = pagina.extract_table()  

                if tabelas:
                    for i, linha in enumerate(tabelas):
                        if i == 0:  
                            if cabecalho_salvo is None:
                                # Substitui valores no cabeçalho
                                cabecalho_salvo = [col.replace("OD", "Seg. Odontologica").replace("AMB", "Seg. Ambulatorial") for col in linha]
                                writer.writerow(cabecalho_salvo) 
                        else:
                            writer.writerow(linha) 

    print(f"✅ Extração refinada concluída! Arquivo salvo em {arquivo_csv}")           

  

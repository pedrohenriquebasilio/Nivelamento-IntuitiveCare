# **README - Desafio de Transformação de Dados**

## **Objetivo**
Este projeto tem como objetivo extrair dados de uma tabela do PDF, salvar os dados em um arquivo CSV, e compactá-lo em um arquivo ZIP. A tabela é parte do "Rol de Procedimentos e Eventos em Saúde" contido no Anexo I do teste fornecido.

## **Descrição do Projeto**
1. **Extração de Dados**: O código utiliza a biblioteca `pdfplumber` para abrir o PDF e extrair as tabelas contidas em todas as páginas do arquivo. 
2. **Salvamento em CSV**: Após extrair os dados, o código salva as informações extraídas em um arquivo CSV, com um cabeçalho customizado. 
3. **Compactação em ZIP**: O arquivo CSV gerado é compactado em um arquivo ZIP com o nome "Teste_[Seu_nome].zip".

## **Bibliotecas Utilizadas**
- `pdfplumber`: Biblioteca Python para extrair texto e tabelas de arquivos PDF. 
- `csv`: Biblioteca padrão do Python para manipulação de arquivos CSV.
- `os`: Biblioteca padrão para manipulação de caminhos e arquivos.
- `zipfile`: Biblioteca padrão para criação de arquivos ZIP.

## **Escolha do Python**
A escolha do Python se deve à sua simplicidade e robustez na manipulação de arquivos PDF. A biblioteca `pdfplumber` é excelente para a extração de tabelas de arquivos PDF, oferecendo uma interface mais intuitiva do que outras alternativas. 
Em uma tentativa inicial de usar uma biblioteca PDF nativa de Java, percebi que o processo de extração era mais complexo e menos eficiente. A biblioteca Python, por outro lado, simplificou o processo de extração e adaptação dos dados.

## **Passos para Execução**
1. Certifique-se de ter o Python instalado. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).
2. Instale a biblioteca `pdfplumber` executando o comando abaixo:
   ```bash
   pip install pdfplumber

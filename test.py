from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Caminho para o arquivo PDF
def escolherArquivo():
    
    janela_padrao = Tk().withdraw()
    caminho_do_arquivo = askopenfilename(filetypes = (("Arquivos em pdf", "*.pdf"), ("Arquivos csv", "*.csv")))

    if caminho_do_arquivo:
        with open(caminho_do_arquivo, encoding='latin_1') as arquivo:
            for linha in arquivo:
                print(linha, end='')
        return caminho_do_arquivo
    else:
        print("Nenhum arquivo selecionado")

from PyPDF2 import PdfReader
from unidecode import unidecode

# Função para extrair texto do PDF
def extract_text_from_pdf():
    arquivo = escolherArquivo()
    text = ''
    with open(arquivo, 'rb') as file:
        reader = PdfReader(file)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

# Função para remover acentuação das vogais e substituir "ç" por "c"
def remove_accents_and_cedilla(text):
    text = unidecode(text)
    return text

# Função para converter texto para maiúsculas
def convert_to_uppercase(text):
    text = text.upper()
    return text

# Função para gravar texto em um arquivo de texto
def write_text_to_txt(text, txt_file_path):
    with open(txt_file_path, 'w', encoding='utf-8') as file:
        file.write(text)

# Extrair texto do PDF
pdf_text = extract_text_from_pdf()

# Remover acentuação das vogais e substituir "ç" por "c"
pdf_text = remove_accents_and_cedilla(pdf_text)

# Converter texto para maiúsculas
pdf_text = convert_to_uppercase(pdf_text)

# Gravar texto em um arquivo de texto
txt_file_path = 'extrato_conta_corrente.txt'
write_text_to_txt(pdf_text, txt_file_path)

print("Texto extraído do PDF e gravado em um arquivo de texto com sucesso!")

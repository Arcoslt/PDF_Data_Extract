from PyPDF2 import PdfFileReader

from tkinter import Tk
from tkinter.filedialog import askopenfilename

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
        
    

def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)

if __name__ == '__main__':

    path = escolherArquivo()
    extract_information(path)
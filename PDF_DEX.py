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
        
import fitz
def get_pdf_content_lines(pdf_path):
    doc = fitz.open(pdf_path)

    for page_number in range(doc.page_count):
        page = doc[page_number]
        text = page.get_text("text")
        
        # Splitting the text into lines and printing each line
        lines = text.split('\n')
        for line_number, line in enumerate(lines, 1):
            if('PIX RECEB.OUTRA IF' in line):
                print(f"Line {line_number}: {line}")


        
if __name__ == '__main__':

    path = escolherArquivo()
    get_pdf_content_lines(path)
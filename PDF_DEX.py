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
import pandas as pd

def extract_text_from_pdf(pdf_path):
    data = {'Page': [], 'Line': [], 'Text': []}

    doc = fitz.open(pdf_path)

    for page_number in range(doc.page_count):
        page = doc[page_number]
        text = page.get_text("text")
        
        # Splitting the text into lines and storing in DataFrame
        lines = text.split('\n')
        for line_number, line in enumerate(lines, 1):
            data['Page'].append(page_number + 1)
            data['Line'].append(line_number)
            data['Text'].append(line)

    doc.close()

    df = pd.DataFrame(data)
    return df

if __name__ == '__main__':

    path = escolherArquivo()
    df = extract_text_from_pdf(path)
    print(df.to_string(index=False))
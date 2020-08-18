import os
from PyPDF2 import PdfFileReader, PdfFileMerger

def juntar_pdf(diretorio):
    arquivos_pdf = [nome_arquivo for nome_arquivo in os.listdir(diretorio) if nome_arquivo.endswith("pdf")]
    agregador = PdfFileMerger()

    for nome_arquivo in arquivos_pdf:
        agregador.append(PdfFileReader(os.path.join(diretorio, nome_arquivo), "rb"))

    agregador.write(os.path.join(diretorio, "pdf_agregado.pdf"))

from pdf2docx import Converter

pdf_path="sample.pdf"
docx_path="sample.docx"


ex = Converter(pdf_file= pdf_path)
ex.convert(docx_filename=docx_path)
ex.close()

from pdf2docx import parse
pdf_file="Mth501 Quiz#1 Mega File.pdf"
word_file="Mth501 Quiz#1 Mega File.docx"

parse(pdf_file, word_file, start=0, end=None)
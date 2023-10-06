import os
import sys
import PyPDF2

# inputs = sys.argv[1:]

inputs = os.listdir(sys.argv[1])
inputs.remove(".DS_Store")
inputs.sort()

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(sys.argv[1] + pdf)
    merger.write(sys.argv[1] + 'merged.pdf')
        
pdf_combiner(inputs)

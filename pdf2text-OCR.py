#!/usr/bin/python3

# Python 3 version 

# by Maxim Leyenson, <leyenson@gmail.com>
# under GNU license

# This simple script performs an OCR (optycal character recognition) on a raster 
# PDF file via Tesseract and produces a plain text

# Requirements: poppler-utils(for pdfinfo), GhostScript (gs), tesseract

# Usage: OCR.py <input.pdf> <output.txt> <language> 
# where  language is a 3-character ISO 639-2 code

# Examples:  
#         $ OCR.py book.pdf book.txt eng
#         $ OCR.py book.pdf book.txt eng+fra


import sys
import os
# import commands
import subprocess

import PyPDF2


# ------------ This function computes number of pages in a PDF file --

def numberOfPagesInPdfFile(filename):
    print("[computing number of pages in a pdf file]")

    from PyPDF2 import PdfFileReader
    # to compute the number of pages in PDF file

    pdf_input = PdfFileReader(open(filename, "rb"))

    #   open("f.pdf", "rb")  is a Python "file object";
    #   open() is a built-in Python function;
    #   'b' stands for 'binary';
    #
    # PdfFileReader(stream)
    #     Initializes a PdfFileReader object.
    #                    stream : A File object

    # getting number of pages:
    number_of_pages = pdf_input.getNumPages()

    # pages = int(pages)
    return number_of_pages 

# -------------------- reading input ---------------------
# -- getting the filenames (i.e. input.pdf output.djvu)
try:
    filename =  sys.argv[1]
    output   =  sys.argv[2]
    language =  sys.argv[3]

    print("file to process:", filename)
    print("output file", output)
    print("language: ", language)

except:
    print('Usage: OCR.py <input.pdf> <output.txt> <language> ')
    print('where  <language> is a 3-character ISO 639-2 code.')
    print(' ')
    print('Examples: ')
    print('   pdf2text-OCR.py  book.pdf book.txt eng')
    print('   pdf2text-OCR.py  book.pdf book.txt rus')
    print('   pdf2text-OCR.py  book.pdf book.txt eng+fra')
    print(' ')
    print('some language codes: ')
    print(' ')
    print(' English: eng')
    print(' French:  fra (sic!)')
    print(' German:  deu')
    print(' Hebrew:  heb')
    print(' Italian: ita')
    print(' Russian: rus')
    sys.exit(1) 


print("[creating empty text file]")
cmd = 'echo > ' + output
print('> ' + cmd)
os.system(cmd)

#-- 

firstpage = 1
lastpage = numberOfPagesInPdfFile(filename)

#               OCR
#-- pdf -> tiff -> text


for i in range (firstpage,lastpage+1):   # 1-(n-1)
    print("--------------- Page", str(i), "/", lastpage, "---------------")
    print("(converting page to tiff)")
    cmd = 'gs -dBATCH -dNOPAUSE -sDEVICE=tiffgray '
    cmd = cmd + ' -sOutputFile=page.tif '
    cmd = cmd + ' -dFirstPage=' + str(i) + ' -dLastPage=' + str(i)
    cmd = cmd + ' -r300 ' + filename
    print('> ' + cmd)
    os.system(cmd)
    print("(running tesseract)")
    cmd = 'tesseract page.tif page -l ' + language
    #    cmd = cmd +  ' -psm 4 '  # Assume a single column of text of variable sizes.  
    #  Mint's version of tesseract does not like this
    print('> ' + cmd)
    os.system(cmd)
    print("[done]")
    cmd = 'cat page.txt >> ' + output
    print('> ' + cmd)
    os.system(cmd)
    cmd = 'echo >> ' + output
    print('> ' + cmd)
    os.system(cmd)
    # cmd = 'rm -vf *.tif '
    # os.system(cmd)

# cleaning..
cmd = 'rm -vf *.tif page.txt'
os.system(cmd)

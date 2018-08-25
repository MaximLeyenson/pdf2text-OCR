#!/usr/bin/python

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
import commands


# ------------ This function computes number of pages in a PDF file --

def numberOfPagesInPdfFile(filename):
    print "[computing number of pages in a pdf file]"
    command ="pdfinfo " + filename + " | grep --text Pages | sed 's/Pages://g;' "
    #  --text: for some reason grep sometimes assumes that pdfinfo output is binary
    print "   executing ", command
    pages = commands.getoutput(command)
    print "[got ", pages, " pages]"
    pages = int(pages)
    # print "[int() = ", pages, "]"
    return pages

# -------------------- reading input ---------------------
# -- getting the filenames (i.e. input.pdf output.djvu)
try:
    filename =  sys.argv[1];
    output   =  sys.argv[2];
    language =  sys.argv[3];
except:
    print 'Usage: %s <input.pdf> <output.txt> <language> ' % sys.argv[0];  #  sys.argv[0] = program name
    sys.exit(1) 

print "[creating empty text file]"
cmd = 'echo > ' + output
print '> ' + cmd
os.system(cmd)

#-- 

firstpage = 1
lastpage = numberOfPagesInPdfFile(filename)

#               OCR
#-- pdf -> tiff -> text


for i in range (firstpage,lastpage+1):   # 1-(n-1)
    print "--------------- Page", str(i), "/", lastpage, "---------------"
    print "(converting page to tiff)"
    cmd = 'gs -dBATCH -dNOPAUSE -sDEVICE=tiffgray '
    cmd = cmd + ' -sOutputFile=page.tif '
    cmd = cmd + ' -dFirstPage=' + str(i) + ' -dLastPage=' + str(i)
    cmd = cmd + ' -r300 ' + filename
    print '> ' + cmd
    os.system(cmd)
    print "(running tesseract)"
    cmd = 'tesseract page.tif  page -l ' + language
    cmd = cmd +  ' -psm 4 '  # Assume a single column of text of variable sizes.  
    print '> ' + cmd
    os.system(cmd)
    print "[done]"
    cmd = 'cat page.txt >> ' + output
    print '> ' + cmd
    os.system(cmd)
    cmd = 'echo >> ' + output
    print '> ' + cmd
    os.system(cmd)
    cmd = 'rm -vf *.tif '
    os.system(cmd)

cmd = 'rm -vf page.txt'
os.system(cmd)

# pdf2text-OCR

This simple script performs an OCR (optycal character recognition) on a raster 
PDF file via Tesseract and produces a plain text


Requirements: [poppler-utils](https://en.wikipedia.org/wiki/Poppler_(software)#poppler-utils)(for pdfinfo), 
GhostScript (gs), [tesseract](https://en.wikipedia.org/wiki/Tesseract)

Say, in Fedora Linux you install them with

```bash
# dnf install -y poppler-utils ghostscript tesseract
# dnf install -y tesseract-langpack-fra
```

(and whatever other languages you need)


Remark: You do not need this script if your PDF file already contains a text 
layer.  In this case all you have to do is run 
```bash
$ pdftotext -layout -nopgbrk book.pdf book.txt
``` 
where pdftotext is a part of the standard library poppler-utils.)
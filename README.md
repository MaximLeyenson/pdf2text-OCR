# pdf2text-OCR

This simple script performs an OCR (optical character recognition) on a raster 
PDF file via Tesseract and produces a plain text

**Usage** 

```bash
$ pdf2text-OCR.py <input.pdf> <output.txt> <language> 
```
where  \<language\> is a 3-character ISO 639-2 code.

Examples:  

```bash
$ pdf2text-OCR.py  book.pdf book.txt eng
$ pdf2text-OCR.py  book.pdf book.txt eng+fra
```


**Requirements**
  * [poppler-utils](https://en.wikipedia.org/wiki/Poppler_(software)#poppler-utils)(for pdfinfo), 
  * GhostScript (gs), 
  * [tesseract](https://en.wikipedia.org/wiki/Tesseract)

Say, in Fedora Linux you can install them with

```bash
$ sudo dnf install -y poppler-utils ghostscript tesseract
$ sudo dnf install -y tesseract-langpack-fra
```

(and whatever other languages you need)


**Remark**

You do not need this script if your PDF file already contains a text 
layer.  In this case all you have to do is run 
```bash
$ pdftotext -layout -nopgbrk book.pdf book.txt
``` 
where pdftotext is a part of the standard library poppler-utils.)
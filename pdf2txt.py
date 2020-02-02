# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:31:09 2020

@author: ashutosh
"""

# modules for 
import PyPDF2
# pdf file object
# you can find find the pdf file with complete code in below
pdfFileObj = open(r'C:\Users\ashutosh\Downloads\RESUME ashutosh-converted.pdf', 'rb')
# pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# number of pages in pdf
print(pdfReader.numPages)
# a page object
pageObj = pdfReader.getPage(1)
# extracting text from page.
# this will print the text you can also save that into String
print(pageObj.extractText())
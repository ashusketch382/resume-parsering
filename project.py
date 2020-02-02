# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 04:31:19 2020

@author: ashutosh
"""

import PyPDF2
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer 
from nltk.corpus import stopwords

pdfFileObj = open(r'C:\Users\ashutosh\Downloads\RESUME ashutosh-converted.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
text=pageObj.extractText()
word_tokens=word_tokenize(text)

stop_words = set(stopwords.words('english')) 
filtered_sentence = [] 

for w in word_tokens: 
	if w not in stop_words: 
		filtered_sentence.append(w) 

my_porter = PorterStemmer()   
for w in filtered_sentence: 
    print(w, " : ", my_porter.stem(w))



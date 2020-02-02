# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 04:03:53 2020

@author: ashutosh
"""
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
 
   
quote =  """Natural language processing (NLP) is a field 
       of computer science, artificial intelligence 
       and computational linguistics concerned with  
       the interactions between computers and human  
       (natural) languages, and, in particular, 
       concerned with programming computers to 
       fruitfully process large natural language  
       corpora. Challenges in natural language 
       processing frequently involve natural 
       language understanding, natural language
       generation frequently from formal, machine 
       -readable logical forms), connecting language 
       and machine perception, managing human-
       computer dialog systems, or some combination  
       thereof."""
       
word_tokens = word_tokenize(quote) 


stop_words = set(stopwords.words('english')) 

filtered_sentence = [] 
for w in word_tokens: 
	if w not in stop_words: 
		filtered_sentence.append(w) 
        
        
my_porter = PorterStemmer()   
for w in filtered_sentence: 
    print(w, " : ", my_porter.stem(w))
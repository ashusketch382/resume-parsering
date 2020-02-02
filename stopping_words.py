# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 10:51:18 2020

@author: ashutosh
"""

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

example_sent =  """Natural language processing (NLP) is a field 
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
  

stop_words = set(stopwords.words('english')) 

word_tokens = word_tokenize(example_sent) 

#filtered_sentence = [w for w in word_tokens if not w in stop_words] 

filtered_sentence = [] 

for w in word_tokens: 
	if w not in stop_words: 
		filtered_sentence.append(w) 

print(word_tokens) 
print(filtered_sentence) 

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 18:38:23 2019

@author: shekh
"""

import nltk
import string
import math 
file_content = open("31100.txt").read()
tokens_0 = nltk.sent_tokenize(file_content)
def clean_tokenize(sentence):
    # Remove punctuation and digits and newline character
    sentence = sentence.translate(str.maketrans('', '', string.punctuation + string.digits))
    sentence = sentence.replace('\n', ' ')
    return sentence.lower()

#cleaning the sentence tokens
tokens_1 = []
for i in tokens_0:
    tokens_sentence = clean_tokenize(i)
    tokens_1.append(tokens_sentence)

#training and testing data
spl = math.floor(80*len(tokens_1)/100)
train = tokens_1[:spl]
test = tokens_1[spl:]

#'@' denotes start of sentence and '$' denotes end of sentence
#Unigrams
unigram_list = []
tokens_unigram = ['@ '+t+' $' for t in train]
for i in tokens_unigram: 
    tokens_words_unigram = list(nltk.ngrams(nltk.word_tokenize(i), 1))
    unigram_list += tokens_words_unigram
fdist_unigram = nltk.FreqDist(unigram_list)
No_of_unigrams = fdist_unigram.N()
MLE_unigram = {}
for d in list(fdist_unigram):
    MLE_unigram[d] = fdist_unigram[d]/sum(fdist_unigram.values())
    

#bigrams
bigram_list = []
for i in train:
    tokens_words_bigrams = list(nltk.ngrams(nltk.word_tokenize(i), 2, pad_left=True, pad_right=True, left_pad_symbol='@', right_pad_symbol='$'))
    bigram_list += tokens_words_bigrams
#print(bigram_list)
fdist_bigram = nltk.FreqDist(bigram_list)
No_of_bigrams = fdist_bigram.N()
Possible_bigrams = No_of_unigrams * No_of_unigrams
MLE_bigram = {}
for d in list(fdist_bigram):
#    print(d)
    MLE_bigram[d] = fdist_bigram[d]/fdist_unigram[(d[0],)]

#trigrams
trigram_list = []
for i in train:
    tokens_words_trigrams = list(nltk.ngrams(nltk.word_tokenize(i), 3, pad_left=True, pad_right=True, left_pad_symbol='@', right_pad_symbol='$'))
    tokens_words_trigrams.pop(0)
    tokens_words_trigrams.pop()
    trigram_list += tokens_words_trigrams
#print(trigram_list)
fdist_trigram = nltk.FreqDist(trigram_list)
No_of_trigrams = fdist_trigram.N()
#Possible_trigrams = No_of_unigrams * No_of_unigrams * No_of_unigrams
MLE_trigram = {}
for d in list(fdist_trigram):
#    print(d)
    MLE_trigram[d] = fdist_trigram[d]/fdist_bigram[(d[0], d[1],)]

#Quadgram
quadgram_list = []
for i in train:
    if len(i) != 1&0:
        tokens_words_quadgrams = list(nltk.ngrams(nltk.word_tokenize(i), 4, pad_left=True, pad_right=True, left_pad_symbol='@', right_pad_symbol='$'))
#        print(tokens_words_quadgrams)
        tokens_words_quadgrams.pop(0)
        tokens_words_quadgrams.pop()
        tokens_words_quadgrams.pop(0)
        tokens_words_quadgrams.pop()
        quadgram_list += tokens_words_quadgrams
#print(quadgram_list)
fdist_quadgram = nltk.FreqDist(quadgram_list)
No_of_quadgrams = fdist_quadgram.N()
#Possible_trigrams = No_of_unigrams * No_of_unigrams *No_of_unigrams * No_of_unigrams
MLE_quadgram = {}
for d in list(fdist_quadgram):
#    print(d)
    MLE_quadgram[d] = fdist_quadgram[d]/fdist_trigram[(d[0], d[1], d[2],)]
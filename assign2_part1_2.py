# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 00:22:37 2019

@author: shekh
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 02:50:51 2019

"""
import numpy as np
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
MLE_quadgram = {}
for d in list(fdist_quadgram):
#    print(d)
    MLE_quadgram[d] = fdist_quadgram[d]/fdist_trigram[(d[0], d[1], d[2],)]
    
list1 = [[k, v] for k, v in MLE_bigram.items()]

#Sentence and paragraph(5 sentences) formation using bigram MLE probalities
para_bigram = ''
for i in range(5):
    start_word = '@'
    sentence_str_bigram = '@'
    while True:
        list_temp = []
        for i in range(len(list1)):
            if list1[i][0][0] == start_word:
                list_temp.append(list1[i])
                list_temp1 = np.array(list_temp)
        list_temp2 = np.random.multinomial(1, list(list_temp1[:,1]))
        next_word = list_temp[np.where(list_temp2 == 1)[0][0]][0][1]
        sentence_str_bigram = sentence_str_bigram + ' ' + next_word
        start_word = next_word
        
        if next_word == '$':
            break
    para_bigram = para_bigram +' '+ sentence_str_bigram 
    

#Sentence and paragraph(5 sentences) formation using trigram MLE probalities
list2 = [[k, v] for k, v in MLE_trigram.items()]    
para_trigram = ''
for i in range(5):
    start_word = '@'
    list_temp = []
    for i in range(len(list1)):
        if list1[i][0][0] == start_word:
            list_temp.append(list1[i])
            list_temp1 = np.array(list_temp)
    list_temp2 = np.random.multinomial(1, list(list_temp1[:,1]))
    second_word = list_temp[np.where(list_temp2 == 1)[0][0]][0][1]
    sentence_str_trigram = '@' + ' ' + second_word
    while True:
        list_temp = []
        for i in range(len(list2)):
            if list2[i][0][0] == start_word and list2[i][0][1] == second_word:
                list_temp.append(list2[i])
                list_temp1 = np.array(list_temp)
        list_temp2 = np.random.multinomial(1, list(list_temp1[:,1]))
        next_word = list_temp[np.where(list_temp2 == 1)[0][0]][0][2]
        sentence_str_trigram = sentence_str_trigram + ' ' + next_word
        start_word = second_word
        second_word = next_word
        
        if next_word == '$':
            break
    para_trigram = para_trigram +' '+ sentence_str_trigram 
    
#Sentence and paragraph(5 sentences) formation using quadigram MLE probalities
list3 = [[k, v] for k, v in MLE_quadgram.items()]    
para_quadgram = ''
for i in range(5):
    start_word = '@'
    list_temp = []
    for i in range(len(list1)):
        if list1[i][0][0] == start_word:
            list_temp.append(list1[i])
            list_temp1 = np.array(list_temp)
    list_temp2 = np.random.multinomial(1, list(list_temp1[:,1]))
    second_word = list_temp[np.where(list_temp2 == 1)[0][0]][0][1]
    list_temp = []
    for i in range(len(list2)):
        if list2[i][0][0] == start_word and list2[i][0][1] == second_word:
            list_temp.append(list2[i])
            list_temp1 = np.array(list_temp)
    list_temp2 = np.random.multinomial(1, list(list_temp1[:,1]))
    third_word = list_temp[np.where(list_temp2 == 1)[0][0]][0][2]
    sentence_str_quadgram = '@' + ' ' + second_word + ' ' + third_word
    while True:
        list_temp = []
        for i in range(len(list3)):
            if list3[i][0][0] == start_word and list3[i][0][1] == second_word and list3[i][0][2] == third_word:
                list_temp.append(list3[i])
                list_temp1 = np.array(list_temp)
        list_temp2 = np.random.multinomial(1, list(list_temp1[:,1]))
        next_word = list_temp[np.where (list_temp2 == 1)[0][0]][0][3]
        sentence_str_quadgram = sentence_str_quadgram + ' ' + next_word
        start_word = second_word
        second_word = third_word
        third_word = next_word
        
        if next_word == '$':
            break
    para_quadgram = para_quadgram +' '+ sentence_str_quadgram 
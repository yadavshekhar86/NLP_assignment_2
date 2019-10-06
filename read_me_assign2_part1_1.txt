* I have taken the "The complete work of Jane Austen" as my corpus. I have cleaned the corpus
removing unwanted characters and newlines. I have converted everything into lowercase.

* The variables unigram_list, bigram_list, trigram_list, quadgram_list are a list of all the unigrams, 
bigrams, trigrams and quadgrams in the corpus

* The variables fdist_unigram, fdist_bigram, fdist_trigram, fdist_quadgram store the count of all the 
  corresponding n-grams occuring in the corpus.

* The variables MLE_unigram, MLE_bigram, MLE_trigram, MLE_quadgram store the probabilities of the 
  corresponding n-grams in the corpus (i.e for bigrams: MLE  = C(Wi-1, Wi)/C(Wi-1))

* The nunber of unigrams, bigrams, trigrams and quadgrams are also calculated.

* '@' represents the start of a sentence and '$' represents the end of a sentence 
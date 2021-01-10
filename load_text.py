# imports
import nltk
from nltk.tokenize import sent_tokenize
import pandas as pd
import os


def generate():
    '''function to generate random sentence from text file'''
    text = open('odyssey/odyssey.txt',encoding='utf-8').read()
    #Tokenize sentences
    sentences = sent_tokenize(text)
    #print(sentences)
    from pandas import DataFrame
    # Put tokenized sentences in dataframe
    lit = DataFrame (sentences,columns=['tokenized_sentences'])
    print(lit.sample())
generate()

#print('test')



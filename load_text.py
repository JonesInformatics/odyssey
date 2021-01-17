# imports
#import nltk
#from nltk.tokenize import sent_tokenize
import pandas as pd
import os

from urllib import request

url = 'https://www.gutenberg.org/files/1728/1728-0.txt'

response = request.urlopen(url)
raw = response.read().decode('utf8')
#sentences = sent_tokenize(text)
#print(sentences)


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
#generate()



#print('test')
# text = open('odyssey/odyssey.txt',encoding='utf-8').read()
#     #Tokenize sentences
# sentences = sent_tokenize(text)
#     #print(sentences)
# from pandas import DataFrame
#     # Put tokenized sentences in dataframe
# lit = DataFrame (sentences,columns=['tokenized_sentences'])
# print(lit.head())

# print(sentences)
# #lit.to_csv('odyssey_df.csv')
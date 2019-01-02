"""
Name: inverted_index.py
Author: Rupali Sinha
Purpose: To create an inverted index (in-memory) and then search for the words occurring in the documents.
"""

import sys
import glob
import utils
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


if __name__ == '__main__':

    os.chdir(sys.argv[1])
    obj = utils.processText()
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    mapping_dict = {}   # maps the filenames to their respective contents in the dictionary
    inverted_index = {} # to store the inverted index in memory
    unique_words=[]     # list of unique words
    for filename in glob.glob('*.txt'):
        contents = obj.readFile(filename)

        # word tokenize the text
        word_tokens = word_tokenize(contents)

        # normalize the text(bring everything into lower case)
        word_tokens = [word.lower() for word in word_tokens]

        # remove punctuations
        word_tokens = [word for word in word_tokens if word.isalpha()]

        # stem the words
        word_tokens = [stemmer.stem(word) for word in word_tokens]

        # remove stop words
        filtered_sentence = []
        for word in word_tokens:
            if word not in stop_words:
                filtered_sentence.append(word)

        for w in filtered_sentence:
            if w not in unique_words:
                unique_words.append(w)

        mapping_dict[filename] = filtered_sentence

    print('Total unique words are {}'.format(len(unique_words)))

    # function call for making an inverted index
    inverted_index = obj.create_index(mapping_dict, inverted_index, unique_words)

    # function call for searching any word; return None
    obj.search_doc(input('Enter the word(s) you want to search (separated by white space): '),inverted_index)





########################
#  Basic Markov Chain  #
#  Author Paul Gleason #
########################

import numpy as np
import random
import re

#TODO change @ detection to regex (done?)

class variables():
    def __init__(self):
        self.corpus = []
        self.pairs = []
        self.word_dict = {}
        self.sentence = "Null"
        self.temp_word = ''

vari = variables()

def generate(input_file):
    data = open(input_file, encoding='utf8').read()

    vari.corpus = data.split()

    # print(vari.corpus)

    def make_pairs():
        for i in range(len(vari.corpus)-1):
            yield (vari.corpus[i], vari.corpus[i+1])
        
    vari.pairs = make_pairs()

    vari.word_dict = {}

    for word_1, word_2 in vari.pairs:
        if word_1 in vari.word_dict.keys():
            vari.word_dict[word_1].append(word_2)
        else:
            vari.word_dict[word_1] = [word_2]

    # markov_string()

def markov_string():
    first_word = np.random.choice(vari.corpus)

    while first_word.islower():
        first_word = np.random.choice(vari.corpus)

    if re.search(r'.*<@.*>.*' , first_word):
        chain = ['`'+first_word+'`']
    else:
        chain = [first_word]

    # if first_word[0:1] == '<' and first_word[1:2] == '@' and first_word[-1] == '>': 
    #     chain = ['`'+first_word+'`']
    # else:
    #     chain = [first_word]

    num_words = random.randint(5,50)

    for i in range(num_words):
        # work = 0
        # if work == 0:
        #     word = np.random.choice(vari.word_dict[chain[-1]])
        # else:
        #     print('ping')
        #     word = np.random.choice(vari.word_dict[temp_word])
        #     work = 0

        try:
            word = np.random.choice(vari.word_dict[chain[-1]])
        except:
            word = np.random.choice(vari.word_dict[vari.temp_word])
        
        # word = np.random.choice(vari.word_dict.get(chain[-1]))

        if re.search(r'.*<@.*>.*' , word):
            chain.append('`'+word+'`')
            # t = '`'+word+'`'
            vari.temp_word = word
        else:
            chain.append(word)
            vari.temp_word  = word

        # if word[0:1] == '<' and word[1:2] == '@' and word[-1] == '>':
        #     chain.append('`'+word+'`')
        #     # t = '`'+word+'`'
        #     vari.temp_word = word
        #     # work = 1
        #     # print(temp_word)
        #     # print(f'{t[1:3]} + {t[-2:-1]}\n')
        # else:
        #     chain.append(word)
        #     vari.temp_word  = word

    sentence = ' '.join(chain)+ '.'

    vari.sentence = sentence

    max_retries = 20

    # return vari.sentence
    if vari.sentence != "":
        while max_retries != 0 and vari.sentence[-4:-1] == 'the' or vari.sentence[-5:-1] == 'then' or vari.sentence[-2:-1] == ',' or vari.sentence[-3:-1] == 'To' or vari.sentence[-3:-1] == 'to' or vari.sentence[-3:-1] == 'he' or vari.sentence[-4:-1] == 'and' or vari.sentence[-4:-1] == 'but':
            # print(sentence)
            vari.sentence = markov_string()
            # print(max_retries)
            max_retries -= 1
        else:
            return vari.sentence

# generate('parsed_data.txt')
# generate('Masterhacker_bot\masterhacker_parsed_data.txt')
# for _ in range(100):
    # print(markov_string())
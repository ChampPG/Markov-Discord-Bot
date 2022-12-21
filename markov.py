########################
#  Basic Markov Chain  #
#  Author Paul Gleason #
########################

import numpy as np
import random

class variables():
    def __init__(self):
        self.corpus = []
        self.pairs = []
        self.word_dict = {}
        self.sentence = "Null"

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

    chain = [first_word]

    num_words = random.randint(5,50)

    for i in range(num_words):
        chain.append(np.random.choice(vari.word_dict[chain[-1]]))
    
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


# generate('Masterhacker_bot\masterhacker_parsed_data.txt')
# print(markov_string())



# data = open('Masterhacker_bot\masterhacker_parsed_data.txt', encoding='utf8').read()

# corpus = data.split()

# print(corpus)

# def make_pairs(corpus):
#     for i in range(len(corpus)-1):
#         yield (corpus[i], corpus[i+1])

# def generate_sentence():  
#     pairs = make_pairs(corpus)

#     # for i in pairs:
#     #     print(i)

#     word_dict = {}

#     for word_1, word_2 in pairs:
#         if word_1 in word_dict.keys():
#             word_dict[word_1].append(word_2)
#         else:
#             word_dict[word_1] = [word_2]

#     # print(word_dict)

#     first_word = np.random.choice(corpus)

#     while first_word.islower():
#         first_word = np.random.choice(corpus)

#     chain = [first_word]

#     num_words = random.randint(5,50)

#     for i in range(num_words):
#         chain.append(np.random.choice(word_dict[chain[-1]]))
    
#     return ' '.join(chain)+ '.'

# max_retries = 20
# sentence = generate_sentence()

# while max_retries != 0 and sentence[-4:-1] == 'the' or sentence[-5:-1] == 'then' or sentence[-2:-1] == ',' or sentence[-3:-1] == 'To' or sentence[-3:-1] == 'to' or sentence[-3:-1] == 'he' or sentence[-4:-1] == 'and' or sentence[-4:-1] == 'but':
#     # print(sentence)
#     sentence = generate_sentence()
#     # print(max_retries)
#     max_retries -= 1
# else:
#     print(sentence)

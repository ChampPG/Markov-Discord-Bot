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




# Current testing

# import random

# # create a function that reads in the text file
# def read_text_file(filename):
#     with open(filename, 'r') as f:
#         return f.read()

# # create a function to build the markov chain
# def build_markov_chain(text):
#     markov_chain = {}
#     # split the file into a list of words
#     words = text.split()
#     # loop through the words
#     for i in range(len(words) - 2):
#         # get the current and next words
#         current_word = words[i]
#         next_word = words[i+1]
#         # if the current word is not in the markov chain, add it
#         if current_word not in markov_chain:
#             markov_chain[current_word] = []
#         # add the next word to the current word's list of next words
#         markov_chain[current_word].append(next_word)
#     return markov_chain

# # create a function to generate a sentence from the markov chain
# def generate_sentence(markov_chain):
#     # choose a random word from the markov chain as the first word of the sentence
#     current_word = random.choice(list(markov_chain.keys()))
#     sentence = current_word.capitalize()
#     # loop until we reach the end of the sentence
#     while True:
#         # get the next word from the markov chain
#         next_word = random.choice(markov_chain[current_word])
#         # add the next word to the sentence
#         sentence += " " + next_word
#         # if the next word is a period, the sentence is done
#         if next_word[-1] in [".", "?", "!"]:
#             break
#         # set the current word to the next word
#         current_word = next_word
#     return sentence

# if __name__ == "__main__":
#     # read in the text file
#     text = read_text_file("text_file.txt")
#     # build the markov chain
#     markov_chain = build_markov_chain(text)
#     # generate a sentence from the markov chain
#     sentence = generate_sentence(markov_chain)
#     # print the sentence
#     print(sentence)

# Test 1

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

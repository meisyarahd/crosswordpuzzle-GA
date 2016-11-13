# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 09:47:28 2016

@author: meisyarah
"""

import numpy as np
import random

class Skeleton:
    
    def __init__(self):
        pass
    
    def build_skeleton(skeleton):
        return self.skeleton
    
    def random_fill():
        pass


def skeleton():
    skeleton = [[1,1,1,1,0,1,1,1,1,1,1,1,1,1,1],\
                [0,1,0,1,0,1,0,0,1,0,1,0,1,0,1],\
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
                [0,1,0,1,0,1,0,0,1,0,1,0,1,0,1],\
                [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1],\
                [0,1,0,1,0,1,0,1,0,1,0,1,0,0,1],\
                [1,1,1,1,1,1,0,1,1,1,1,1,1,1,1],\
                [0,0,0,1,0,1,0,1,0,1,0,1,0,0,0],\
                [1,1,1,1,1,1,1,1,0,1,1,1,1,1,1],\
                [1,0,0,1,0,1,0,1,0,1,0,1,0,1,0],\
                [1,1,1,1,1,0,1,1,1,1,1,1,1,1,1],\
                [1,0,1,0,1,0,1,0,0,1,0,1,0,1,0],\
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
                [1,0,1,0,1,0,1,0,0,1,0,1,0,1,0],\
                [1,1,1,1,1,1,1,1,1,1,0,1,1,1,1]]
    return np.asarray(skeleton)
    

class Individual:
    
    def __init__(self, skeleton):
        self.skeleton = skeleton
        self.n_row = len(skeleton)
        self.n_col = len(skeleton[0])
    
    def get_wlength(body):
        wlength = {}
        n_row = len(body) - 2
        n_col = len(body[0]) - 2
        for i in range(1,n_row+1):
            for j in range(1,n_col+1):
                if body[i,j] == 1:
                    key = (i-1, j-1)
                    if body[i,j-1] == 0:
                        wlen = 0
                        while body[i,j] != 0:
                            wlen += 1
                            j += 1
                        if wlen > 1:
                            wlength[key] = wlen
        return (wlength)
        
    def get_hlength(body):
        hlength = {}
        n_row = len(body) - 2
        n_col = len(body[0]) - 2
        for j in range(1,n_col+1):
            for i in range(1,n_row+1):
                if body[i,j] == 1:
                    key = (i-1, j-1)
                    if body[i-1,j] == 0:
                        hlen = 0
                        while body[i,j] != 0:
                            hlen += 1
                            i += 1
                        if hlen > 1:
                            hlength[key] = hlen
        return (hlength)
    
    def random_fill(skeleton):
        s = skeleton
        for i in range(len(s)):
            for j in range(len(s[0])):
                if s[i,j] == 1:
                    x = random.randint(65,90)
                    s[i,j] = x
        return s
    
    def get_wordlist(s, wlength, hlength):
        word_list = {}
        for key in wlength:
            i, j = key
            word = []
            for l in range(wlength[key]):
                word.append(chr(s[i,j]))
                j += 1
            word = ''.join(word)
            wkey = (key, 0)
            word_list[wkey] = [word, wlength[key]]
        for key in hlength:
            i, j = key
            word = []
            for l in range(hlength[key]):
                word.append(chr(s[i,j]))
                i += 1
            word = ''.join(word)
            wkey = (key, 1)
            word_list[wkey] = [word, hlength[key]]
        return (word_list)
    
    def compute_fitness(word_list):
        import dictionary
        penalty = 0
        for wkey in word_list:
            word = word_list[wkey][0]
            if word not in dictionary:
                penalty += 1
        return (penalty)
    
    def genes(self):
        body = self.skeleton
        a = np.zeros((1, len(body[0])))
        body = np.concatenate((a, body, a), axis=0)
        b = np.zeros((len(body),1))
        body = np.concatenate((b, body, b), axis=1)
        
        



  
s = np.asarray(skeleton())
n_row = len(s)
n_col = len(s[0])

m = s
a = np.zeros((1, len(m[0])))
m = np.concatenate((a, m, a), axis=0)
b = np.zeros((len(m),1))
m = np.concatenate((b, m, b), axis=1)

# get position, direction, word_length

wlength = {}
hlength = {}
# check accross (code=0)
for i in range(1,n_row+1):
    for j in range(1,n_col+1):
        if m[i,j] == 1:
            key = (i-1, j-1)
            if m[i,j-1] == 0:
                wlen = 0
                while m[i,j] != 0:
                    wlen += 1
                    j += 1
                if wlen > 1:
                    wlength[key] = wlen

for j in range(1,n_col+1):
    for i in range(1,n_row+1):
        if m[i,j] == 1:
            key = (i-1, j-1)
            if m[i-1,j] == 0:
                hlen = 0
                while m[i,j] != 0:
                    hlen += 1
                    i += 1
                if hlen > 1:
                    hlength[key] = hlen                

for i in range(n_row):
    for j in range(n_col):
        if s[i,j] == 1:
            x = random.randint(65,90)
            s[i,j] = x


# get words
word_list = {}

for key in wlength:
    i, j = key
    word = []
    for l in range(wlength[key]):
        word.append(chr(s[i,j]))
        j += 1
    word = ''.join(word)
    wkey = (key, 0, wlength[key])
    word_list[wkey] = [word]
    
for key in hlength:
    i, j = key
    word = []
    for l in range(hlength[key]):
        word.append(chr(s[i,j]))
        i += 1
    word = ''.join(word)
    wkey = (key, 1, hlength[key])
    word_list[wkey] = [word]

dictionary = ['ABCD','BALADA','ANUGERAH','BERANGKAT']

# compute fitness
penalty = 0
for wkey in word_list:
    word = word_list[wkey][0]
    if word not in dictionary:
        penalty += 1


# cross-over

# update word_list

def decode_frame(s, word_list):
    for key, _ in word_list.items():
        word = []
        i,j = key[0]
        if key[1] == 0:
            for l in range(key[2]):
                word.append(chr(s[i,j]))
                j += 1
        elif key[1] == 1:
            for l in range(key[2]):
                word.append(chr(s[i,j]))
                i += 1
        word = ''.join(word)
        word_list[key] = word
    return word_list
                


def update_wordlist(s, word_list, key, new_word):
    word_list[key] = new_word
    i,j = key[0]
    for l in range(len(new_word)):
        s[i,j] = ord(new_word[l])
        if key[1] == 0:
            j += 1
        elif key[1] == 1:
    new_word_list = decode_frame(s, word_list)
    return s, new_word_list



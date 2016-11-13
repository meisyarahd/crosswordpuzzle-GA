# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 09:47:28 2016

@author: meisyarah
"""

import numpy as np
import random

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
    

#class Word:
#    def __init__(self, loc, type, wlength, hlength):
#        body = self.skeleton.copy()
#        a = np.zeros((1, len(body[0])))
#        body = np.concatenate((a, body, a), axis=0)
#        b = np.zeros((len(body),1))
#        body = np.concatenate((b, body, b), axis=1)
#
#        n_row = len(body) - 2
#        n_col = len(body[0]) - 2   
#        
#        wlength = {}
#        for i in range(1,n_row+1):
#            for j in range(1,n_col+1):
#                if body[i,j] == 1:
#                    loc = (i-1, j-1)
#                    if body[i,j-1] == 0:
#                        wlen = 0
#                        while body[i,j] != 0:
#                            wlen += 1
#                            j += 1
#                        if wlen > 1:
#                            wlength[loc] = wlen
#        
#        hlength = {}
#        for j in range(1,n_col+1):
#            for i in range(1,n_row+1):
#                if body[i,j] == 1:
#                    loc = (i-1, j-1)
#                    if body[i-1,j] == 0:
#                        hlen = 0
#                        while body[i,j] != 0:
#                            hlen += 1
#                            i += 1
#                        if hlen > 1:
#                            hlength[loc] = hlen    
#        for loc in wlength:
#            i, j = loc
#            key = (loc, 0, wlength[loc])
#            word_list[loc] = None
#        for key in hlength:
#            i, j = key
#            key = (loc, 1, hlength[loc])
#            word_list[loc] = None

class Individual:
    
    def __init__(self, skeleton, grid=[], word_list={}, fitness=0):
        self.skeleton = skeleton
        self.grid = grid
        self.word_list = word_list
        self.fitness = fitness
        
    def init_wordlist(self):
        body = self.skeleton.copy()
        a = np.zeros((1, len(body[0])))
        body = np.concatenate((a, body, a), axis=0)
        b = np.zeros((len(body),1))
        body = np.concatenate((b, body, b), axis=1)
    
        n_row = len(body) - 2
        n_col = len(body[0]) - 2   
        
        wlength = {}
        for i in range(1,n_row+1):
            for j in range(1,n_col+1):
                if body[i,j] == 1:
                    loc = (i-1, j-1)
                    if body[i,j-1] == 0:
                        wlen = 0
                        while body[i,j] != 0:
                            wlen += 1
                            j += 1
                        if wlen > 1:
                            wlength[loc] = wlen
        
        hlength = {}
        for j in range(1,n_col+1):
            for i in range(1,n_row+1):
                if body[i,j] == 1:
                    loc = (i-1, j-1)
                    if body[i-1,j] == 0:
                        hlen = 0
                        while body[i,j] != 0:
                            hlen += 1
                            i += 1
                        if hlen > 1:
                            hlength[loc] = hlen    
        self.word_list = {}
        for loc in wlength:
            i, j = loc
            key = (loc, 0, wlength[loc])
            self.word_list[key] = None        
        for loc in hlength:
            i, j = loc
            key = (loc, 1, hlength[loc])
            self.word_list[key] = None
            
        self.word_list = self.decode_grid()
        return self.word_list
    
    def init_grid(self):
        self.grid = self.skeleton.copy()
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i,j] == 1:
                    self.grid[i,j] = random.randint(65,90)
        return self.grid
    
    def decode_grid(self):
        for key, _ in self.word_list.items():
            word = []
            i,j = key[0]
            if key[1] == 0:
                for l in range(key[2]):
                    word.append(chr(self.grid[i,j]))
                    j += 1
            elif key[1] == 1:
                for l in range(key[2]):
                    word.append(chr(self.grid[i,j]))
                    i += 1
            word = ''.join(word)
            self.word_list[key] = word
        return self.word_list        
    
    def update_wordlist(self, key, new_word):
        self.word_list[key] = new_word
        i,j = key[0]
        for l in range(len(new_word)):
            self.grid[i,j] = ord(new_word[l])
            if key[1] == 0:
                j += 1
            elif key[1] == 1:
                i += 1
        self.word_list = self.decode_grid()
        return self.grid, self.word_list
        
    def compute_fitness(self):
    #    import dictionary
        dictionary = ['BALA','SAYA','AWSHFGY','DNEIAKWIHFE','AWUE','NSAUEB']
        penalty = 0
        for key in self.word_list:
            word = self.word_list[key]
            if word not in dictionary:
                penalty += 1
        self.fitness = 1/(penalty + 0.00000000001)
        return self.fitness

# config

n_individual = 10
n_population = 10
n_generation = 10
p_c = 1
p_m = 0.3

s = skeleton()

# generate population
population = []
for i in range(n_individual):
    x = Individual(s, grid=init_grid(s), word_list=init_wordlist(s))
    x.word_list = x.decode_grid()
    x.fitness = x.compute_fitness()
    population.append(x)

# cross-over

n_parent = int(p_c* n_individual)
population.sort(key=lambda x: x.fitness, reverse=True)

parent = population[:n_parent]

def crossover(parent_1, parent_2):
    import copy
    offs_1 = copy.deepcopy(parent_1)
    offs_2 = copy.deepcopy(parent_2)
    a = random.randint(1,len(parent_1.word_list))
    b = random.randint(1,len(parent_2.word_list))
    idx = list(population[0].word_list.keys())
    key_1 = idx[a]
    key_2 = idx[b]
    word_1 = offs_1.word_list[key_1]
    word_2 = offs_2.word_list[key_2]
    offs_1.wordlist = offs_1.update_wordlist(key_2, word_2)
    offs_2.wordlist = offs_2.update_wordlist(key_1, word_1)
    offs_1.fitness = offs_1.compute_fitness()
    offs_2.fitness = offs_2.compute_fitness()
    return offs_1, offs_2

offs = []
for i in range(0,n_parent,2):
    parent_1 = parent[i]
    parent_2 = parent[i+1]
    offs_1, offs_2 = crossover(parent_1, parent_2)
    offs.append(offs_1)
    offs.append(offs_2)
    
n_mutation = int(p_m*n_individual*len(population[0].word_list))





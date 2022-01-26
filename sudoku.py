# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 20:16:19 2022

@author: evane
"""

def get_num_of_matrix(diff_lvl):
    diff_lvl = "easy"
    way = open(diff_lvl + ".txt","r")
    data = way.read()
    way.close()
    return data[-4]
#print(get_num_of_matrix(x))

def get_random_number(num_easy_matrix):
    num_easy_matrix = 3
    import random as rand
    return rand.randrange(1, num_easy_matrix)
#print(get_random_number(num_easy_matrix))

def get_matrix(matrix_id):
    matrix_id = "3"
    diff_lvl= "easy" 
    way = open(diff_lvl + ".txt","r")
    data = way.read()
    return data[data.find("%%%" + str(int(matrix_id) -1 ) + "%%%") + 7 : data.find("%%%" + matrix_id + "%%%")]
#print(get_matrix(2))

def pre_matrix_to_matrix():
    pre_matrix = get_matrix(2)  #tirar do código e acrescentar pre_matrix no argumento. 
    matrix = []
    for ele in pre_matrix[:len(pre_matrix)-1]:
        if ele == "\n":
            matrix.append([])
        elif ele != ",":
            matrix[len(matrix)-1].append(int(ele))
    return matrix
            
            
#!/usr/bin/env python3
from sys import stdin
import math

var_qtd = {}

def sort_func(elem):
    return abs(int(elem))

def verificator(claus, vars_atual):
    claus_false = []

    for i, x in enumerate(claus):
        bool_claus = [(literal, Tru) for literal in x]

        # a clausula é falsa
        if not any(x):
            # adiciona o indice da clausula em uma lista
            claus_false.append(i)
            for y in x:
                # soma mais um no dict para poder ordenar depois no lits
                var_qtd.update(y+=1)
    
    if len(claus_false) == 0:
        print("SAT")

            
    
    

Var, Claus = input().split()
Var = int(Var)
Claus = int(Claus)

all_var = {x:True if x>0 else False for x in range(-Var,Var+1) }

list_claus = [[]] * Claus

# inserindo as clausulas em uma lista
for x in range(Claus):
    var_atuais = input().split()
    # vou simplesmente inserir em True e False na ordem que o usuário inserir
    # var_atuais = sorted(var_atuais, key=sort_func)
    for y in enumerate(var_atuais):
        if y[1] == 0:
            continue
        # inicializa a quantidade em zero para ordenar no lits
        var_qtd.update({y[1]:0})
 
        # cria uma lista de como foi escrito no input
        var_atuais[y[0]] = y[1]
    list_claus[x].append(var_atuais)

#list_var = [0] * Var
# decidi que um dict é melhor
dict_var = {}
for line in stdin:

    cmd, *val = line.split()
    print('cmd', cmd)
    print('val', val)

    if cmd == "full":
        for x in val: # enumerate(val):
            i = int(x)
            dict_var.update({i : all_var[i]})
        print(dict_var)

    elif cmd == 'flip':
        i = int(val[0])
        print("valor i:", i)
        #dict_var[abs(i) - 1] = not dict_var[abs(i) - 1]

        # retira o que tinha no dicionário e depois reinsere com valor e indice trocado
        pos = dict_var.pop(i, math.inf)
        neg = dict_var.pop(-i, math.inf)
        dic_value = not min(pos, neg)
        dict_var.update({ i if dic_value else -i : dic_value } )

        print(dict_var)
        print('')

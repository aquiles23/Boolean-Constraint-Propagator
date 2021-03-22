#!/usr/bin/env python3
from sys import stdin
import math



def sort_func(elem):
    return abs(int(elem))

def verificator(claus: list, vars_atual : dict, var_qtd: dict):
    claus_false = []
    qtd_false = 0
    for i, x in enumerate(claus):
        bool_claus = [
            vars_atual[key] if x[key]>0 else not vars_atual[key] 
            for key in vars_atual
        ]

        # a clausula é falsa
        if not any(bool_claus):
            # adiciona o indice da clausula em uma lista
            claus_false.append(i)
            qtd_false += 1
            for y in x:
                # soma mais um no dict para poder ordenar depois no lits
                var_qtd[y] += 1
    if len(claus_false) == 0:
        print("SAT")
    else:
        print(f"[{qtd_false} clausulas falsas] ",end="")
        print(*claus_false, sep=" ")
        print(f"[lits] ",end="")
        lvar_qtd = sorted(var_qtd, key= lambda x: var_qtd[x], reverse=True)
        print(*lvar_qtd, sep=" ")
    
    

Var, Claus = input().split()
Var = int(Var)
Claus = int(Claus)

var_qtd = {}
all_var = {x:True if x>0 else False for x in range(-Var,Var+1) }

list_claus = []

# inserindo as clausulas em uma lista
for x in range(Claus):
    inp = input().split()
    var_atuais = []
    # var_atuais = sorted(var_atuais, key=sort_func)
    for y in enumerate(inp):
        if y[1] == '0':
            break
        # inicializa a quantidade em zero para ordenar no lits
        var_qtd.update({int(y[1]):0})
 
        # cria uma lista de como foi escrito no input
        var_atuais.append(int(y[1]))
    list_claus.append(var_atuais)
print(list_claus)
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
        # print(dict_var)

        verificator(list_claus, dict_var, var_qtd)
        # var_qtd = dict.fromkeys(var_qtd, 0)

    elif cmd == 'flip':
        i = int(val[0])
        print("valor i:", i)
        #dict_var[abs(i) - 1] = not dict_var[abs(i) - 1]

        # retira o que tinha no dicionário e depois reinsere com valor e indice trocado
        pos = dict_var.pop(i, math.inf)
        neg = dict_var.pop(-i, math.inf)
        dic_value = not min(pos, neg)
        dict_var.update({ i if dic_value else -i : dic_value } )
        verificator(list_claus, dict_var, var_qtd)

        #zera a contagem
        # var_qtd = dict.fromkeys(var_qtd, 0)

        # print(dict_var)
        # print('')

#!/usr/bin/env python3
import sys
import math
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import multiprocessing as mp
import psutil as ps
import os

queue = mp.Queue()
queue_lock = mp.Lock()

def verificator(claus: list, var_qtd : dict):
    claus_false = []
    this_var_qtd = var_qtd.copy()
    parent = ps.Process(os.getppid())
    #print(f"var_atuais:  {vars_atual}")
    # print(f"clausulas {claus}")
    while not queue.empty() or True:
        queue_lock.acquire()
        try:
            vars_atual = queue.get(timeout=1)
        except:
            queue_lock.release()
            break
        queue_lock.release()

        qtd_false = 0
        for i, x in enumerate(claus):
            #list compreension
            # print("clausula atual:", x)

            bool_claus = []
            for y in x:
                # retirar um for otimizou bastante o algoritmo
                if abs(y) in vars_atual:
                    if y>0:
                        bool_claus.append(vars_atual[abs(y)])
                    else:
                        bool_claus.append(not vars_atual[abs(y)])
                elif y in vars_atual:
                    if y>0:
                        bool_claus.append(vars_atual[y])
                    else:
                        bool_claus.append(not vars_atual[y])


            # a clausula é falsa
            if not any(bool_claus):
                # adiciona o indice da clausula em uma lista
                claus_false.append(i)
                qtd_false += 1
                for y in x:
                    # soma mais um no dict para poder ordenar depois no lits
                    this_var_qtd[y] += 1
        if not claus_false:
            print("SAT")
        else:
            print(f"[{qtd_false} clausulas falsas] ",end="")
            print(*claus_false)
            print(f"[lits] ",end="")
            lvar_qtd = list(filter(lambda x: this_var_qtd[x] != 0,this_var_qtd))

            lvar_qtd = sorted(lvar_qtd, key= lambda x: (this_var_qtd[x], abs(x)) , reverse=True)
            print(*lvar_qtd)
        bool_claus.clear()
        this_var_qtd = var_qtd.copy()
        claus_false.clear()
    return "xablau"

def producer(all_var: dict):
    dict_var = {}
    for line in sys.stdin:

        cmd, *val = line.split()
        #print('cmd', cmd)
        #print('val', val)

        if cmd == "full":
            # para usar o full mais de uma vez tem que limpar o dicionário
            dict_var.clear()
            for x in val: # enumerate(val):
                i = int(x)
                dict_var.update({i : all_var[i]})
            # print(dict_var)
            
            # aqui coloca na fila ao invés de chamar a função
            # verificator(list_claus, dict_var, var_qtd)
            
            queue.put_nowait(dict_var)

            #zera a contagm
            # var_qtd = dict.fromkeys(var_qtd, 0)

        elif cmd == 'flip':
            i = int(val[0])
            #print("valor i:", i)
            #dict_var[abs(i) - 1] = not dict_var[abs(i) - 1]

            # retira o que tinha no dicionário e depois reinsere com valor e indice trocado
            pos = dict_var.pop(i, math.inf)
            neg = dict_var.pop(-i, math.inf)
            dic_value = not min(pos, neg)
            dict_var.update({ i if dic_value else -i : dic_value } )
            
            # aqui coloca na fila ao invés de chamar a função
            # verificator(list_claus, dict_var, var_qtd)
            queue.put_nowait(dict_var)
            #zera a contagem
            # var_qtd = dict.fromkeys(var_qtd, 0)

            # print(dict_var)
            # print('')
    return 'tred_return'

def main():
    num_cores = mp.cpu_count() if len(sys.argv) <= 1 else int(sys.argv[1])
    Var, Claus = input().split()
    Var = int(Var)
    Claus = int(Claus)

    var_qtd = {}
    #dict compreension
    all_var = {x: x>0 for x in range(-Var,Var+1)}

    list_claus = []

    # inserindo as clausulas em uma lista
    for _ in range(Claus):
        inp = input().split()
        var_atuais = []
        # var_atuais = sorted(var_atuais, key=sort_func)
        for y in inp:
            if y == '0':
                break
            # inicializa a quantidade em zero para ordenar no lits
            var_qtd.update({int(y):0})

            # cria uma lista de como foi escrito no input
            var_atuais.append(int(y))
        list_claus.append(var_atuais)

    with ThreadPoolExecutor() as TExecutor:
        tred = TExecutor.submit(producer, all_var)
        with ProcessPoolExecutor(max_workers=num_cores) as PExecutor:
            for i in range(num_cores):
                proc = PExecutor.submit(verificator, list_claus, var_qtd)
        print(proc.result(), tred.result())

if __name__ == '__main__':
    main()
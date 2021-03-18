from sys import stdin

Var, Claus = input().split()
Var = int(Var)
Claus = int(Claus)

dict_var = {x:True if x>0 else False for x in range(-Var,Var+1) }

list_claus = [[]] * Claus

# inserindo as clausulas em uma lista
for x in range(Claus):
    var_atuais = input().split()
    for y in enumerate(var_atuais):
        if y[1] == 0:
            continue
        var_atuais[y[0]] = int(y[1])
    list_claus[x].append(var_atuais)

def fullFlip(cmd,*var):
    list_var = [0] * Var
    if cmd == "full":
        for x in enumerate(var):
            list_var[x[0]] = list_var[dict_var[x[1]]]


        
    

for line in stdin:f
    cmd, *val = line.split()







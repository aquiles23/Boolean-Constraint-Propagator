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

for line in stdin:
    """print(line, end='')"""
    cmd, *val = line.split()
    print('cmd', cmd)
    print('val', val)

    if cmd == 'full':
        for x in val:
            i = int(x)
            if i > 0:
                dict_var[abs(i)] = True
            elif i < 0:
                dict_var[abs(i)] = False
        print(dict_var)
        print('')

    elif cmd == 'flip':
        i = int(val[0])
        if dict_var[abs(i)] == False:
            dict_var[abs(i)] = True
        else:
            dict_var[abs(i)] = False

        print(dict_var)
        print('')


for line in stdin:f
    cmd, *val = line.split()
    list_var = [0] * Var
    if cmd == "full":
        for x in enumerate(var):
            list_var[x[0]] = dict_var[x[1]]






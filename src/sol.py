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

list_var = [0] * Var
for line in stdin:
    """print(line, end='')"""
    cmd, *val = line.split()
    print('cmd', cmd)
    print('val', val)

    
    if cmd == "full":
        for x in enumerate(val):
            list_var[x[0]] = dict_var[int(x[1])]
        print(list_var)

    elif cmd == 'flip':
        i = int(val[0])
        print("valor i:", i)
        list_var[abs(i) - 1] = not list_var[abs(i) - 1]

        print(list_var)
        print('')

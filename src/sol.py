from sys import stdin

Var, Claus = input().split()
Var = int(Var)
Claus = int(Claus)

dict_var = {x:True for x in range(1,Var+1) }
list_claus = [[]] * Claus

for x in range(Claus):
    var_atuais = input().split()
    for y in enumerate(var_atuais):
        var_atuais[y[0]] = int(y[1])
    print(var_atuais)
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


    
"""     primeiro = True
    
    var_atual = int(input())
    while var_atual : 
        if(not primeiro):
            var_atual = int(input())
        list_claus[x].append(var_atual)
        primeiro = False """



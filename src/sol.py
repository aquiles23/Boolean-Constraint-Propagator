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


    
"""     primeiro = True
    
    var_atual = int(input())
    while var_atual : 
        if(not primeiro):
            var_atual = int(input())
        list_claus[x].append(var_atual)
        primeiro = False """



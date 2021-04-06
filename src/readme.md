## requisitos

python3
pip install psutil

## para executar a solução sequencial

```
./sol.py
```
ou para usar um arquivo de input

```
./sol.py < ../input/flat75-90
```

## para executar a solução paralela

```
./sol_paralelo.py num_cores
```

onde `num_cores` é o numero de processos simultaneos que deseja rodar.

para usar um arquivo de input
```
./sol_paralelo.py num_cores < ../input/flat75-90
```
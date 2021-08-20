import numpy as np
import csv
import sys
import time

if len(sys.argv) >= 3:
    path_actions_csv = sys.argv[1]
    max_invest = int(sys.argv[2])
else:
    raise Exception('Paramètres manquant. commande : python optimized.py <Lien fichier csv> <investissement maximum>')


class Action:
    def __init__(self, name, cost, perform):
        self.name = name
        self.cost = float(cost)
        self.perform = float(perform)/100

    def __str__(self):
        return self.name+' '+str(self.cost)+' '+str(self.perform)+' '+str(self.cost*self.perform)


def knapsack_01(actions, max_w):
    m = np.zeros(shape=(len(actions) + 1, max_w+1))
    w = [0, *[int(ac.cost)+1 for ac in actions]]
    v = [0, *[ac.cost * ac.perform for ac in actions]]

    for i in range(1,len(actions)+1):
        for j in range(max_w+1):
            if w[i] > j:
                m[i,j] = m[i-1, j]
            else:
                m[i,j] = max(m[i-1,j],m[i-1,j-w[i]]+v[i])

    seq = []
    while i != 0:
        if m[i, j] > m[i - 1, j]:
            seq.append(actions[i - 1])
            j = j - w[i]
        i = i - 1
    return seq


actions = []
with open(path_actions_csv, newline='') as file:
    reader = list(csv.reader(file))
    for row in reader[1:]:
        if float(row[1]) <= 0 or float(row[2]) <= 0:
            pass
        else:
            actions.append(Action(row[0], row[1], row[2]))

actions.sort(key = lambda ac : ac.cost, reverse=True)

t1 = time.time()
seq = knapsack_01(actions, max_invest)
t2 = time.time() - t1
print('Meilleur sequence : ')
for ac in seq:
    print('-',ac)
print('Total investissement : ', sum([ac.cost for ac in seq]))
print('Espérance : ', sum([ac.cost*ac.perform for ac in seq]))
print("Temps d'exécution : ", t2)
import itertools
import time
import sys
import csv


if len(sys.argv) >= 3:
    path_actions_csv = sys.argv[1]
    max_invest = float(sys.argv[2])
else:
    raise Exception('Paramètres manquant. commande : python brute_force.py <Lien fichier csv> <investissement maximum>')


class Action:
    def __init__(self, name, cost, perform):
        self.name = name
        self.cost = cost
        self.perform = perform

    def __str__(self):
        return self.name + ' ' + str(self.cost) + ' ' + str(self.perform)


with open(path_actions_csv) as csvfile:
    reader = csv.DictReader(csvfile)
    actions = []
    for row in reader:
        actions.append(Action(row['name'], float(row['price']), float(row['profit'])))


def filter_sequence(actions, seq_actions):
    sum_cost = sum([ac.cost for ac in seq_actions])
    if sum_cost > max_invest:
        return False
    for ac in actions:
        if ac not in seq_actions and sum_cost+ac.cost <= max_invest:
            return False
    return True


t1 = time.time()
sequence = []
performance = 0
for k in range(1,len(actions)+1):
    for seq in itertools.combinations(actions, k):
        if filter_sequence(actions, seq) and sum([ac.cost*ac.perform for ac in seq]) > performance:
            sequence = seq
            performance = sum([ac.cost*ac.perform for ac in seq])

print('Meilleur séquence : ')
for ac in sequence:
    print('-',ac)
print('Total investissement : ', sum([ac.cost for ac in sequence]) )
print('Espérance : ', sum([ac.cost*ac.perform for ac in sequence]))
print("Temps d'exécution : ", time.time()-t1)
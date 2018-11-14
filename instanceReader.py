from pathlib import Path
from os import listdir
import Knapsack as K

folder = Path('./Instancias/')
instances = [folder/fileName for fileName in listdir(folder)]

def readInstance( fileName, values: list, weights: list ):    
    with open(fileName,'r') as f:
        nElements, sackSize = f.readline().strip().split()
        for line in f:
            v_i,w_i = line.strip().split()
            values += [int(v_i)]
            weights += [int(w_i)]
    return int(nElements), int(sackSize)


for instancia in instances:
    weights = []
    values = []
    n,w = readInstance(instancia,values,weights)
    problem = K.KnapSack(n,10,w,values,weights)
    solution = problem.solve()
    print('Solucao problema '+str(instancia).split()[-1], solution)

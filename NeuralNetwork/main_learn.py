import numpy as np
import time
import csv
from scipy import optimize

import neural_network as nn

neural_network = nn.NeuralNetwork(21, 10, 1)

Y = []
X = []
with open('data.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter=";")
    for row in csvReader:
        if row[0] == "input":
            continue
        row = [value.replace(",", ".") for value in row]
        Y.append(row[0])
        X.append(row[1:])
Y = np.array(Y).astype(float)
Y = Y * 0.5 + 0.5
X = np.array(X).astype(float)

initial_nn_params = neural_network.randInitializeWeights()
options = {'maxiter': 100}
lambda_ = 1


def costFunction(nn_params): return neural_network.costfunction(
    nn_params, X, Y, lambda_)


res = optimize.minimize(costFunction,
                        initial_nn_params,
                        jac=True,
                        method='TNC',
                        options=options)

# get the solution of the optimization
nn_params = res.x
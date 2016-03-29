# coding=utf8

import math
import numpy as np
import operator

from itertools import groupby
from joblib import Parallel, delayed

def distance_euclidian(a, b, length):
    """
    Calcula a distância eucliana entre dois pontos de dimensões arbritárias.
    a e b devem ser dois vetores do python.
    """
    total = 0

    # for i in range(length):
    #     total += (a[i] - b[i]) * (a[i] - b[i])

    difference = np.subtract(a, b)
    difference_squared = np.square(difference)
    total = np.sum(difference_squared)

    return math.sqrt(total)

def voting_majority(labels):
    """
    Determina o rótulo final por voto de maioria
    Y é um vetor de rótulos
    """
    votes = dict()
    for i in range(len(labels)):
        label = labels[i]
        if label in votes:
            votes[label] += 1
        else:
            votes[label] = 1

    sorted_votes = sorted(votes.items(), key=operator.itemgetter(1))
    return sorted_votes[len(sorted_votes)-1][0]

class KNN:
    def __init__(self, k=3, distance = distance_euclidian, voting = voting_majority):
        """
        Inicialização padrão com k=3, função de distância euclidiana e função
        de voto por maioria
        """
        self.distance = distance
        self.voting = voting
        self.k = k

    def neighbors(self, X):
        """
        Retorna os rótulos dos k vizinhos
        """
        # distances = []

        # percorre a base de treinamento calculando as distâncias
        # for i in range(0, self.n_training_samples, 1):
        #     dist = self.distance(X, self.Xtrain[i], self.n_features)
        #     distances.append((dist, self.ytrain[i]))

        # distances = [((self.distance(X, self.Xtrain[i], self.n_features), self.ytrain[i])) for i in range(self.n_training_samples)]
        distances = Parallel(n_jobs=4)(delayed(self.distance)(X, self.Xtrain[i], self.n_features) for i in range(self.n_training_samples))
        distances = zip(distances, self.ytrain)

        # ordena o vetor de distâncias
        sorted_distances = sorted(distances, key=lambda x: x[0])

        k_labels = [x[1] for x in sorted_distances[0:self.k]]

        print k_labels

        # retorna as k menores distâncias
        return k_labels

    def fit(self, X, y):
        """
        Treina o modelo com uma base de treinamento
        """
        self.Xtrain = np.array(X)
        self.ytrain = np.array(y)
        # define o número de características e de amostras de treinamento
        # a partir de Xtrain
        self.n_features = len(X[0])
        self.n_training_samples = len(self.Xtrain)

    def predict(self, Xtest):
        """
        Classifica instâncias
        """
        ytest = []
        # itera sobre a base de testes
        for i in range(0, len(Xtest), 1):
            print "instance %d" % i
            k_neighbors = self.neighbors(Xtest[i])
            label = self.voting(k_neighbors)
            ytest.append(label)
            print "label: %d" % label
        return ytest

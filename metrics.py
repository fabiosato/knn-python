import numpy as np

def confusion_matrix(Ytest, Ypred):
    labels = np.unique(Ytest)
    n_labels = len(labels)
    matrix = np.zeros((n_labels, n_labels))
    
    for i in range(len(Ytest)):
        matrix[Ytest][Ypred] += 1

    return matrix

def print_confusion_matrix(matrix):
    n_labels = len(matrix)
    for i in range(n_labels):
        line = ''
        for j in range(n_labels):
            line += matrix[i][j]
            line += '\t'
        print line

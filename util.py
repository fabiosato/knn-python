import numpy as np

def load_data(filename):
    X = []
    Y = []

    myfile = open(filename, 'r')
    header = myfile.readline()
    (n_samples, n_features) = header.split(" ")
    print int(n_samples)
    print int(n_features)

    for i in range(int(n_samples)):
        line = myfile.readline()
        columns = [float(s) for s in line.split(" ")]
        x = columns[0:len(columns)-1]
        y = int(columns[-1])
        X.append(x)
        Y.append(y)

    myfile.close()

    return (X, Y)

# def confusion_matrix(Ytest, Ypred):
#     labels = np.unique(Ytest)
#     n_labels = len(labels)
#     matrix = np.zeros((n_labels, n_labels))
#
#     for i in range(len(Ytest)):

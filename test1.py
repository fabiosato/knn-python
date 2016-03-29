import knn
import util
import pickle

print "Carregando base de treinamento"
(Xtrain, Ytrain) = util.load_data('CCtrain')

print "Carregando base de testes 1"
(Xtest, Ytest) = util.load_data('CCtest1')

knn1 = knn.KNN()

knn1.fit(Xtrain, Ytrain)

print "Classificando base de testes"
Ypred = knn1.predict(Xtest)

print "Classificacao obtida"
print Ypred

print "Salvando resultados"
pickle.dump(Ypred, open('CCpred1.pickle', 'w'))

import knn
import util
import pickle

print "Carregando base de treinamento"
(Xtrain, Ytrain) = util.load_data('CCtrain')

print "Carregando base de testes 2"
(Xtest, Ytest) = util.load_data('CCtest2')

knn2 = knn.KNN()

knn2.fit(Xtrain, Ytrain)

print "Classificando base de testes"
Ypred = knn2.predict(Xtest)

print "Classificacao obtida"
print Ypred

print "Salvando resultados"
pickle.dump(Ypred, open('CCpred2.pickle', 'w'))

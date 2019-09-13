import sklearn.datasets as ds
mnist = ds.fetch_mldata('MNIST original',data_home='./mnist/')

import numpy as np
sample = np.random.randint(70000, size=5000)
data = mnist.data[sample]
target = mnist.target[sample]
print(len(data))

import sklearn.model_selection as ms
xtrain, xtest, ytrain, ytest = ms.train_test_split(data, target, train_size=0.8, test_size=0.2)

import sklearn.neighbors as nn
model = nn.KNeighborsClassifier(n_neighbors=3)
model.fit(xtrain, ytrain)
error = model.score(xtest, ytest)
print('Erreur: %f' % error)

score = []
for k in range(2,15):
    model = nn.KNeighborsClassifier(k)
    score.append(model.fit(xtrain, ytrain).score(xtest, ytest))
import matplotlib.pyplot as plt
plt.plot(range(2,15), score, 'o-')
plt.show()

min_nn = score.index(max(score)) + 2
print("min_nn: "+str(min_nn))

model = nn.KNeighborsClassifier(n_neighbors=min_nn)
model.fit(xtrain, ytrain)
error = model.score(xtest, ytest)
print('Erreur: %f' % error)

# On récupère le classifieur le plus performant
model = nn.KNeighborsClassifier(min_nn)
model.fit(xtrain, ytrain)

# On récupère les prédictions sur les données test
predicted = model.predict(xtest)

# On redimensionne les données sous forme d'images
images = xtest.reshape((-1, 28, 28))

# On selectionne un echantillon de 12 images au hasard
select = np.random.randint(images.shape[0], size=12)

# On affiche les images avec la prédiction associée
for index, value in enumerate(select):
    plt.subplot(3,4,index+1)
    plt.axis('off')
    plt.imshow(images[value],cmap=plt.cm.gray_r,interpolation="nearest")
    plt.title('Predicted: %i' % predicted[value])

plt.show()

# Gestion des erreurs
# on récupère les données mal prédites
misclass = (ytest != predicted)
misclass_images = images[misclass,:,:]
misclass_predicted = predicted[misclass]

# on sélectionne un échantillon de ces images
select = np.random.randint(misclass_images.shape[0], size=12)

# on affiche les images et les prédictions (erronées) associées à ces images
for index, value in enumerate(select):
    plt.subplot(3,4,index+1)
    plt.axis('off')
    plt.imshow(misclass_images[value],cmap=plt.cm.gray_r,interpolation="nearest")
    plt.title('Predicted: %i' % misclass_predicted[value])

plt.show()

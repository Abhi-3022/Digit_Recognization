# -*- coding: utf-8 -*-
"""DigitRecognization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11LrKHm1Kd4KASIq4REdbywBPcbS2oksi
"""

from sklearn.datasets import load_digits
digits_dataset = load_digits()
print('Keys of Digit dataset {}'.format(digits_dataset.keys()))
data = digits_dataset.data
target = digits_dataset.target

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(data,target,test_size = 0.25,random_state = 0)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train,y_train)
KNeighborsClassifier(knn)
y_pred = knn.predict(x_test)

print(digits_dataset.data.shape)
import matplotlib.pyplot as plt
plt.gray()
plt.matshow(digits_dataset.images[1796])
plt.show()



import sklearn.metrics as metrics
print("Accuracy of the Test Data \n {}".format(metrics.accuracy_score(y_test,y_pred)))
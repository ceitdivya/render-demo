import pandas as pd
import numpy as np
import joblib

df = pd.read_csv('Iris.csv')

X = np.array(df.iloc[:, 1:5])
y = np.array(df.iloc[:, 5:])

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y.reshape(-1))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.svm import SVC
sv = SVC(kernel='linear').fit(X_train,y_train)

joblib.dump(sv, 'iri.joblib')

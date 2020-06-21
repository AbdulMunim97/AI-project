from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import RidgeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
import pandas as pd
import numpy as np

def mlPreddict(label):
    df = pd.read_csv('classification.csv')
    df_names = df
    Xfeatures = df_names['Names']
    cv = CountVectorizer()
    x = cv.fit_transform(Xfeatures)
    y = df_names.Classes
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=12)

    knn = KNeighborsClassifier(n_neighbors=158)
    r_c = RidgeClassifier()
    m_nb = MultinomialNB()
    dt_c = DecisionTreeClassifier()
    svm_c = svm.SVC()

    knn.fit(x_train, y_train)
    r_c.fit(x_train, y_train)
    m_nb.fit(x_train, y_train)
    dt_c.fit(x_train, y_train)
    svm_c.fit(x_train, y_train)

    knn.score(x_test, y_test)
    r_c.score(x_test, y_test)
    m_nb.score(x_test, y_test)
    dt_c.score(x_test, y_test)
    svm_c.score(x_test, y_test)

    sample_name = [label]
    vect = cv.transform(sample_name).toarray()

    prediction = svm_c.predict(vect)
    predict = ''.join(map(str, prediction))
    print(predict)

    return predict

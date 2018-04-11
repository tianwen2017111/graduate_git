# coding=utf-8
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
import numpy as np
import cross_val

def f_measure(testy, prdty):
    prediction = 0
    key = 0
    max = 0.0
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for i in range(len(prdty)):
        if testy[i] > max:
            max = testy[i]
    for i in range(len(prdty)):
        if prdty[i] == 1.0:
            key = i
        if max == testy[i]:
            prediction = i
    if prediction == key:
        for i in range(len(prdty)):
            if i == prediction:
                TP = TP + 1
            else:
                TN = TN + 1
    else:
        for i in range(len(prdty)):
            if i == prediction:
                FP = FP + 1
            elif i == key:
                FN = FN + 1
            else:
                TN = TN + 1
    Precision = (TP + TN)/(TP + TN + FP + FN)
    Recall = TP/(TP + FN)
    # f_m = (2*TP/(TP+FP)*Recall)/(TP/(TP+FP)+Recall)
    # return Precision,Recall,f_m
    return Precision,Recall

def loadDataSet(trainFile):
    dataMat = []
    labelMat = []
    fr = open(trainFile)
    for line in fr.readlines():
        dataSample = line.strip().split(',')
        featureSample = []
        for i in range(0,len(dataSample)):
            featureSample.append(float(dataSample[i]))
        dataMat.append(featureSample)
        labelMat.append(float(dataSample[len(dataSample)-1]))
    fr.close()
    return dataMat,labelMat

def svm_run(train_data,train_label,test_data,test_label):
    clf = svm.SVC(kernel='linear')
    clf.fit(train_data,train_label)
    predictLabel = clf.predict(test_data)
    print('predictLabel:',predictLabel.tolist(),test_label)
    Precision = metrics.accuracy_score(test_label,predictLabel)
    Recall = metrics.recall_score(test_label,predictLabel)
    print 'SVM:',Precision,Recall

def rf_run(train_data,train_label,test_data,test_label):
    clf = RandomForestClassifier(n_estimators=50, max_depth=None, min_samples_split=2, random_state=0)
    clf.fit(train_data, train_label)
    predictLabel = clf.predict(test_data)
    print('predictLabel:', predictLabel.tolist(), test_label)
    Precision = metrics.accuracy_score(test_label, predictLabel)
    Recall = metrics.recall_score(test_label, predictLabel)
    print 'Random Forest:',Precision, Recall

def knn_run(train_data,train_label,test_data,test_label):
    clf = KNeighborsClassifier(algorithm='kd_tree',n_neighbors=30)
    clf.fit(train_data, train_label)
    predictLabel = clf.predict(test_data)
    print('predictLabel:', predictLabel.tolist(), test_label)
    Precision = metrics.accuracy_score(test_label, predictLabel)
    Recall = metrics.recall_score(test_label, predictLabel)
    print 'kNN:',Precision, Recall

def bayes_run(train_data,train_label,test_data,test_label):
    clf = GaussianNB()
    clf.fit(train_data, train_label)
    predictLabel = clf.predict(test_data)
    print('predictLabel:', predictLabel.tolist(), test_label)
    Precision = metrics.accuracy_score(test_label, predictLabel)
    Recall = metrics.recall_score(test_label, predictLabel)
    print 'Naive Bayes:',Precision, Recall

if __name__ == '__main__':
    trainPath = r'Train.txt'
    testPath = r'Test.txt'
    train_data, train_label = loadDataSet(trainPath)
    test_data, test_label = loadDataSet(testPath)

    svm_run(train_data,train_label,test_data,test_label)
    rf_run(train_data,train_label,test_data,test_label)
    knn_run(train_data,train_label,test_data,test_label)
    bayes_run(train_data,train_label,test_data,test_label)



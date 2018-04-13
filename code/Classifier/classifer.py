# coding=utf-8
from sklearn import svm
from sklearn.multiclass import OneVsRestClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
import numpy as np
import os
# import file_util

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


def svm_run(train_data,train_label,test_data,test_label):
    clf = svm.LinearSVC(C=1,multi_class='ovr')
    clf.fit(train_data,train_label)
    # model = OneVsRestClassifier(svm.SVC(kernel='linear'))
    # clf = model.fit(train_data, train_label)
    predictLabel = clf.predict(test_data)
    Precision = metrics.accuracy_score(test_label,predictLabel)
    Recall = metrics.recall_score(test_label,predictLabel,average='macro')
    f = metrics.f1_score(test_label, predictLabel, average='macro')
    print 'SVM:',Precision,Recall,f

def rf_run(train_data,train_label,test_data,test_label):
    clf = RandomForestClassifier(n_estimators=50, max_depth=None, min_samples_split=2, random_state=0)
    clf.fit(train_data, train_label)
    predictLabel = clf.predict(test_data)
    # print('predictLabel:', predictLabel.tolist(), test_label)
    # file_util.write_file("predictLabel.txt", predictLabel)
    # file_util.write_file("test_label.txt", test_label)
    Precision = metrics.accuracy_score(test_label, predictLabel)
    Recall = metrics.recall_score(test_label, predictLabel, average='macro')
    f = metrics.f1_score(test_label, predictLabel, average='macro')
    print 'Random Forest:',Precision, Recall,f

def knn_run(train_data,train_label,test_data,test_label):
    clf = KNeighborsClassifier(algorithm='kd_tree',n_neighbors=30)
    clf.fit(train_data, train_label)
    predictLabel = clf.predict(test_data)
    # print('predictLabel:', predictLabel.tolist(), test_label)
    Precision = metrics.accuracy_score(test_label, predictLabel)
    Recall = metrics.recall_score(test_label, predictLabel, average='macro')
    f = metrics.f1_score(test_label, predictLabel, average='macro')

    print 'kNN:',Precision, Recall, f

def bayes_run(train_data,train_label,test_data,test_label):
    clf = GaussianNB()
    clf.fit(train_data, train_label)
    predictLabel = clf.predict(test_data)
    # print('predictLabel:', predictLabel.tolist(), test_label)
    Precision = metrics.accuracy_score(test_label, predictLabel)
    Recall = metrics.recall_score(test_label, predictLabel, average='macro')
    f = metrics.f1_score(test_label, predictLabel, average='macro')
    print 'Naive Bayes:',Precision, Recall,f

if __name__ == '__main__':
    feature_path = "feature"
    keywords = "IAT"
    filenames = file_util.find_filenames(feature_path, keywords)
    file = file_util.combine_labels(filenames, keywords,feature_path)
    data,label = loadDataSet(file)

    train_data, train_label,test_data, test_label = get_data_for_cross_validation(data,label)
    print len(train_data), len(test_data)
    svm_run(train_data,train_label,test_data,test_label)
    rf_run(train_data,train_label,test_data,test_label)
    knn_run(train_data,train_label,test_data,test_label)
    bayes_run(train_data,train_label,test_data,test_label)



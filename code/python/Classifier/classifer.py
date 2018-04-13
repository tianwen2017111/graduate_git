# coding=utf-8
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
import numpy as np
import os
from cross_val import *
from file_util import *

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

# def find_filenames(dir_path, key_word):
#     #获取包含关键字的文件名，并以列表的形式返回
#     filenames = list()
#     for root, _, files in os.walk(dir_path):
#         for file in files:
#             if key_word in file:
#                 filenames.append(file)
#     return filenames
#
# #一个文件数据数目太少怎么办
# def combine_labels(filenames,keywords,feature_path):
#     filepath = r"combine/%s.txt" %keywords
#     if os.path.exists(filepath):
#         os.remove(filepath)
#     file_keywords = open(filepath,'w+')
#     label = 0
#     for file in filenames:
#         label = label + 1
#         f = open(r"%s/%s" % (feature_path, file))
#         for line in f.readlines():
#             file_keywords.writelines(r"%d,%s" %(label,line))
#         f.close()
#     return file_keywords

def loadDataSet(trainFile):
    dataMat = []
    labelMat = []
    fr = open(trainFile.name)
    # print open(trainFile.name)
    for line in fr.readlines():
        dataSample = line.strip().split(',')
        # dataSample = line.strip().split(' ')
        featureSample = []
        labelMat.append(float(dataSample[0]))
        for i in range(1,len(dataSample)):
            featureSample.append(float(dataSample[i]))
        dataMat.append(featureSample)
    fr.close()
    return dataMat,labelMat

# def loadDataSet(trainFile):
#     dataMat = []
#     labelMat = []
#     fr = open(trainFile.name)
#     # print open(trainFile.name)
#     for c, line in enumerate(fr.readlines()):
#         dataSample = line.strip().split(',')
#         # dataSample = line.strip().split(' ')
#         featureSample = []
#         labelMat.append(c)
#         for i in range(1,len(dataSample)):
#             featureSample.append(float(dataSample[i]))
#         dataMat.append(featureSample)
#     fr.close()
#     return dataMat,labelMat


def svm_run(train_data,train_label,test_data,test_label):
    clf = svm.SVC(kernel='linear')
    clf.fit(train_data,train_label)
    predictLabel = clf.predict(test_data)
    print('predictLabel:',predictLabel.tolist(),test_label)
    Precision = metrics.accuracy_score(test_label,predictLabel)
    Recall = metrics.recall_score(test_label,predictLabel,average='macro')
    f = metrics.f1_score(test_label, predictLabel, average='macro')
    print 'SVM:',Precision,Recall,f

def rf_run(train_data,train_label,test_data,test_label):
    clf = RandomForestClassifier(n_estimators=50, max_depth=None, min_samples_split=2, random_state=0)
    clf.fit(train_data, train_label)
    predictLabel = clf.predict(test_data)
    print('predictLabel:', predictLabel.tolist(), test_label)
    Precision = metrics.accuracy_score(test_label, predictLabel)
    Recall = metrics.recall_score(test_label, predictLabel, average='macro')
    f = metrics.f1_score(test_label, predictLabel, average='macro')
    print 'Random Forest:',Precision, Recall,f

def knn_run(train_data,train_label,test_data,test_label):
    clf = KNeighborsClassifier(algorithm='kd_tree',n_neighbors=30)
    clf.fit(train_data, train_label)
    predictLabel = clf.predict(test_data)
    print('predictLabel:', predictLabel.tolist(), test_label)
    Precision = metrics.accuracy_score(test_label, predictLabel)
    Recall = metrics.recall_score(test_label, predictLabel, average='macro')
    f = metrics.f1_score(test_label, predictLabel, average='macro')

    print 'kNN:',Precision, Recall, f

def bayes_run(train_data,train_label,test_data,test_label):
    clf = GaussianNB()
    clf.fit(train_data, train_label)
    predictLabel = clf.predict(test_data)
    print('predictLabel:', predictLabel.tolist(), test_label)
    Precision = metrics.accuracy_score(test_label, predictLabel)
    Recall = metrics.recall_score(test_label, predictLabel, average='macro')
    print 'Naive Bayes:',Precision, Recall

if __name__ == '__main__':
    feature_path = "feature"
    keywords = "IAT"
    filenames = find_filenames(feature_path, keywords)
    file = combine_labels(filenames, keywords,feature_path)
    data,label = loadDataSet(file)

    # print len(data),len(label)
    # # print data
    # print label
    train_data, train_label,test_data, test_label = get_data_for_cross_validation(data,label)
    print len(train_data), len(test_data)
    svm_run(train_data,train_label,test_data,test_label)
    rf_run(train_data,train_label,test_data,test_label)
    knn_run(train_data,train_label,test_data,test_label)
    bayes_run(train_data,train_label,test_data,test_label)



#coding:utf-8
import sys
import os
import file_util, settings
import random
from sklearn.model_selection import StratifiedKFold

#给样本添加标签,将添加完标签的数据写入文件中，形成feature
def combine_samples(filenames, keywords, feature_path):
    filepath = r"combine/%s.txt" %keywords
    if os.path.exists(filepath):
        os.remove(filepath)
    file_keywords = open(filepath,'w+')
    label = 0
    for file in filenames:
        print "Using file:", file
        label = label + 1
        f = open(r"%s/%s" % (feature_path, file))
        for line in f.readlines():
            # text = line.split(',')
            text = line.split(',')[1:]
            file_keywords.writelines(r"%d,%s" %(label,",".join(text)))
        if label == settings.DEVICE_NUM:
            break
        f.close()
    file_keywords.close()

    return file_keywords


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
    data = list(zip(dataMat,labelMat))
    random.shuffle(data)
    dataMat[:], labelMat[:] = zip(*data)
    return dataMat,labelMat


def get_train_test_data(feature_path, keywords, cv=10):
    # print "script: extract_feature.py,  lineNumber:", sys._getframe().f_lineno, ",  func:", sys._getframe().f_code.co_name


    filenames = file_util.find_filenames(feature_path, keywords)
    #随机生成DEVICE_NUM个随机数，取出相应的feature文件，file_No为文件序号
    file_No = random.sample(range(0, len(filenames)), settings.DEVICE_NUM)
    new_filenames = [filenames[i] for i in file_No]
    print new_filenames
    file = combine_samples(new_filenames, keywords, feature_path)
    data, label =loadDataSet(file)
    skf = StratifiedKFold(n_splits=cv, random_state=True)
    train_data = list()
    for train_index,test_index in skf.split(data, label):
        train_data = [data[i] for i in train_index]
        train_label = [label[i] for i in train_index]
        test_data = [data[i] for i in test_index]
        test_label = [label[i] for i in test_index]
        break
    return train_data, train_label,test_data, test_label, new_filenames






if __name__ == '__main__':
    import settings
    get_train_test_data(settings.FEATURE_DIR, 'frameSize')
from __future__ import division
import random
import numpy as np


def get_data_for_validation_random(dataX, dataY, cv=10):
    datalen = len(dataX)
    rand_sample = random.sample(range(datalen), datalen)
    datagroupX = dict()
    datagroupY = dict()
    for i, rs in enumerate(rand_sample):
        datagroupX.setdefault(i%cv, list()).append(dataX[rs])
        datagroupY.setdefault(i%cv, list()).append(dataY[rs])

    def listextend(x, y):
        x_ = x[:]
        x_.extend(y)
        return x_
    for i in range(cv):
        trainX = reduce(listextend, [datagroupX[j] for j in range(cv) if j != i])
        trainY = reduce(listextend, [datagroupY[j] for j in range(cv) if j != i])
        testX = datagroupX[i]
        testY = datagroupY[i]
        yield trainX, trainY, testX, testY

def get_data_for_cross_validation(dataX,dataY,cv=10):
    trainX = []
    testX = []
    trainY = []
    testY = []
    seed = random.randint(1, cv)
    # print dataY
    label = dataY[0]
    index = 0
    for i in range(len(dataY)):
        if label != dataY[i]:
            index = 0
            label = dataY[i]
        index = index + 1
        if index%cv == seed:
            # print index,label
            testX.append(dataX[i])
            testY.append(dataY[i])
        else:
            trainX.append(dataX[i])
            trainY.append(dataY[i])
    return trainX,trainY,testX,testY



def get_data_for_validation_order(dataX, dataY, cv=10):
    subjects = set(dataY)
    dataXspa = dict()
    dataYspa = dict()
    id = dict()
    for dx, dy in zip(dataX, dataY):
        dataXspa.setdefault(dy, dict()).setdefault(id.setdefault(dy, 0), list()).append(dx)
        dataYspa.setdefault(dy, dict()).setdefault(id[dy], list()).append(dy)
        id[dy] += 1
        id[dy] %= cv

    for i in range(cv):
        def list_add(x, y):
            x_ = x[:]
            x_.extend(y)
            return x_
        testx = reduce(list_add, [dataXspa[subject][i] for subject in subjects])
        testy = reduce(list_add, [dataYspa[subject][i] for subject in subjects])
        trainx = reduce(list_add, [dataXspa[subject][j] for j in range(cv) if j != i for subject in subjects])
        trainy = reduce(list_add, [dataYspa[subject][j] for j in range(cv) if j != i for subject in subjects])
        yield trainx, trainy, testx, testy


# def cross_validation_f_measure_multi(clf, dataX, dataY, cv=10, testX=None, testY=None,
#                                      isbinaryclassifier=True,is_val_rand=True, **kwargs):
#     '''if testX is None and testY is None, then it is an open set test.
#        And if isbinaryclassifier == True, then it uses binary classifier.'''
#     get_data_for_validation = get_data_for_validation_random if is_val_rand else get_data_for_validation_order
#     from f_measure import f_measure
#     openset_test = True if testY else False
#     if openset_test:
#         print 'openset test: return fn and fp'
#     else:
#         print 'closeset test: return fn'
#     Plist = list()
#     Rlist = list()
#     Flist = list()
#     subjects = set(dataY)
#     numofsub = len(subjects)
#     negative_label = '0'
#     try:
#         dataY[0] + '0'
#     except TypeError:
#         negative_label = 0
#     for i, (trainX, trainY, testX_, testY_) in \
#             enumerate(get_data_for_validation(dataX=dataX, dataY=dataY, cv=cv)):
#         P, R, F = 0, 0, 0
#         for subject in subjects:
#             if isbinaryclassifier:
#                 trainY_ = [subject if y == subject else negative_label for y in trainY]
#             else:
#                 trainY_ = trainY
#             # clf = RandomForestClassifier(n_estimators=51)
#             clf_ = clf.fit(trainX, trainY_, **kwargs)
#             prdt = clf_.predict
#             if openset_test:
#                 testX.extend(testX_)
#                 testY.extend(testY_)
#             else:
#                 testX = testX_
#                 testY = testY_
#             predictY = prdt(testX)
#             p, r, f = f_measure(prdty=predictY, testy=testY, poslabel=subject)
#             P, R, F = P+p, R+r, F+f
#         Plist.append(P/numofsub)
#         Rlist.append(R/numofsub)
#         Flist.append(F/numofsub)
#     return np.array(Plist), np.array(Rlist), np.array(Flist)


if __name__ == '__main__':
    dataY = [0 if random.random() > 0.5 else 1 for _ in range(42)]
    print type(dataY)
    for trainx, trainy, testx, testy in get_data_for_validation_order(zip(range(42), range(42)), dataY, cv=5):
        print trainx, trainy, testx, testy



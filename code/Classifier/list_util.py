# encoding: utf-8
#列表转置
def transpose(matrix):
    # print "script: temp.py,  lineNumber:", sys._getframe().f_lineno, ",  func:", sys._getframe().f_code.co_name
    return map(list, zip(*matrix))

# 取出矩阵的某一列
def get_column_from_matrix(matrix, col):
    """
    :param matrix: 二维列表（矩阵）
    :param col: 列编号
    :return: 矩阵的第col列
    """

    # print "script: temp.py,  lineNumber:", sys._getframe().f_lineno, ",  func:", sys._getframe().f_code.co_name
    return [row[col] for row in matrix]


def get_data_for_cross_validation(dataX,dataY,cv=5):
    import random
    import numpy as np
    trainX = []
    testX = []
    trainY = []
    testY = []
    while len(testX) == 0:
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
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
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

#列表横向合并
def merge(list1, list2):
    """
    列表横向合并
    :param list1: list，第一个列表
    :param list2: list，第二个列表
    :return: merge_list，合并后的列表
    列表1和列表2的行数必须一致
    example：
    >>> a = [[1, 2], [3, 4], [12, 13]]
    >>> b = [[5, 6], [7, 8], [22, 23]]
    >>> merge(a, b)
    >>> [[1, 2, 5, 6], [3, 4, 7, 8], [12, 13, 22, 23]]
    """
    merge_list = [list1[i] + list2[i] for i in range(len(list1))]
    return merge_list


if __name__ == '__main__':
    a = [[1, 2], [3, 4], [12, 13]]
    b = [[5, 6], [7, 8], [22, 23]]
    print merge(a, b)
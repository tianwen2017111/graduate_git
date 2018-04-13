# encoding: utf-8
import sys
import list_util


def get_hist(vector, bin_number):
    """
    计算向量的频率分布
    :param vector: 待计算向量
    :param bin_number: 区间数
    :return: 每一个区间的频率
    """
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        raise ImportError('The program requires matplotlib')

    if len(vector) > bin_number:
        n, nbins, patches = plt.hist(vector, bin_number, normed=1, histtype='bar', alpha=0.75)
        if max(vector) == min(vector):
            for i, _n in enumerate(n):
                n[i] = 1.0/bin_number
        else:
            bin_width = (max(vector) - min(vector)) / bin_number
            # 频数分布直方图的每个长方形的面积，才是该区间内的频率
            for i, _n in enumerate(n):
                n[i] = _n * bin_width
        #n为numpy.ndarray格式，需要将其转换为list
        return n.tolist()
    else:
        print "bin_number error"


def divide_vector_into_group(vector, group_size):
    """将一个向量(vector)划分成若干个大小相同的组(group)
        其中组数（group_number）已知，
        每组元素个数（group_size） = 总的样本数(len(vector)) / 组数(group_number)
        :parameter vector: 待划分向量
        :parameter group_size: 每组元素的个数"""

    if len(vector) > group_size:
        group_number = len(vector) / group_size #每组元素的个数
        for i in xrange(group_number ):
            group_i = vector[group_size*i: group_size*(i+1)]#第i组数据
            yield group_i
    else:
        print "group_size error"


def get_feature_from_matrix(data, group_size, bin_number):
    # print "script: extract_feature.py,  lineNumber:", sys._getframe().f_lineno, ",  func:", sys._getframe().f_code.co_name
    def get_feature_from_vector(vector):
        feature = list()
        divied_data = divide_vector_into_group(vector, group_size=group_size)
        for group in divied_data:
            feature.append(get_hist(group, bin_number))
        return feature

    return map(get_feature_from_vector, list_util.transpose(data))  # 归一化矩阵的每一列


if __name__ == '__main__':
    pass
    # import os
    # import file_util
    # ROOT_PATH = 'Data'
    # GROUP_SIZE = settings.GROUP_SIZE
    # BIN_NUMBER = settings.BIN_NUMBER
    # params_list = settings.params_list
    # generate_features("Data", "feature", params_list, group_size=GROUP_SIZE, bin_number=BIN_NUMBER)


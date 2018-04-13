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


def get_statistics(vector):
    import numpy as np
    a = np.array(vector)
    a_max = np.max(a)
    a_min = np.min(a)
    a_std = np.std(a)
    a_mean = np.mean(a)
    a_median = np.median(a)
    a_Q1 = np.percentile(a, 25)
    a_Q3 = np.percentile(a, 75)
    s_v = [a_max, a_min, a_std, a_mean, a_median, a_Q1, a_Q3]
    return s_v


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
            # feature.append(get_hist(group, bin_number)) #基于概率密度的特征
            feature.append(get_statistics(group)) #基于统计量的特征
        return feature

    return map(get_feature_from_vector, list_util.transpose(data))  # 归一化矩阵的每一列


if __name__ == '__main__':
    v = [1, 2, 1, 3, 5, 12, 0]
    get_statistics(v)
    import sklearn
    print sklearn.__version__
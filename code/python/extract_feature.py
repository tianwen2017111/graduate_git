# encoding: utf-8
import sys
def divide_data(data, group_number=4):
    """
    
    :param data: 原始数据，一维列表
    :param bin_number: 分组数目   
    :return: 
    """
    print "script: extract_feature.py,  lineNumber:", sys._getframe().f_lineno, ",  func:", sys._getframe().f_code.co_name



    # return map(devide_vecotr, data)

def get_hist(vector, bin_number=5):
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

    n, nbins, patches = plt.hist(vector, bin_number, normed=1, histtype='bar', alpha=0.75)
    bin_width = (max(vector) - min(vector)) / bin_number
    # print bin_width
    # bins = []
    # 频数分布直方图的每个长方形的面积，才是该区间内的频率
    for i, _n in enumerate(n):
        n[i] = _n * bin_width
    # 取每个bins的中点值（为了保持n和bins维度的一致）
    # for i in range(len(nbins) - 1):
    #     bins.append((nbins[i] + nbins[i + 1]) / 2)
    return n

def divide_vector_into_group(vector, group_size=300):
    """将一个向量(vector)划分成若干个大小相同的组(group)
        其中组数（group_number）已知，
        每组元素个数（group_size） = 总的样本数(len(vector)) / 组数(group_number)
        :parameter vector: 待划分向量"""

    group_number = len(vector) / group_size #每组元素的个数
    for i in xrange(group_number ):
        group_i = vector[group_size*i: group_size*(i+1)]#第i组数据
        yield group_i


# def generate_train_sample(data):



if __name__ == '__main__':
    import os
    import file_util
    ROOT_PATH = 'G:\graduate_git'
    GROUP_NUMBER = 100
    BIN_NUMBER = 20

    denoised_dir_path = os.path.join(ROOT_PATH, 'denoised')
    for root, _, files in os.walk(denoised_dir_path):
        for file in files:
            denoised_file_path = root + '\\' + file

            data = file_util.read_vector_file(denoised_file_path)
            divied_data = divide_vector_into_group(data)

            feature_file_path = os.path.join(ROOT_PATH, 'feature', file)
            print "Generating: ", feature_file_path
            feature = []
            for group in divied_data:
                feature.append(get_hist(group, bin_number=BIN_NUMBER))
            file_util.write_matrix_to_file(feature_file_path, feature)

            # file_util.write_matrix_to_file(feature_file_path, feature)
            # file_util.write_matrix_to_file(feature_file_path, feature)

    # import data_process
    # import os
    # import file_util
    # data_path = "G:\graduate_git\Data"
    # file_path = os.path.join(data_path, "text.txt")

    # no = temp.normalize(data)
    # print no
    # data = file_util.read_file(file_path)
    # print data
    # first_vector = data_process.get_column_from_matrix(data, 0)
    # print first_vector
    # print get_hist(first_vector,bin_number=5)




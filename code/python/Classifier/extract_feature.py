# encoding: utf-8
import sys
import data_process


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

        return n
    else:
        print "bin_number error"

def divide_vector_into_group(vector, group_size):
    """将一个向量(vector)划分成若干个大小相同的组(group)
        其中组数（group_number）已知，
        每组元素个数（group_size） = 总的样本数(len(vector)) / 组数(group_number)
        :parameter vector: 待划分向量"""

    if len(vector) > group_size:
        group_number = len(vector) / group_size #每组元素的个数
        for i in xrange(group_number ):
            group_i = vector[group_size*i: group_size*(i+1)]#第i组数据
            yield group_i
    else:
        print "group_size error"

def get_feature_from_matrix(data,group_size,bin_number):
    print "script: extract_feature.py,  lineNumber:", sys._getframe().f_lineno, ",  func:", sys._getframe().f_code.co_name
    print "3333333333",data
    def get_feature_from_vector(vector):
        feature = []
        divied_data = divide_vector_into_group(vector, group_size=group_size)
        for group in divied_data:
            # print group
            feature.append(get_hist(group, bin_number=bin_number))
        print "------------",type(feature)
        return feature

    return map(get_feature_from_vector, data_process.transpose(data))  # 归一化矩阵的每一列


def divide_matrix_to_file(data, target_path, base_name, post_name_list):
    """
    * 将二维列表的每一行分别写入文件中，
    * 二维列表有几列，就生成几个文件
    * 新文件的文件名为： root_file + '_' + new_files[i] + '.txt'

    :param data: 二维列表
    :param file_path: 文件保存的路径
    :param root_file: string, 根文件名
    :param new_filenames: list，新文件名列表
    :return: None
    ---------
    example:
    root_file = 'animal'
    new_files = ['dog', 'bee', 'duck']
    则新生成三个文件，文件名分别为'animal_dog.txt','animal_dog.txt','animal_dog.txt'
    """
    print "script: extract_feature.py,  lineNumber:", sys._getframe().f_lineno, ",  func:", sys._getframe().f_code.co_name
    print data
    for i, row in enumerate(data):
        param_file_name = os.path.join(target_path, base_name + "_" + post_name_list[i] + ".txt")
        print "dfhjghjd",type(row[0]),row
        # if i == 1:
        #     break
        file_util.write_file(param_file_name, row)


def generate_features(source_dir_path, target_dir_path, params_list, group_size=2, bin_number=2):
    print "script: extract_feature.py,  lineNumber:", sys._getframe().f_lineno, ",  func:", sys._getframe().f_code.co_name
    file = "text.txt"
    data = file_util.read_file(source_dir_path + "\\" + file)
    # print data
    fp = get_feature_from_matrix(data, group_size, bin_number)
    # print "fp--------",fp
    divide_matrix_to_file(fp, target_dir_path, base_name=file, post_name_list=params_list)
    # for root, _, files in os.walk(source_dir_path):
    #     for file in files:
    #         print file
    #         data = file_util.read_file(source_dir_path + "\\" + file)
    #         fp = get_feature_from_matrix(data, group_size, bin_number)
    #         divide_matrix_to_file(fp, target_dir_path, file, params_list)

if __name__ == '__main__':
    import os
    import file_util
    ROOT_PATH = 'Data'
    GROUP_SIZE = 500
    BIN_NUMBER = 20
    params_list = ['IAT', 'frameSize', 'transRate']
    generate_features("Data", "feature", params_list, group_size=5, bin_number=2)

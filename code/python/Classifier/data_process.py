# encoding: utf-8

import file_util
import os
import sys


#数据归一化（最大值最小值）
def normalize(matrix):
    """Data normalization
    :parameter
    ----------
    data: two-dimensional list(二维列表)
    """
    print "script: temp.py,  lineNumber:", sys._getframe().f_lineno, ",  func:", sys._getframe().f_code.co_name
    #向量的归一化
    def fn(vector):
        vector_max = max(vector)
        vector_min = min(vector)
        return [(v - vector_min)/(vector_max - vector_min) for v in vector]
    normalized = map(fn, transpose(matrix))#归一化矩阵的每一列
    return transpose(normalized)


#数据降噪
def denoise(matrix, thresholds):
    """Data denoise, Filter out any data greater than the threshold.
       :parameter
       ----------
       matrix: two-dimensional list 二维列表
       thresholds: list, 每一个的参数的阈值，即每一列的阈值。只有当一个样本中的
                    每一个参数均小于其对应的阈值时，才保留该样本
       ----------
       example：
       matrix = [[1.0, 2.0, 3.0],
                [4.0, 2.0, 6.0], 
                [1.5, 2.9, 3.5], 
                [1.5, 3.1, 3.5]]
       >>denoise(matrix, [2.0, 3.0, 4.0])
       >>[[1.0, 2.0, 3.0], [1.5, 2.9, 3.5]]
       """

    def fn(list):
        for i, item in enumerate(list):
            if item > thresholds[i]:
                return False
        return True
    return filter(fn, matrix)


#画出数据的散点图
def point_plot(vector):
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        raise ImportError('The program requires matplotlib')
    # fig = plt.figure(0)
    plt.scatter(range(0, len(vector)), vector)
    # ax = fig.add_subplot
    # ax.scatter(range(0,vector.len), vector)
    plt.show()

#列表转置
def transpose(matrix):
    print "script: temp.py,  lineNumber:", sys._getframe().f_lineno, ",  func:", sys._getframe().f_code.co_name
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


def divide_matrix_to_file(data, file_path, root_file, new_filenames):
    """    
    * 将二维列表的每一列分别写入文件中，
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
    print "script: data_process.py,  lineNumber:", sys._getframe().f_lineno, ",  func:", sys._getframe().f_code.co_name
    for i in range(len(data[0])):
        vector_i = get_column_from_matrix(data, i)
        param_file_name = os.path.join(file_path, root_file + "_" + new_filenames[i] + ".txt")
        file_util.write_vector_to_file(param_file_name, vector_i)


def refactor_param(filepath, params):
    for root, _, files in os.walk(filepath):
        for file in files:
            source_file = root + '\\' + file
            data = file_util.read_file(source_file)

            divide_matrix_to_file(data, filepath, file[:-4], params)

if __name__ == '__main__':
    # undenoised_dir_path = "Data"
    # denoised_dir_path = "undenosied"
    # params = ['IAT', 'frameSize', 'transRate']
    # refactor_param("Data", params)
    data = file_util.read_file('Data\\text.txt')
    print denoise(data, [100000,10000,100000])
    # for root, _, files in os.walk(undenoised_dir_path):
    #     for file in files:
    #         source_file = root + '\\' + file
    #         data = file_util.read_file(source_file)
    #         print denoised_dir_path
    #         divide_matrix_to_file(data, denoised_dir_path, file[:-4], params)
            # denoised = denoise(data, [0.04, 100, 1.2 * 10 ** 6])
            # divide_matrix_to_file(denoised, denoised_dir_path, file[:-4], params)







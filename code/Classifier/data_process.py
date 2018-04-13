# encoding: utf-8

import file_util
import os
import sys
import list_util


#数据归一化（最大值最小值）
def normalize(matrix):
    """Data normalization
    :parameter
    ----------
    data: two-dimensional list(二维列表)
    """
    # print "script: data_process.py,  lineNumber:", sys._getframe().f_lineno, ",  func:", sys._getframe().f_code.co_name
    #向量的归一化
    def fn(vector):
        vector_max = max(vector)
        vector_min = min(vector)
        return [(v - vector_min)/(vector_max - vector_min) for v in vector]
        # for v in vector:
        #     print v,vector_max,vector_min
        #     return (v - vector_min)/(vector_max - vector_min)
    normalized = map(fn, list_util.transpose(matrix))#归一化矩阵的每一列
    return list_util.transpose(normalized)


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
    # print "script: data_process.py,  lineNumber:", sys._getframe().f_lineno, ",  func:", sys._getframe().f_code.co_name
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



# if __name__ == '__main__':
    # undenoised_dir_path = "Data"
    # denoised_dir_path = "undenosied"
    # params = ['IAT', 'frameSize', 'transRate']
    # refactor_param("Data", params)
    # print denoise(data, [100000,10000,100000])
    # for root, _, files in os.walk(undenoised_dir_path):
    #     for file in files:
    #         source_file = root + '\\' + file
    #         data = file_util.read_file(source_file)
    #         print denoised_dir_path
    #         divide_matrix_to_file(data, denoised_dir_path, file[:-4], params)
            # denoised = denoise(data, [0.04, 100, 1.2 * 10 ** 6])
            # divide_matrix_to_file(denoised, denoised_dir_path, file[:-4], params)







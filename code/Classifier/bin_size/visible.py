#coding: utf-8
import matplotlib.pyplot as plt
import file_util, list_util


if __name__ == '__main__':
    feature = "FS"
    rf_result = file_util.read_file(feature + "/rf_result.txt")
    svm_result = file_util.read_file(feature + "/svm_result.txt")
    knn_result = file_util.read_file(feature + "/knn_result.txt")
    bayes_result = file_util.read_file(feature + "/bayes_result.txt")

    rf_F = list_util.get_column_from_matrix(rf_result, 2)
    svm_F = list_util.get_column_from_matrix(svm_result, 2)
    knn_F = list_util.get_column_from_matrix(knn_result, 2)
    bayes_F = list_util.get_column_from_matrix(bayes_result, 2)

    x = range(5, 16, 1)

    plt.figure(1)

    plt.axis([4, 19, 0, 1.2])
    plt.plot(x, rf_F, marker='o', color='steelblue', label='RF')
    plt.plot(x, svm_F, marker='*', color='darkseagreen', label='SVM')
    plt.plot(x, knn_F, marker='^', color='orange', label='KNN')
    plt.plot(x, bayes_F, marker='v', color='lightcoral', label='NBC')
    # plt.legend(loc='upper center', ncol=4)
    plt.legend()
    plt.xlabel("bin_size")
    plt.ylabel("F1")
    plt.show()
#coding: utf-8
import file_util, list_util
import matplotlib.pyplot as plt

def plot_re(filename, threshold):
    result = file_util.read_file(filename)
    p = list_util.get_column_from_matrix(result, 0)
    r = list_util.get_column_from_matrix(result, 1)
    f = list_util.get_column_from_matrix(result, 2)

    indices = [i for i in range(len(f)) if f[i] > threshold]

    new_p = [p[i] for i in indices]
    new_r = [r[i] for i in indices]
    new_f = [f[i] for i in indices]

    # plt.axis([0, 50, 0, 1])
    # plt.plot(new_r[:50], new_p[:50],color='steelblue', marker='*', label='precision')
    # plt.plot(range(50), new_r[:50],color='darkseagreen', marker='*', label='recall')
    # plt.plot(range(50), new_f[:50],color='salmon', marker='*', label='F-measure')
    plt.show()

if __name__ == '__main__':
    #IAT: rf_threshold:0.8, svm_rf_threshold:0.4, knn_rf_threshold:0.7, bayes_rf_threshold:0.7
    #FS: rf_threshold:0.8, svm_rf_threshold:0.7, knn_rf_threshold:0.6, bayes_rf_threshold:0.7
    #TR: rf_threshold:0.8, svm_rf_threshold:0.8, knn_rf_threshold:0.6, bayes_rf_threshold:0.7
    #mix: rf_threshold:0.8, svm_rf_threshold:0.8, knn_rf_threshold:0.7, bayes_rf_threshold:0.8
    plot_re('svm_result.txt', 0.7)
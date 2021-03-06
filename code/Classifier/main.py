#coding: utf-8
import sys
import os
import file_util, settings, data_process, extract_feature, list_util
import classifer, cross_val

# def generate_features(source_dir_path, target_dir_path, params_list, group_size=300, bin_number=10):
#     # print "script: extract_feature.py,  lineNumber:", sys._getframe().f_lineno, ",  func:", sys._getframe().f_code.co_name
#     for root, _, files in os.walk(source_dir_path):
#         for file in files:
#             data = file_util.read_file(source_dir_path + "\\" + file)
#             # #---------------test function-------------------------
#             denoised_data = data_process.denoise(data, settings.THRESHOLDS)
#
#             # file_util.write_file('denoised'+'\\'+file, denoised_data)
#             fp = extract_feature.get_feature_from_matrix(denoised_data, group_size, bin_number)
#
#             for i, row in enumerate(fp):
#                 print len(row)
#                 param_file_name = os.path.join(target_dir_path, file[:-4] + "_" + params_list[i] + ".txt")
#                 row = data_process.normalize(row)#归一化
#                 file_util.write_file(param_file_name, row)
#             # break

def generate_mix_features(source_dir_path, target_dir_path, params_list, group_size=300, bin_number=10):
    # print "script: extract_feature.py,  lineNumber:", sys._getframe().f_lineno, ",  func:", sys._getframe().f_code.co_name
    for root, _, files in os.walk(source_dir_path):
        for file in files:
            data = file_util.read_file(source_dir_path + "\\" + file)
            # #---------------test function-------------------------
            # denoised_data = data_process.denoise(data, settings.THRESHOLDS)

            # file_util.write_file('denoised'+'\\'+file, denoised_data)
            fp = extract_feature.get_feature_from_matrix(data, group_size, bin_number)
            # fp = extract_feature.get_feature_from_matrix(denoised_data, group_size, bin_number)
            fp_dict = dict()
            for i, row in enumerate(fp):
                row = data_process.normalize(row)#归一化
                fp_dict[i] = row

            mix_fp_temp = list_util.merge(fp_dict[0], fp_dict[1])
            mix_fp = list_util.merge(mix_fp_temp, fp_dict[2])
            target_file = os.path.join(target_dir_path, file[:-4] + "_" + ".txt")
            file_util.write_file(target_file, mix_fp)




def invoke_classifers(train_data, train_label, test_data, test_label):
    classifer.svm_run(train_data, train_label, test_data, test_label)
    classifer.rf_run(train_data, train_label, test_data, test_label)
    classifer.knn_run(train_data, train_label, test_data, test_label)
    classifer.bayes_run(train_data, train_label, test_data, test_label)

if __name__ == '__main__':

    data_dir = settings.DATA_DIR
    feature_dir = settings.FEATURE_DIR
    group_size = settings.GROUP_SIZE
    bin_number = settings.BIN_NUMBER
    params_list = settings.params_list
    # deveice_number = 4
    print "device number: ", settings.DEVICE_NUM


    for i in range(10):

        generate_mix_features(data_dir, feature_dir, params_list, group_size, bin_number)
        train_data, train_label, test_data, test_label = cross_val.get_train_test_data(feature_dir, keywords='_', cv=10)
        # invoke_classifers(train_data, train_label, test_data, test_label)

        svm_p, svm_r, svm_f = classifer.svm_run(train_data, train_label, test_data, test_label)
        svm_file = open('svm_result.txt', 'a')
        svm_file.write(str(svm_p) + ',' + str(svm_r) + ',' + str(svm_f) + '\n')
        svm_file.close()

        rf_p, rf_r, rf_f = classifer.rf_run(train_data, train_label, test_data, test_label)
        rf_file = open('rf_result.txt', 'a')
        rf_file.write(str(rf_p) + ',' + str(rf_r) + ',' + str(rf_f) + '\n')
        rf_file.close()

        knn_p, knn_r, knn_f = classifer.knn_run(train_data, train_label, test_data, test_label)
        knn_file = open('knn_result.txt', 'a')
        knn_file.write(str(knn_p) + ',' + str(knn_r) + ',' + str(knn_f) + '\n')
        knn_file.close()

        bayes_p, bayes_r, bayes_f = classifer.bayes_run(train_data, train_label, test_data, test_label)
        bayes_file = open('bayes_result.txt', 'a')
        bayes_file.write(str(bayes_p) + ',' + str(bayes_r) + ',' + str(bayes_f) + '\n')
        bayes_file.close()



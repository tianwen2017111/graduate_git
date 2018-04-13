#coding: utf-8
import sys
import os
import file_util, settings, data_process, extract_feature
import classifer

def generate_features(source_dir_path, target_dir_path, params_list, group_size=2, bin_number=2):
    print "script: extract_feature.py,  lineNumber:", sys._getframe().f_lineno, ",  func:", sys._getframe().f_code.co_name
    for root, _, files in os.walk(source_dir_path):
        for file in files:
            # file = "jzp_phone.txt"
            data = file_util.read_file(source_dir_path + "\\" + file)
            # #---------------test function-------------------------
            denoised_data = data_process.denoise(data, settings.THRESHOLDS)

            # file_util.write_file('denoised'+'\\'+file, denoised_data)
            fp = extract_feature.get_feature_from_matrix(denoised_data, group_size, bin_number)

            for i, row in enumerate(fp):
                param_file_name = os.path.join(target_dir_path, file + "_" + params_list[i] + ".txt")
                # print "Save in: ", param_file_name
                file_util.write_file(param_file_name, row)
            # break

def invoke_classifers(train_data, train_label, test_data, test_label):
    classifer.svm_run(train_data, train_label, test_data, test_label)
    classifer.rf_run(train_data, train_label, test_data, test_label)
    classifer.knn_run(train_data, train_label, test_data, test_label)
    classifer.bayes_run(train_data, train_label, test_data, test_label)

if __name__ == '__main__':
    data_dir = settings.DATA_DIR
    feature_dir = settings.FEATURE_DIR
    group_sizes = range(200, 500, 50)
    bin_number = settings.BIN_NUMBER
    params_list = settings.params_list
    for group_size in group_sizes:
        print "group_size-----------",group_size
        generate_features(data_dir, feature_dir, params_list, group_size, bin_number)
        train_data, train_label, test_data, test_label = file_util.get_train_test_data(feature_dir,"IAT")
        invoke_classifers(train_data, train_label, test_data, test_label)

#coding: utf-8
import sys
import os
import file_util, settings, data_process, extract_feature
import classifer, cross_val

def generate_features(source_dir_path, target_dir_path, params_list, group_size=2, bin_number=2):
    # print "script: extract_feature.py,  lineNumber:", sys._getframe().f_lineno, ",  func:", sys._getframe().f_code.co_name
    for root, _, files in os.walk(source_dir_path):
        for file in files:
            data = file_util.read_file(source_dir_path + "\\" + file)
            # #---------------test function-------------------------
            denoised_data = data_process.denoise(data, settings.THRESHOLDS)

            # file_util.write_file('denoised'+'\\'+file, denoised_data)
            fp = extract_feature.get_feature_from_matrix(denoised_data, group_size, bin_number)

            for i, row in enumerate(fp):
                param_file_name = os.path.join(target_dir_path, file[:-4] + "_" + params_list[i] + ".txt")
                # print "Save in: ", param_file_name
                # 归一化
                # print "row--------",row
                # row = data_process.normalize(row)
                # print "normalize_row--------", row
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
    group_sizes = range(500, 550, 50)
    bin_number = settings.BIN_NUMBER
    params_list = settings.params_list
    # deveice_number = 4
    print "device number: ", settings.DEVICE_NUM
    for group_size in group_sizes:
        print "group_size-----------",group_size
        generate_features(data_dir, feature_dir, params_list, group_size, bin_number)
        train_data, train_label, test_data, test_label = cross_val.get_train_test_data(feature_dir, "frameSize", cv=10)
        # print max(train_label)
        # file_util.write_file("combine/train_data.txt",train_data)
        # file_util.write_file("combine/train_label.txt",train_label)
        # file_util.write_file("combine/test_data.txt",test_data)
        # file_util.write_file("combine/test_label.txt",test_label)

        invoke_classifers(train_data, train_label, test_data, test_label)

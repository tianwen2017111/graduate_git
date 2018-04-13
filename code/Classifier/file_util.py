# encoding: utf-8
import os

def file_line_count(file):
    """Return the number of lines in the file"""
    mfile = open(file, 'r')
    line_num = len(mfile.readlines())
    return line_num


def read_file(file):
    data_list = list()
    with open(file, 'r') as mfile:
        for line in mfile:
            data_list.append([float(n) for n in line.split(',')])
    return data_list


def write_file(file,text):
    # file_fir = os.path.split(file)[0]
    # #检查路径是否存在，如果不存在则创建
    # if not os.path.isdir(file_fir):
    #     os.makedirs(file_fir)
    with open(file,'w') as f:
        #判断text是一维列表还是二维列表
        # print type(text)
        if type(text[0]) is list:
            for line in text:
                f.write(','.join(str(s) for s in line))
                f.write('\n')
        else:
            f.write('\n'.join(str(s) for s in text))


def write_sample_to_file(file, all_the_text, _label):
    """Created by liangliang"""
    mfile = open(file, 'w')
    for c, line in enumerate(all_the_text):
        #数据格式为：'+1 1:0.24 2:0.345 3:0.456 .....'
        # mfile.write(line)
        mfile.write(_label[c]+',')
        mfile.write(','.join([str(s) for s in line]))
        mfile.write('\n')
    mfile.close()


def count_files(dir_path):
    import glob
    print dir_path
    line_num = list()
    # for filename in glob.glob(r'G:\study\2017\fifty_seven\test_data\ppsj\Ultrashort_spec\*\*.txt'):
    for root, _, filenames in os.walk(dir_path):
        for filename in filenames:
            if 'FULL' in filename:
                pass
            else:
                print filename
                line_num.append(file_line_count(os.path.join(root,filename)))
    t = sorted(line_num)
    print t
    print sum(line_num) / len(line_num)


def find_filenames(dir_path, key_word):
    #获取包含关键字的文件名，并以列表的形式返回
    filenames = list()
    for root, _, files in os.walk(dir_path):
        for file in files:
            if key_word in file:
                filenames.append(file)
    return filenames


if __name__ == '__main__':
    pass
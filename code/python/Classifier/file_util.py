# encoding: utf-8
import os

def file_line_count(file):
    """Return the number of lines in the file"""
    mfile = open(file, 'r')
    line_num = len(mfile.readlines())
    return line_num

def load_sig_data(file):
    ''' read data from file and trans it for list '''
    mfile = open(file, 'r')
    file_list = list()
    try:
        lines = mfile.readlines()
        for line in lines:
            file_list.append(float(line))
    finally:
        mfile.close()
    # print "the length of '%s' is %d" % (filename, len(data_list))
    return file_list

# def read_file(file):
#     """Read file"""
#     mfile = open(file, 'r')
#     data_list = list()
#     for line_ in mfile:
#         data_list.append([float(n) for n in line_.split(',')])
#     return data_list

# def read_vector_file(file):
#     """Read file,文件只有一列，返回结果为一维列表"""
#     mfile = open(file, 'r')
#     data_list = list()
#     for line_ in mfile:
#         data_list.extend([float(n) for n in line_.split(',')])
#     return data_list

def read_file(file):
    data_list = list()
    with open(file, 'r') as mfile:
        for line in mfile:
            data_list.append([float(n) for n in line.split(',')])
            # print type(line[0])
            # if type(line[0]) is list:
            #     data_list.append([float(n) for n in line.split(',')])
            # else:
            #     data_list.extend([float(n) for n in line.split(',')])
    return data_list



def write_file(file,text):
    with open(file,'w') as f:
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
        mfile.write(_label[c]+' ')
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

#一个文件数据数目太少怎么办
def combine_labels(filenames,keywords,feature_path):
    filepath = r"combine/%s.txt" %keywords
    if os.path.exists(filepath):
        os.remove(filepath)
    file_keywords = open(filepath,'w+')
    label = 0
    for file in filenames:
        label = label + 1
        f = open(r"%s/%s" % (feature_path, file))
        for line in f.readlines():
            file_keywords.writelines(r"%d %s" %(label,line))
        f.close()
    file_keywords.close()

    return file_keywords

if __name__ == '__main__':
    text = [[1,2,3,4],[45,25,67]]
    # write_file("tttt.txt",text)
    print read_file("tttt.txt")
    # if type(text[0]) is 'list':
    #     print "1111111111111111"
    # else:
    #     print "sfdf"
    # print isinstance(text,(list))
    # filenames = []
    # feature_path = "feature"
    # keywords = "frameSize"
    # filenames = find_filenames(feature_path,keywords)
    # file = combine_labels(filenames,keywords)
    # print os.path.exists('combine/frameSize.txt')
    # os.close('combine/frameSize.txt')
    # os.remove(r'combine/frameSize.txt')
#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from file_util import *
from list_util import *
from data_process import denoise, normalize

def scatter_data(data):
    # -------------IAT散点图----------------------
    # IAT = get_column_from_matrix(data, 0)
    # # f1 = plt.figure(1)
    # plt.axis([0, 55000, 0, 1])
    # plt.scatter(range(len(IAT)), IAT, color='darkseagreen', marker='*')
    # # plt.show()
    # plt.savefig("G:\graduate_git\images\IAT.png")

    # -------------FrameSize散点图----------------------
    # FS = get_column_from_matrix(data, 1)
    # # f2 = plt.figure(2)
    # plt.axis([0, 55000, 0, 1])
    # plt.scatter(range(len(FS)), FS, color='steelblue', marker='*')
    # # plt.show()
    # plt.savefig("G:\graduate_git\images\FS.png")

    # -------------transRate散点图----------------------
    TR = get_column_from_matrix(data, 2)
    # f2 = plt.figure(3)
    plt.axis([0, 55000, 0, 1])
    plt.scatter(range(len(TR)), TR, color='salmon', marker='*')
    # plt.show()
    plt.savefig("G:\graduate_git\images\TR.png")




if __name__ == '__main__':

    data = read_file('ytw_ipad.txt')
    denoised = denoise(data, [0.2, 200, 0.2*10**9])
    normalized = normalize(denoised)
    # write_file("normalized.txt", normalized)
    scatter_data(normalized)


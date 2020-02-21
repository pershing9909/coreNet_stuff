import pandas as pd
import numpy as np

fp = open("BRAS10_cu.log")

for line in fp.readlines():  # 遍历每一行

    # print(line)
    # filename = line[:14]  # 每行取前14个字母，作为下面新建文件的名称
    # content = line[14:]  # 每行取第15个字符后的所有字符，作为新建文件的内容
    #
    # with open("e:\\" + filename + ".txt", "w") as fp2:
    #     fp2.write(content + "\n")









fp.close()
# 自动化测试中，要准备csv文件，文件内一般包含账号密码，所以要读取文件，自然就需要文件地址的处理
import csv
import os

file_name = '../config/账号密码.csv'
# 先找到测试数据文件(路径+文件名.csv)，如
print(os.path.dirname(__file__))  # 查看当前位置,而dirname()是返回目录的路径，这个是特殊用法
data_path = os.path.join(os.path.dirname(__file__), "..", "config", file_name)
print(data_path)
# B)打开这个文件(with  open);目的：是为了读取内容 ，如（as：重命名）
with open(data_path, "r", encoding="utf8") as file_data:
    # 使用读取测试数据文件中的内容
    file_value = csv.reader(file_data)
    # 把读取到的内容转换成python中的列表
    list_file = list(file_value)[1]
# E)把读取到的内容返回出去，（按行返回，1行就表示1个用例）
print(list_file)
print(list_file[1])

#总结：如何获得当前地址、如何获得相对路径地址、如何拼接、如何用csv库处理文件、最后如何提取想要的数据

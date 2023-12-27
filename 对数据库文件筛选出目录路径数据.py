import os
import re

# 指定目录和文件名
directory = r'D:\xxx\xxx'
filename = '数据.txt'

# 构建文件路径
file_path = os.path.join(directory, filename)

# 读取文件内容
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 提取路径数据
paths = []
for line in lines:
    match = re.search(r"/\s*\w+[\w./-]*", line)  # 使用正则表达式匹配路径类型的数据
    if match:
        path = match.group()
        paths.append(path)

# 导出到txt文件
output_file = 'result.txt'  # 修改为你想要的输出文件名
output_path = os.path.join(directory, output_file)

with open(output_path, 'w') as output:
    for path in paths:
        output.write(path + '\n')

print('提取完成！')

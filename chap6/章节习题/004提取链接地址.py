import re
import os

# 使用绝对路径
file_path = os.path.join('e:\\Microsoft Visual Studio\\Project\\Python_learning\\chap6\\章节习题', '习题4文本.txt')
with open(file_path, 'r', encoding='utf-8') as text:
    content = text.read()

# 使用非贪婪匹配(.*?)并更精确的匹配URL
pattern = r'https://.*?auto'  
matches = re.findall(pattern, content)

# 输出所有匹配到的URL
if matches:
    for match in matches:
        print(match)

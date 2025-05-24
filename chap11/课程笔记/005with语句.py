def write_fun(dst_file, content):
    with open(dst_file, 'w', encoding='utf-8' ) as file:
        file.write(content)

def read_fun(src_file):
    with open(src_file, 'r', encoding='utf-8' ) as file:
        content = file.read()
        return content  

def copy_fun(src_file, dst_file):
    write_fun(dst_file, read_fun(src_file))

if __name__ == '__main__':
    copy_fun(r'E:\Microsoft Visual Studio\Project\Python_learning\a.txt', r'E:\Microsoft Visual Studio\Project\Python_learning\chap11\课程笔记\aa.txt')

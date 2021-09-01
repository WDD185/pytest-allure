import os
import shutil


def read_txt():
    file = open('readme.txt', encoding='utf-8')
    while True:
        text = file.readline()
        print(text)
        a = '12345\n'
        if text == a:
            break
    file.close()


def write_txt():
    file = open('readme.txt', 'a', encoding='utf-8')
    file.write('\n我的中国心')
    file.close()
    file = open('readme.txt', encoding='utf-8')
    text = file.read()
    print(text)
    file.close()


def copy_txt():
    file1 = open('readme.txt', encoding='utf-8')
    file2 = open('readme2.txt', 'w', encoding='utf-8')
    text = file1.read()
    file2.write(text)
    file1.close()
    file2.close()


def copy_big_txt():
    file1 = open('readme.txt', encoding='utf-8')
    file2 = open('readme2.txt', 'w', encoding='utf-8')
    while True:
        text = file1.readline()
        file2.write(text)
        if len(text) == 0:
            break
    file1.close()
    file2.close()


def create_mir():
    print(os.listdir('G:\\mydir'))
    os.mkdir('G:\\mydir\\ndie')
    shutil.rmtree()  # 删除非空目录
    print(os.getcwd())  # 获取当前目录
    os.chdir()  # 切换到指定目录
    os.path.isdir()  # 判断是不是一个目录
    os.path.exists()  # 判断一个目录或文件是否存在


def op_batch():
    if os.path.exists('G:\\mydir\\mine'):
        shutil.rmtree('G:\\mydir\\mine')
    os.mkdir('G:\\mydir\\mine')
    os.chdir('G:\\mydir\\mine')
    print(os.getcwd())
    for i in range(1, 11):
        file = open('need%d.txt' % i, 'w', encoding='utf-8')
        file.write('test00%d，您好，这里是一行代码' % i)
        file.close()


def modify_name_batch():
    print(os.getcwd())
    path = 'G:\\mydir\\mine'
    if os.getcwd() != path:
        os.chdir(path)
    files_name = os.listdir()
    print(files_name)
    for x in files_name:
        os.rename(x, 'wxh ' + x)


print(eval('\'-\' * 50'))
print(eval('\'你好\''))
print(eval('{\'name\':\'wang\'}'))


def calc():
    user_input = input('请输入计算公式:')
    print(eval(user_input))



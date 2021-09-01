def search_data():
    i_list = [100, 'hello', 23.56, True, (10, 20)]
    find_data = True
    for i in i_list:
        if i == find_data:
            print('找到了：%s' % i)
            break
    else:
        print('没有你找的数据')


def find_name():
    i_list2 = [{'name': '王小1', 'age': 20, 'sex': '男'},
               {'name': '王小2', 'age': 22, 'sex': '女'},
               {'name': '王小3', 'age': 23, 'sex': '男'},
               {'name': '王小4', 'age': 25, 'sex': '女'}]
    want = input('请输入名字以查询：')
    for v in i_list2:
        if v.get('name') == want:
            print('我们找到了%s的信息' % v.get('name'))
            print('名字：%s，年龄：%s，性别：%s' %
                  (v.get('name'), v.get('age'), v.get('sex')))
            break
    else:
        v = '没有你想找的人'

    return v


my_sister = '飞鱼'
print(my_sister)
print(id(my_sister))


def one():
    print(my_sister)
    print(id(my_sister))


def two():
    global my_sister
    my_sister = '张倩'
    print(my_sister)
    print(id(my_sister))


def login_qq(user, pwd=123456):
    mysql_user = '李江华'
    mysql_pwd = 123456
    if user == mysql_user and pwd == mysql_pwd:
        return '登陆成功'
    else:
        return '用户名或密码错误'


print(login_qq('李江华'))

import io
import random

t = 'hello,baby'
s = io.StringIO(t)
print(s)
print(s.getvalue())
s.seek(7)
s.write('h')
print(s.getvalue())

dit = {
    'name': '刘欢',
    'age': 19,
    'sex': '男'
}

a, b, c = dit.values()  # 获取键值对的值
d, e, f = dit.items()  # 获取键值对的其中一对
g, h, i = dit  # 获取键值对的键
print(a, b, c, d, e, f, g, h, i)

lst2 = [{'id': 111, 'name': '网站'},
        {'id': 112, 'name': '营销工具'},
        {'id': 113, 'name': '公众号'},
        {'id': 119, 'name': '网报小程序'},
        {'id': 101, 'name': '自然口碑'},
        {'id': 102, 'name': '营销活动'},
        {'id': 103, 'name': '营销口碑'},
        {'id': 114, 'name': '地推'},
        {'id': 115, 'name': '广告'},
        {'id': 116, 'name': '户外广告'}]
for i in lst2:  # 先把列表里的字典取出来
    for x in i:  # 再把字典里的键取出来
        print(i[x])  # 最后通过字典取值的办法把字典里的值取出来

print(lst2)
w, q = random.sample(lst2, 1)[0].values()
print(w, q)
lst3 = [x.get('id') for x in lst2]
print(lst3)

name = ['王以太', '张锋', '李琴']
age = [12, 23, 17]
for x, y in zip(name, age):
    print('这是{}，他已经{}岁了'.format(x, y))

import json
import random
import time
import copy


def draw_a_circle():
    lst = ["\\", "|", "/", "———"]
    for i in range(20):
        j = i % 4
        print("\r" + lst[j], end="")
        time.sleep(0.2)


def now_air():
    tmp = 26
    wetness = 89.6
    pm_25 = 11
    return tmp, wetness, pm_25


print(now_air())

for i in range(10, 0, -1):
    print(i)

l_list = [x for x in range(4)]
print(l_list)

i_list = [x for x in range(0, 10, 2)]
print(i_list)

s_list = [x + 100 for x in range(10)]
print(s_list)

t_list = [x * x for x in range(10)]

a = [x for x in range(21) if x % 2 == 0]
a.sort(reverse=True)
print(a)


def test_list_1():
    a_list = []
    for x in range(10):
        a_list.append(x)
    print(a_list)


b = [random.randint(0, 100) for x in range(100)]
print(b)

b_list = [x + 100 for x in b if x % 2 == 0]
print(b_list)

c_list = []

num1 = [10, [12, 29]]
num2 = num1.copy()  # 通过copy函数把数据复制给num2，但是是不同的引用地址,但是引用地址中存的内存空间还是一样的，这是是浅拷贝
num3 = copy.deepcopy(num1)  # 通过copy中的deepcopy方法可以让引用地址中的内存空间也不一样，可以完全独立，这是深拷贝
num1.append(5)
num1[1].append(90)
num1[0] = 8
print(id(num1), num1)
print(id(num2), num2)
print(id(num3), num3)

context = [
    {
        'name': '三国演义',
        'author': '罗贯中',
        'price': 120
    },
    {
        'name': '西游记',
        'author': '吴承恩',
        'price': 100
    },
    {
        'name': '红楼梦',
        'author': '曹雪芹',
        'price': 90
    }]

for x in context:
    for y in x:
        print(x[y])

L = [('Bob', 75), ('adam', 92), ('bart', 66), ('Lisa', 88)]

print(sorted(L, key=lambda L: L[0].capitalize()))

L1 = {
    'Bob': 75,
    'adam': 92,
    'bart': 66,
    'Lisa': 88
}

print(sorted(L1.items(), key=lambda d: d[1]))
print(sorted(L1.items(), key=lambda d: d[0].capitalize()))


def count(func):
    start_time = time.clock()
    func()
    end_time = time.clock()
    count_time = end_time - start_time
    print('一共用时%d' % count_time)


def ret():
    for i in [1, 2, 3, 4]:
        i += 1
        yield i

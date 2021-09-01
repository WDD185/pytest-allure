import random
import time


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

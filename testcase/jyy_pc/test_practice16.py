from multiprocessing import Process, Pool
import random
import math


def run(x):
    lst = []
    for i in range(10):
        i += x
        lst.append(i)
    print(lst)
    return lst


def run1(y):
    s = random.randint(1, 10)
    x = s + y
    print(x)
    return x


def bar(multiple):
    def foo(n):
        print(multiple ** n)

    return foo


def f(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return (x * f(x - 1))


if __name__ == '__main__':
    p = Process(target=run, args=(3,), name='列表')
    #  p1 = Process(target=run1, args=(4,), name='相加')
    print(p.name)
    p.start()
    p.join()

    # print(p1.name)
    p1 = Pool()
    for i in range(10):
        p1.apply_async(run1, (i,))
    p1.close()
    p1.join()
    bar(2)(3)
    print(f(5))
    a = [2, 4, 6, 8, 20, 30, 40]
    print(a[::2])
    print(a[-2:])


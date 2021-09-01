def num_value(num, *args, **kwargs):
    # *args用来接收多余的参数，用元组的格式保存
    # **kwargs用来接收对于的关键字参数，用字典的格式保存
    print(num)
    print(args)
    print(kwargs)


num_value(123, 856, 512, name='元宝', sex='男', age=18)


def sum_unm(*args):
    print(args)
    sum1 = 0
    for i in args:
        sum1 += i
    return sum1


print(sum_unm(1, 2, 3, 85, 59, 62))

print((lambda: 100)())
print((lambda x: x + 100)(50))
print((lambda x, y: x * y)(50, 100))


def sum_num1(a, b, opt):
    print('a=%d' % a)
    print('b=%d' % b)
    print('%d + %d = %d' % (a, b, opt(a, b)))
    # 这里其实是把匿名函数的地址当作sum函数的参数传进去了，括号就相当于调用这个匿名函数，括号里的就是匿名函数参数


sum_num1(10, 20, lambda x, y: x + y)


class Human:
    def run(self, name):
        #  定义类里的方法
        print('吃了就跑，跑回了%s的娘家' % name)

    def eat(self, food):
        print('%s吃%s' % (self.name, food))
        self.run(self.name + '妈')  # 通过self方法调用类内部方法


jack = Human()
rose = Human()
#  使用类创建了两个对象。对象有属性有方法
#  对象名就是一个变量名，保存对象内存空间的地址，并且地址不同，互不干扰
jack.name = '杰克'
rose.name = '肉丝'
#  给对象添加属性,可以通过self参数访问这个属性（在外部给对象添加属性）
jack.eat('蒜苗回锅肉')
rose.eat('香肠')


class Cat:
    def __init__(self, name):
        #  init方法用来初始化数据，在类创建对象的时候自动调用
        #  给init方法传参，再用self内部其他的方法就可以调用这个参数
        print('用来初始化数据的')
        self.cat_name = name

    def drink(self, water):
        print('%s爱喝%s' % (self.cat_name, water))


cat1 = Cat('蓝白弟弟')
cat2 = Cat('英短妹妹')
cat1.drink('橙汁')
cat2.drink('骨头汤')

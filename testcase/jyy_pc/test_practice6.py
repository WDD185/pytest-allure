try:
    def fuc2():
        open('mine.txt', 'r', encoding='utf-8')


    fuc2()
except NameError:
    print('这是没有资源的错误')
except ValueError:
    print('这是值的错误')
except ZeroDivisionError:
    print('这是除数为0的错误')
except Exception as ecp:
    print('出现错误:%s' % ecp)
else:
    print('没有异常哦')
finally:
    print('结束罗')

try:
    def input_password():
        user_password = input('请输入您的密码：')
        if len(user_password) < 8:
            error = Exception('密码长度小于8位')
            #  使用exception类来自定义输出的错误信息
            raise error
            #  raise用来抛出该异常信息
        else:
            return user_password


    def no_index():
        lst = [0, 10]
        return lst[5]


    no_index()
except Exception as ecp:
    print('系统错误：%s' % ecp)
else:
    print('感谢您的输入')


class Del:
    def __init__(self, *args, **kwargs):
        self.file = open('try2.txt', 'r', encoding='utf-8')
        if args:
            self.cat_name = args[0]
        else:
            self.cat_name = '张嘉佳'

    def cat_drink(self, water):
        print('%s喜欢喝%s' % (self.cat_name, water))

    def book(self):
        print(self.file.read())

    def __del__(self):
        #  使用del方法自动清除对象的内存空间，当退出程序时自动调用
        self.file.close()


cat1 = Del('小蓝')
cat1.cat_drink('牛奶')
Del().book()

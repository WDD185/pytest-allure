class Person:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('%s是个吃货' % self.name)


if __name__ == '__main__':
    jack = Person('jack')  # 使用类模板创建对象，对象在内存空间中实际存在，就叫做实例对象
    print(jack)
    print(jack.name)  # 实例对象中的属性，是实例属性
    jack.eat()  # 实例对象的方法，并且具有self属性的，是实例方法


class Moth:
    count = 1

    def __init__(self, name):
        self.name = name

    @classmethod  # 通过装饰器定义一个类方法
    def test_1(cls):
        sum1 = cls.count + 1  # 通过cls可以直接访问类属性count
        return sum1

    @staticmethod  # 通过装饰器定义一个静态方法
    def test_2():  # 静态方法不需要实例属性（self）和类属性（cls）
        your_name = 'david'
        his_name = 'rockC'
        print('%s和%s是好朋友' % (your_name, his_name))


if __name__ == '__main__':
    print(Moth.test_1())
    Moth.test_2()


class Game:
    top_score = 500

    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('算工资啦')

    @staticmethod
    def show_help():
        print('亲爱的玩家您好，欢迎来到本游戏！')

    @classmethod
    def show_top_score(cls):
        print('玩家历史最高纪录为：' + str(cls.top_score))

    def start_game(self):
        print('%s开始游戏' % self.name)


if __name__ == '__main__':
    Game.show_help()
    Game.show_top_score()
    Game('JC').start_game()

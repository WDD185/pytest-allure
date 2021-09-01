class Father:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.country = args[2]
        self.play = args[3]

    def dad_intro(self):
        print('我爸爸叫%s，他今年%s岁了,他的国籍是%s' % (self.name, self.age, self.country))

    def dad_play(self):
        print('我爸比较喜欢玩%s' % self.play)


class Mother:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.country = args[2]

    def mom_intro(self):
        print('我妈妈叫%s，她今年%s岁了,她的国籍是%s' % (self.name, self.age, self.country))

    def mom_play(self, play):
        print('我妈比较喜欢玩%s' % play)


class Mine(Father, Mother):
    def dad_play(self):
        print('我跟我爸爸一样也喜欢玩%s' % self.play)


class Bas(object):  # 新式类object是所有类的父类，创建类时可以在后面加上括号object，可以继承新式类
    pass


class Dog:
    def __init__(self, *args):
        self.dog_name = args[0]

    def game(self):
        print('%s喜欢玩游戏' % self.dog_name)


class Howling(Dog):
    def __init__(self, *args):
        self.dog_name = args[0]

    def game(self):
        print('%s喜欢在天上玩' % self.dog_name)


class Person(Dog):
    def __init__(self, *args):
        self.person_name = args[0]

    def play_with_howling(self, dog):
        print('%s喜欢跟%s一起玩' % (self.person_name, dog.dog_name))
        dog.game()


if __name__ == '__main__':
    jack = Person('jack')
    lucky = Dog('旺财')
    rose = Howling('哮天犬')
    jack.play_with_howling(lucky)


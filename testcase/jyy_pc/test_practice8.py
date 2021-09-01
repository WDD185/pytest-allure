class Soldier:
    def __init__(self, name, gun='AK47'):
        self.name = name
        self.gun = gun


class Fire:
    def __init__(self, bullet, bullet_num):
        self.bullet = bullet
        self.bullet_num = bullet_num

    def shoot(self, gun):
        if self.bullet <= 0:
            print('枪里没有子弹，无法射击')
            return
        else:
            self.bullet -= 1
            print('%s使用%s向前发射，子弹数量-1，目前为%d' % (gun.name, gun.gun, self.bullet))

    def load(self, gun):
        self.bullet += self.bullet_num
        print('%s装填子弹，子弹数量+%d，目前为%d' % (gun.name, self.bullet_num, self.bullet))
        #  可以把上个方法赋值变量，再把这个变量传参进入下一个函数，就可以使用上一个函数中的变量值了


person = Soldier('刘大炮', '东风XC-995F')
AK48 = Fire(28, 5)
AK48.shoot(person)
AK48.load(person)


class Women:
    def __init__(self, *args):
        self.name = args[0]
        self.__age = 20
        #  在属性前加上双下划线，将该属性变为私有属性，类外部无法访问但是可以在内部调用

    def her_age(self):
        print('这是%s个人秘密，只能说她是：%s岁' % (self.name, self.__age))

    def __secret(self):
        #  在方法前加上双下划线，将该方法变为私有方法，类外部无法访问
        print('我不想告诉你')


xiaoju = Women('小菊')
xiaoju.her_age()
xiaoju._Women__secret()


#  但是python的私有不是绝对的，只是通过名字重整的方式，把属性和方法的名字重整了，_类名__属性/方法名


class Animal:
    def __init__(self, *args):
        self.name = args[0]
        self.__age = 18

    def get_age(self):
        return self.__age

    def eat(self, *args):
        print('年龄是%s的每个%s都需要吃%s' % (self.__age, self.name, args[0]))  # 在类内部可以访问私有属性


class Cat(Animal):  # 在类后面加括号，括号中写入父类即可继承父类的属性方法等  子类（父类）：...这是单继承
    def catch(self, *args):
        print('%s喜欢抓%s' % (self.name, args[0]))


class ChinaCat(Cat):  # 在子类下继承，这个类叫为孙类，这是多层继承
    def character(self):
        print('中国猫的性格一般很温和')

    def catch(self, *args):  # 对上层父类的方法进行重写或拓展
        super().catch('狗子')  # 使用super方法调用父类的方法
        print('%s喜欢抓%s和%s' % (self.name, args[0], args[1]))


if __name__ == '__main__':
    lb = Animal('蓝白弟弟')
    lb.eat('耗子')
    Cat('美短弟弟').catch('鱼')
    ChinaCat('中国猫').catch('毛毛虫', '鸽子')

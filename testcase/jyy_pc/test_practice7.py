class Run:
    def __init__(self, *args, **kwargs):
        if len(args) == 2:
            self.name = args[0]
            self.weight = int(args[1])
        else:
            print('传参有误，请重新输入')
            self.name = input('请输入对象名字：')
            self.weight = int(input('请输入对象体重：'))

    def run(self):
        print('%s开始跑步' % self.name)
        self.weight -= 0.5
        print('%s跑完步后，体重降了0.5公斤，现在的体重是%d' % (self.name, self.weight))

    def eat(self, food):
        print('%s开始吃%s' % (self.name, food))
        self.weight += 1
        print('%s吃完%s后，体重涨了1公斤，现在的体重是%d' % (self.name, food, self.weight))


class HouseItem:
    def __init__(self, *args):
        print(len(args))
        if len(args) == 2:
            self.name = args[0]
            self.item_area = int(args[1])
        else:
            print('参数有误，请重新输入')
            self.name = input('请重新输入家具名称：')
            self.item_area = int(input('请重新输入家具占地面积：'))


class House:
    def __init__(self, *args):
        if len(args) == 2:
            self.type = args[0]
            self.house_area = int(args[1])
            self.free_area = self.house_area
            self.item_lst = []
        else:
            print('参数有误，请重新输入')
            self.type = input('请重新输入户型：')
            self.house_area = int(input('请重新输入户型面积：'))
            self.free_area = self.house_area
            self.item_lst = []

    def add_item(self, item):
        if self.free_area < item.item_area:
            print('家具面积超过户型面积')
            return
        self.free_area -= item.item_area
        self.item_lst.append(item.name)
        print('目前房型%s，剩余面积为%d平方，家具列表%s' % (self.type, self.free_area, self.item_lst))


bed = HouseItem('席梦思', 10)
cab = HouseItem('梳妆柜', 5)
table = HouseItem('电脑桌', 6)

your_house = House('B', 110)
my_house = House('四室两厅两卫', 168)
your_house.add_item(bed)
your_house.add_item(table)
my_house.add_item(bed)
my_house.add_item(cab)
my_house.add_item(table)

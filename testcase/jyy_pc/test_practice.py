import random


def a_game():
    while True:
        computer = random.sample(['1', '2', '3'], 1)[0]
        user = input('石头：1，剪刀：2，布：3\n输入后点击回车 \n请输入您的拳法：')
        if user in ['1', '2', '3']:
            print('您出：', user)
            print('电脑出：', computer)
            if (user == '1' and computer == '2')\
                    or (user == '2' and computer == '3')\
                    or (user == '3' and computer == '1'):
                print('您赢了..真是厉害！')
            elif user == computer:
                print('打了个平手')
            else:
                print('您输了，还要再来一把吗？')
        else:
            print('出手错误，游戏结束')
            break


def sign_to_replace():
    age = 18
    name = '小张'
    sex = '男'
    print('姓名:%s , 年龄：%d , 性别：%s' % (name, age, sex))


def a_loop():
    count = 1
    while count <= 5:
        print('对不起，count = %d ' % count)
        count += 1
    print('循环结束了')


def b_loop():
    i = 0
    sum1 = 0
    while i <= 100:
        if i % 2 == 0:
            print('i = %d' % i)
            sum1 = sum1 + i
        i += 1
    print('总和是：%d' % sum1)
    print('循环结束了')


def c_loop():
    apple = 0
    while apple < 5:
        print('apple:%d' % apple)
        if apple == 3:
            print('吃到第三个不想吃了')
            break
        apple += 1
    print('循环结束了')


def d_loop():
    apple2 = 0
    while apple2 < 5:
        apple2 += 1
        if apple2 == 3:
            print('第三个不想吃')
            continue
        print('apple2 = %d' % apple2)
    print('循环结束了')


def f_loop():
    day = 0
    while day < 3:
        sorry = 0
        while sorry < 3:
            sorry += 1
            print('我真的知错了%d' % sorry)
        print('刷碗')
        print('---------')
        day += 1
    print('做完了')


def g_loop():
    y = 1
    while y <= 9:
        x = 1
        while x <= y:
            print('%d * %d = %d\t' % (x, y, x * y), end='')
            x += 1
        print()
        y += 1


if __name__ == '__main__':
    g_loop()


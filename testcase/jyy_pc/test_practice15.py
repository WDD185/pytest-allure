import pygame


class Main:

    def __init__(self):
        self.window = None
        self.width = 800
        self.height = 500
        self.color_background = pygame.Color(0, 0, 0)
        self.color_text = pygame.Color(255, 0, 0)
        self.title = '欢迎来到 --坦克大战--'

    def start_game(self):
        pygame.display.init()
        self.window = pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption(self.title)
        while True:
            self.window.fill(self.color_background)
            self.get_event()
            self.window.blit(self.get_text('剩余地方坦克数量{}'.format(5)), (5, 5))
            pygame.display.update()

    def get_event(self):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                self.end_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print('坦克向左移动')
                elif event.key == pygame.K_RIGHT:
                    print('坦克向右移动')
                elif event.key == pygame.K_UP:
                    print('坦克向上移动')
                elif event.key == pygame.K_DOWN:
                    print('坦克向下移动')
                elif event.key == pygame.K_SPACE:
                    print('坦克发射子弹')

    def get_text(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('华文楷体', 18)
        text_surface = font.render(text, True, self.color_text)
        return text_surface

    def end_game(self):
        print('游戏结束，谢谢使用')
        exit()


class Tank:
    def __init__(self):
        self.images = {
            'u': pygame.image.load(r'E:pic\apple.jpg')
        }

    def move(self):
        pass

    def shoot(self):
        pass

    def show_tank(self):
        pass


class MyTank(Tank):
    def __init__(self):
        pass


class EnemyTank(Tank):
    def __init__(self):
        pass


class Bullet:
    def __init__(self):
        pass

    def move(self):
        pass

    def show(self):
        pass


class Boom:
    def __init__(self):
        pass

    def show(self):
        pass


class Wall:
    def __init__(self):
        pass

    def show(self):
        pass


class Music:
    def __init__(self):
        pass

    def play_music(self):
        pass


if __name__ == '__main__':
    Main().start_game()

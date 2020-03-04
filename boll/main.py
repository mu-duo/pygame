import pygame
import boll
import random
from config import *
import threading

class MyThread(threading.Thread):
    def __init__(self,a_boll,name = ''):
        threading.Thread.__init__(self)
        self.name = name
        self.boll = a_boll

    def run(self) -> None:
        while True:
            self.boll.move()
            pygame.time.delay(10)


def main():
    #初始化
    pygame.init()

    #设置窗口大小及名称
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('小球碰撞模拟器')

    #装纳小球
    boll_set = []
    #装纳线程，未启用
    thread_set = []

    #产生小球
    for i in range(BOLLS):
        # 小球半径在 10 -- 20 之间
        boll_set.append(boll.Boll(random.randint(10,20)))
        '''
        采用线程模式会极大的消耗资源，导致卡顿，若开启，请在boll模块里增加小球移动速度
        '''
        # thread_set.append(MyThread(boll_set[i]))
        # thread_set[i].start()

    while True:
        # 填充背景
        screen.fill((255,255,255))
        for i in boll_set:
            ''''
            开启线程模式时可选择关闭i.move(), 不关没有问题
            '''
            #每个小球移动一次
            i.move()
            # 若开启碰撞，则进行碰撞监测
            if HIT:
                i.hit(boll_set)
            pygame.draw.circle(screen, i.color, i.pos, i.radius)

        # 延时10ms
        pygame.time.delay(10)
        #更新
        pygame.display.update()



if __name__ == '__main__':
    main()

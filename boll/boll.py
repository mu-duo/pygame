from config import *
import random


class Boll():
    def __init__(self, radius=10):
        # 半径，默认为10
        self.radius = radius
        # 圆心坐标
        self.pos = [random.randint(self.radius, SCREEN_SIZE[X]-self.radius), random.randint(self.radius, SCREEN_SIZE[Y]-self.radius)]
        # 颜色随机
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        # 速度随机
        self.speed = [random.randint(-5,5), random.randint(-5,5)]

    def __repr__(self):
        print(self.pos)
        print(self.radius)
        print(self.speed)
        print(self.color)
        return ''

    def move(self):
        #移动
        self.pos[X] += self.speed[X]
        self.pos[Y] += self.speed[Y]

        # 判断是否出界
        if (self.pos[X] >= SCREEN_SIZE[X] - self.radius and self.speed[X]>0) or (self.pos[X] <= self.radius and self.speed[X]<0):
            self.speed[X] = -1*self.speed[X]
        if (self.pos[Y] >= SCREEN_SIZE[Y] - self.radius and self.speed[Y]>0) or (self.pos[Y] <= self.radius and self.speed[Y]<0):
            self.speed[Y] = -1*self.speed[Y]

    #碰撞机制可以尝试优化
    def hit(self,boll_set):
        #碰撞监测
        for boll in boll_set:
            distance = ((self.pos[X] - boll.pos[X]) ** 2 + (self.pos[Y] - boll.pos[Y]) ** 2)
            if distance < (self.radius**2+boll.radius**2) and distance > self.radius+boll.radius:
                self.speed = [-1*self.speed[X],-1*self.speed[Y]]


if __name__ == '__main__':
    boll = Boll()
    print(boll)
    boll.move()
    print(boll)

import pygame
import sys
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.pos=(x,y)
        self.lie=False
        self.neighbours=0
    def change_state(self):
        if self.lie == True:
            self.lie == False
        else:
            self.lie == True
    def get_neighbour(self,all_points):
        n1=(self.x-1,self.y-1)
        n2=(self.x,self.y-1)
        n3=(self.x+1,self.y-1)
        n4=(self.x-1,self.y)
        n5=(self.x+1,self.y)
        n6=(self.x-1,self.y+1)
        n7=(self.x,self.y+1)
        n8=(self.x+1,self.y+1)
        count=0
        neighbours_pre=[n1,n2,n3,n4,n5,n6,n7,n8]
        for neighbours_pre_one in neighbours_pre:
            for point in all_points:
                if point.pos == neighbours_pre_one and point.lie == True:
                    count+=1
        self.neighbours=count
WIDTH = 800
HIGHT = 600
block_size = (30, 30)
ROW = int(HIGHT/block_size[0])
COL = int(WIDTH/block_size[1])
Bg_color = (255, 255, 255)
life_color=(125,125,125)
screen_size = (WIDTH, HIGHT)
Line_color=(215,0,95)
pygame.init()
windows = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Life Game")
clock = pygame.time.Clock()
clocktrick = 30
Quit=False
subflag=0
all_points=set()
for i in range(ROW):
    for j in range(COL):
        all_points.add(Point(j,i))
poslist=set()
flag=True
while not Quit:
    pygame.Surface.fill(windows,Bg_color)
    for point in poslist:
        pygame.draw.rect(windows,life_color , ((point[0] * block_size[0], point[1] * block_size[0]), block_size))
    for j in range(ROW+1):
        pygame.draw.line(windows,Line_color,(0,j*block_size[0]),(COL*block_size[0],j*block_size[0]))
    for j in range(COL+1):
        pygame.draw.line(windows,Line_color,(j*block_size[0],0),(j*block_size[0],COL*block_size[0]))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Quit=True
            sys.exit()
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == 13:
                flag = not flag
                subflag = 1
            if event.key==91 :
                clocktrick=clocktrick*0.9
                break
            if event.key==93:
                clocktrick=clocktrick+1
                break
            if event.key==8:
                clocktrick=1
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos=event.pos
            point=(int(pos[0]/block_size[0]),int(pos[1]/block_size[1]))
            clocktrick=30
            if flag:
                if point in poslist:
                    poslist.remove(point)
                else:
                    poslist.add(point)
    if not flag:
        clocktrick=1
        if subflag:#通过次变量实现这个语句只会被执行一次
            for pos in poslist:
                for point in all_points:
                    if pos==point.pos:
                        point.lie=True
                    subflag=0
        for point in all_points:
            point.get_neighbour(all_points)
        #开始进化,把生的point点加入posliost,死的如果存在则删除
        for point in all_points:
            if point.neighbours == 3:
                point.lie = True
            elif point.neighbours == 2:
                pass
            else:
                point.lie = False
            if point.lie==True:
                poslist.add(point.pos)
            elif point.lie == False and point.pos in poslist:
                poslist.remove(point.pos)
    
    clock.tick(clocktrick)
    pygame.display.flip()

import pygame
import time
import random
import math

pygame.init()

screen_width = 300 #적정 스크린 사이즈:3000(메인 빵 이미지 크기)
screen_height = 300 #적정 스크린 사이즈:2500(메인 빵 이미지 크기)
#6:5

screen = pygame.display.set_mode((screen_width,screen_height) , pygame.RESIZABLE)

clock = pygame.time.Clock()

MapSize = (2500,3000)

OneCellPerPx = int(max(screen_width,screen_height)/10)


MAIN_BREAD = pygame.image.load('./img/main_bread.png')
main_bread = MAIN_BREAD #화질이 깨져서 원본 하나 해두고 복사본을 바꾸면서 쓰기
STD_HEADMOLD_IMG0001 = pygame.image.load('./animation/headmold_standing/headmold0001.png')
std_headmold_img0001 = STD_HEADMOLD_IMG0001
STD_HEADMOLD_IMG0002 = pygame.image.load('./animation/headmold_standing/headmold0002.png')
std_headmold_img0002 = STD_HEADMOLD_IMG0001
STD_HEADMOLD_IMG0003 = pygame.image.load('./animation/headmold_standing/headmold0003.png')
std_headmold_img0003 = STD_HEADMOLD_IMG0001
STD_HEADMOLD_IMG0004 = pygame.image.load('./animation/headmold_standing/headmold0004.png')
std_headmold_img0004 = STD_HEADMOLD_IMG0001
STD_HEADMOLD_IMG0005 = pygame.image.load('./animation/headmold_standing/headmold0005.png')
std_headmold_img0005 = STD_HEADMOLD_IMG0001
MICOMOLD_IMG0001 = pygame.image.load('./animation_headmold/micomold0001.png')
micomold_img0001 = MICOMOLD_IMG0001
MICOMOLD_IMG0002 = pygame.image.load('./animation_headmold/micomold0002.png')
micomold_img0002 = MICOMOLD_IMG0002
MICOMOLD_IMG0003 = pygame.image.load('./animation_headmold/micomold0003.png')
micomold_img0003 = MICOMOLD_IMG0003
STD_BABYMOLD_IMG0001 = pygame.image.load('./animation/babymold_standing/babymold0001.png')
std_babymold_img0001 = STD_BABYMOLD_IMG0001
STD_BABYMOLD_IMG0002 = pygame.image.load('./animation/babymold_standing/babymold0002.png')
std_babymold_img0002 = STD_BABYMOLD_IMG0002
STD_BABYMOLD_IMG0003 = pygame.image.load('./animation/babymold_standing/babymold0003.png')
std_babymold_img0003 = STD_BABYMOLD_IMG0003
STD_BABYMOLD_IMG0004 = pygame.image.load('./animation/babymold_standing/babymold0004.png')
std_babymold_img0004 = STD_BABYMOLD_IMG0004
STD_BABYMOLD_IMG0005 = pygame.image.load('./animation/babymold_standing/babymold0005.png')
std_babymold_img0005 = STD_BABYMOLD_IMG0005
HEADMOLDROKET_IMG = pygame.image.load('./img/headroket.png')
headmoldroket_img = HEADMOLDROKET_IMG
MICOMOLDROKET_IMG = pygame.image.load('./img/micoroket.png')
micomoldroket_img = MICOMOLDROKET_IMG
ANTISEPTIC_IMG = pygame.image.load('./img/antiseptic.png')
antiseptic_img = ANTISEPTIC_IMG






main_bread = pygame.transform.scale(MAIN_BREAD,(screen_width,screen_height))

class type:
    ANIMATION = 0
    LIVING = 1
    FOOD = 2
    def __init__(self):
        self.type = ""
class animation(type):
    HEADMOLD_ANI = 0
    MICOMOLD_ANI = 1
    ANTISEPTIC_ANI = 2
    BABYMOLD_ANI = 3
    def __init__(self,type_,fps):
        self.type = type.ANIMATION
        self.anitype = type_
        self.progress = 1
        self.fps = fps
        self.anilenght = 0
        self.fftime = time.time() #처음 프레임이 나왔던 시간 'f'irst 'f'rame time
        if self.anitype == self.HEADMOLD_ANI:
            self.anilenght = 5
        elif self.anitype == self.MICOMOLD_ANI:
            self.anilenght = 3
        elif self.anitype == self.BABYMOLD_ANI:
            self.anilenght = 5
        elif self.anitype == self.ANTISEPTIC_ANI:
            self.anilenght = 1
    def get_animation(self,width,height):
        if self.anitype == self.HEADMOLD_ANI:
            if self.progress == 1:
                return pygame.transform.scale(STD_HEADMOLD_IMG0001,(width,height))
            elif self.progress == 2:
                return pygame.transform.scale(STD_HEADMOLD_IMG0002,(width,height))
            elif self.progress == 3:
                return pygame.transform.scale(STD_HEADMOLD_IMG0003,(width,height))
            elif self.progress == 4:
                return pygame.transform.scale(STD_HEADMOLD_IMG0004,(width,height))
            elif self.progress == 5:
                return pygame.transform.scale(STD_HEADMOLD_IMG0005,(width,height))
        elif self.anitype == self.MICOMOLD_ANI:
            if self.progress == 1:
                return pygame.transform.scale(MICOMOLD_IMG0001,(width,height))
            elif self.progress == 2:
                return pygame.transform.scale(MICOMOLD_IMG0002,(width,height))
            elif self.progress == 3:
                return pygame.transform.scale(MICOMOLD_IMG0003,(width,height))
        elif self.anitype == self.BABYMOLD_ANI:
            if self.progress == 1:
                return pygame.transform.scale(STD_BABYMOLD_IMG0001,(width,height))
            elif self.progress == 2:
                return pygame.transform.scale(STD_BABYMOLD_IMG0002,(width,height))
            elif self.progress == 3:
                return pygame.transform.scale(STD_BABYMOLD_IMG0003,(width,height))
            elif self.progress == 4:
                return pygame.transform.scale(STD_BABYMOLD_IMG0004,(width,height))
            elif self.progress == 5:
                return pygame.transform.scale(STD_BABYMOLD_IMG0005,(width,height))
        elif self.anitype == self.ANTISEPTIC_ANI:
            if self.progress == 1:
                return pygame.transform.scale(ANTISEPTIC_IMG,(width,height))
    def update(self,width,height):
        if time.time()-self.fftime > 1/self.fps*self.progress:
            if self.progress >= self.anilenght:
                self.progress = 1
                self.fftime = time.time()
            else:
                self.progress +=1        
        return self.get_animation(width,height)

class mold(type): #곰팡이
    def __init__(self):
        self.type = type.LIVING
        self.HeadPos = [500,500]
        self.micomolds:list[micomold] = []
        self.animation = animation(animation.HEADMOLD_ANI,6)
        self.spore = 0
    def w(self,elapsed):
        self.HeadPos[1]-=10*elapsed
    def a(self,elapsed):
        self.HeadPos[0]-=10*elapsed
    def s(self,elapsed):
        self.HeadPos[1]+=10*elapsed
    def d(self,elapsed):
        self.HeadPos[0]+=10*elapsed
    def usespore(self,target):
        rokets.append(headmoldroket(self.HeadPos,target))

class micomold(type): #곰팡이 노비
    def __init__(self,rating,pos):
        self.type = type.LIVING
        self.Pos = pos
        self.helth = 100
        self.spawntime = 1000
        self.animation = animation(animation.MICOMOLD_ANI,3)
    def update(self):
        self.spawntime -= random.randrange(0,10)
        if self.spawntime <= 0:
            self.spawn()
            self.spawntime = 1000
    def spawn(self):
        babymolds.append(babymold(self.Pos))

class roket(type):
    def __init__(self,pos,target):
        self.type = type.LIVING
        self.Pos = pos
        self.target:antiseptic = target
    def update(self,elapsed):
        self.go(elapsed)
    def go(self,elapsed):
        self.Pos = gothere(self.Pos,self.target.Pos,5,elapsed)
    def get_img(self,width,height):
        pass
class micomoldroket(roket):
    def __init__(self,pos,target):
        self.type = type.LIVING
        self.Pos = pos
        self.target = target
    def get_img(self,width,height):
        return pygame.transform.scale(MICOMOLDROKET_IMG,(width,height))
class headmoldroket(roket):
    def __init__(self,pos,target):
        self.type = type.LIVING
        self.Pos = pos
        self.target = target
    def get_img(self,width,height):
        return pygame.transform.scale(HEADMOLDROKET_IMG,(width,height))

class babymold(type):
    def __init__(self,pos):
        self.type = type.LIVING
        self.Pos = pos
        self.flyvec = []
        self.flyvec = [random.randrange(-200,200)+self.Pos[0],random.randrange(-200,200)+self.Pos[1]]
        self.changevec = 3
        self.fctime = time.time()
        self.growtime = 1000
        self.animation = animation(animation.BABYMOLD_ANI,6)
    def update(self,elsped):
        self.growtime -= random.randrange(0,100)*elsped
        if self.growtime <= 0:
            self.grow()
        self.randommove(elapsed)
    def randommove(self,elsped):
        if time.time()-self.fctime > self.changevec:
            self.fctime = time.time()
            self.flyvec = [random.randrange(-200,200)+self.Pos[0],random.randrange(-200,200)+self.Pos[1]]
        self.Pos = gothere(self.Pos,self.flyvec,20,elsped)
    def grow(self):
        babymolds.remove(self)
        if random.randrange(0,2) == 1:
            micomolds.append(micomold(0,self.Pos))
class antiseptic(type): #방부제
    def __init__(self,pos):
        self.type = type.LIVING
        self.Pos = pos
        self.animation = animation(animation.ANTISEPTIC_ANI,3)
class tansuuuuuu(type): #탄수화물
    def __init__(self):
        self.type = type.FOOD
        self.pos = [0,0]
        self.animation = animation(3)
        
class dannnnnnnn(type): #단백질
    def __init__(self):
        self.type = type.FOOD
        self.pos = [0,0]
        self.animation = animation(3)

class zzzzziiiii(type): #지방
    def __init__(self):
        self.type = type.FOOD
        self.pos = [0,0]
        self.animation = animation(3)

def move_headmold(elapsed):
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        HEADMOLD.w(elapsed)
        print("w")
    if pressed_key[pygame.K_a]:
        HEADMOLD.a(elapsed)
        print("a")
    if pressed_key[pygame.K_s]:
        HEADMOLD.s(elapsed)
        print("s")
    if pressed_key[pygame.K_d]:
        HEADMOLD.d(elapsed)
        print("d")

def ToTuple(list):
    return (list[0],list[1])

def AddCamPos(list):
    return [list[0]-camPos[0],list[1]-camPos[1]]

def controlForCenter(list): #위치를 화면 가운데로 만들기 위한 함수
    return [list[0]+screen_width/2,list[1]+screen_height/2]

def controlForCenter2(list,width,height):
    return [list[0]-width/2,list[1]-height/2]

def get_posforscreen(list,img_width,img_height):
    re = list
    re = AddCamPos(re)
    re = get_pxpercell(re)
    re = controlForCenter(re)
    re = controlForCenter2(re,img_width,img_height)
    re = ToTuple(re)
    return re

def get_posforscreen2(pos,img_width,img_height): 
    re = pos
    re = AddCamPos(re)
    re = get_pxpercell(re)
    re = controlForCenter2(re,img_width,img_height)
    re = ToTuple(re)
    return re

def gothere(pos,there,distance_,elsped):
    #print(elsped)
    distance = distance_*elsped
    dx = there[0] - pos[0]
    dy = there[1] - pos[1]
    dxy = math.sqrt(dx**2 + dy**2)
    if dxy <= 12:
        return pos
    dxdis = dx*(distance/dxy)
    dydis = dy*(distance/dxy)
    #print(dxdis)
    return [dxdis+pos[0],dydis+pos[1]]

def get_pxpercell(cell):
    return OneCellPerPx*cell

class upgrade:
    SRL = 1 #skill reloading 
    SRL_MAX = 5
    def getSRLV():# srl value
        re = 1
        if upgrade.SKILLRELOADING == 2:
            re = 0.8
        elif upgrade.SKILLRELOADING == 3:
            re = 0.5
        elif upgrade.SKILLRELOADING == 4:
            re = 0.2
        elif upgrade.SKILLRELOADING == 5:
            re = 0.1
        elif upgrade.SKILLRELOADING == 6:
            re = 0.02
        return re
    SL = 1 #speed
    S_MAX = 5
    def getSV():
        re = 1
        if upgrade.SL == 2:
            re = 1.2
        elif upgrade.SL == 3:
            re = 1.5
        elif upgrade.SL == 4:
            re = 2
        elif upgrade.SL == 5:
            re = 2.5
        elif upgrade.SL == 6:
            re = 5
    


HEADMOLDSIZE = get_pxpercell(1)
MICOMOLDSIZE = get_pxpercell(0.5)
BABYMOLDSIZE = get_pxpercell(0.3)
ANTISEPTICSIZE = get_pxpercell(0.5)
ROKETSIZE = get_pxpercell(0.2)

HEADMOLD = mold()
micomolds:list[micomold] = [micomold(1,[499,499])]
babymolds:list[babymold] = [babymold([499,499])]
antiseptics:list[antiseptic] = [antiseptic([450,450])]
rokets:list[roket] = [headmoldroket([499,499],antiseptics[0])]


camPos = [0,0]

LOBBY = 0
INGAME = 1
loc = 1 #로비와 인게임 상태를 저장
running = True #역시 chat gptㅎㅎ 이거 제출 직전에 지워야됨
while running:
    elapsed = clock.get_time()/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            new_width, new_height = event.size
            screen_width = new_width
            screen_height = new_height
            main_bread = pygame.transform.scale(MAIN_BREAD,(screen_width,screen_height))
            OneCellPerPx = int(max(screen_width,screen_height)/10)
            HEADMOLDSIZE = get_pxpercell(1)
            MICOMOLDSIZE = get_pxpercell(0.5)
            BABYMOLDSIZE = get_pxpercell(0.3)
            ROKETSIZE = get_pxpercell(0.2)
            ANTISEPTICSIZE = get_pxpercell(0.5)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                print("f")


    screen.fill((100,100,100))

    if loc == LOBBY:
        screen.blit(main_bread,(0,0))
    elif loc == INGAME:
        move_headmold(elapsed)
        camPos = HEADMOLD.HeadPos
        print(camPos)
        print(get_posforscreen(HEADMOLD.HeadPos,HEADMOLDSIZE,HEADMOLDSIZE))
        for bm in babymolds:
            bm.update(elapsed)
        for mm in micomolds:
            mm.update()
        for a in antiseptics:
            pass
        for r in rokets:
            r.update(elapsed)
            
        for mm in micomolds:
            screen.blit(mm.animation.update(MICOMOLDSIZE,MICOMOLDSIZE),get_posforscreen2(mm.Pos,MICOMOLDSIZE,MICOMOLDSIZE))
        for bm in babymolds:
            screen.blit(bm.animation.update(BABYMOLDSIZE,BABYMOLDSIZE),get_posforscreen2(bm.Pos,BABYMOLDSIZE,BABYMOLDSIZE))
        for a in antiseptics:
            screen.blit(a.animation.update(ANTISEPTICSIZE,ANTISEPTICSIZE),get_posforscreen2(a.Pos,ANTISEPTICSIZE,ANTISEPTICSIZE))
        for r in rokets:
            screen.blit(r.get_img(ROKETSIZE,ROKETSIZE),get_posforscreen2(r.Pos,ROKETSIZE,ROKETSIZE))
        screen.blit(HEADMOLD.animation.update(HEADMOLDSIZE,HEADMOLDSIZE),get_posforscreen(HEADMOLD.HeadPos,BABYMOLDSIZE,BABYMOLDSIZE))
    pygame.display.flip()

    clock.tick(60) #초당 60프레임
pygame.quit()
print('도윤이바보멍청이아님이 맞음')
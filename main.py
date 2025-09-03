import pygame
import time

pygame.init()

screen_width = 300 #적정 스크린 사이즈:3000(메인 빵 이미지 크기)
screen_height = 300 #적정 스크린 사이즈:2500(메인 빵 이미지 크기)
#6:5

screen = pygame.display.set_mode((screen_width,screen_height) , pygame.RESIZABLE)

clock = pygame.time.Clock()

MapSize = (2500,3000)

OneCellPerPx = max(screen_width,screen_height)/15

MAIN_BREAD = pygame.image.load('./img/main_bread.png')
main_bread = MAIN_BREAD #화질이 깨져서 원본 하나 해두고 복사본을 바꾸면서 쓰기
HEADMOLD_IMG0001 = pygame.image.load('./animation_headmold/headmold_animation0001.png')
meadmold_img0001 = HEADMOLD_IMG0001
HEADMOLD_IMG0002 = pygame.image.load('./animation_headmold/headmold_animation0002.png')
meadmold_img0002 = HEADMOLD_IMG0001
HEADMOLD_IMG0003 = pygame.image.load('./animation_headmold/headmold_animation0003.png')
meadmold_img0003 = HEADMOLD_IMG0001

main_bread = pygame.transform.scale(MAIN_BREAD,(screen_width,screen_height))

class type:
    ANIMATION = 0
    LIVING = 1
    FOOD = 2
    def __init__(self):
        self.type = ""
class animation(type):
    def __init__(self,fps):
        self.type = type.ANIMATION
        self.progress = 1
        self.fps = fps
        self.fftime = time.time() #처음 프레임이 나왔던 시간 'f'irst 'f'rame time
    def get_animation(self,width,height):
        if self.progress == 1:
            return pygame.transform.scale(HEADMOLD_IMG0001,(width,height))
        elif self.progress == 2:
            return pygame.transform.scale(HEADMOLD_IMG0002,(width,height))
        elif self.progress == 3:
            return pygame.transform.scale(HEADMOLD_IMG0003,(width,height))
    def update(self,width,height):
        if time.time()-self.fftime > 1/self.fps*self.progress:
            if self.progress >= 3:
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
        self.animation = animation(3)
    def w(self):
        self.HeadPos[1]-=0.5
    def a(self):
        self.HeadPos[0]-=0.5
    def s(self):
        self.HeadPos[1]+=0.5
    def d(self):
        self.HeadPos[0]+=0.5

class micomold(type): #곰팡이 노비
    def __init__(self,rating):
        self.type = type.LIVING
        self.Pos = [0,0]
        self.helth = 100
        self.animation = animation(3)

class antiseptic(type): #방부제
    def __init__(self):
        self.type = type.LIVING
        self.Pos = [0,0]
        self.animation = animation(3)
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

def move_headmold():
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        HEADMOLD.w()
        print("w")
    if pressed_key[pygame.K_a]:
        HEADMOLD.a()
        print("a")
    if pressed_key[pygame.K_s]:
        HEADMOLD.s()
        print("s")
    if pressed_key[pygame.K_d]:
        HEADMOLD.d()
        print("d")

def ToTuple(list):
    return (list[0],list[1])

def AddCamPos(list):
    return [list[0]-camPos[0],list[1]-camPos[1]]

def controlForCenter(list):
    return [list[0]+screen_width/2,list[1]+screen_height/2]

def controlForCenter2(list):
    return [list[0]/2,list[1]+screen_height/2]

def get_posforscreen(list):
    return ToTuple(controlForCenter(AddCamPos(list)))


HEADMOLD = mold()
micomolds:list[micomold] = []
antiseptics:list[antiseptic] = []

camPos = [0,0]

LOBBY = 0
INGAME = 1
loc = 1 #로비와 인게임 상태를 저장
running = True #역시 chat gptㅎㅎ 이거 제출 직전에 지워야됨
while running:
    elapsed = clock.get_time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            new_width, new_height = event.size
            screen_width = new_width
            screen_height = new_height
            main_bread = pygame.transform.scale(MAIN_BREAD,(screen_width,screen_height))

    screen.fill((0,0,0))

    if loc == LOBBY:
        screen.blit(main_bread,(0,0))
    elif loc == INGAME:
        move_headmold()
        #camPos = HEADMOLD.HeadPos
        print(get_posforscreen(HEADMOLD.HeadPos))
        screen.blit(HEADMOLD.animation.update(200,200),get_posforscreen(HEADMOLD.HeadPos))
    pygame.display.flip()

    clock.tick(60) #초당 60프레임
pygame.quit()
print('도윤이바보멍청이아님')
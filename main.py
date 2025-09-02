import pygame

pygame.init()

screen_width = 300 #적정 스크린 사이즈:3000(메인 빵 이미지 크기)
screen_height = 300 #적정 스크린 사이즈:2500(메인 빵 이미지 크기)
#6:5

screen = pygame.display.set_mode((screen_width,screen_height) , pygame.RESIZABLE)

clock = pygame.time.Clock()

MapSize = (2500,3000)

MAIN_BREAD = pygame.image.load('.\img\main_bread.png')
main_bread = MAIN_BREAD #화질이 깨져서 원본 하나 해두고 복사본을 바꾸면서 쓰기

main_bread = pygame.transform.scale(MAIN_BREAD,(screen_width,screen_height))

class mold: #곰팡이
    def __init__(self):
        self.HeadPos = [500,500]
        self.micomolds:list[micomold] = []
    def w(self):
        self.HeadPos[1]+=0.5
    def a(self):
        self.HeadPos[0]-=0.5
    def s(self):
        self.HeadPos[1]-=0.5
    def d(self):
        self.HeadPos[0]+=0.5

class micomold: #곰팡이 노비
    def __init__(self,rating):
        self.Pos = (0,0)
        self.helth = 100

class antiseptic: #방부제
    def __init__(self):
        self.Pos = (0,0)
class tansuuuuuu:
    def __init__(self):
        pass


HEADMOLD = mold()
micomolds:list[micomold] = []
antiseptics:list[antiseptic] = []

camPos = [0,0]
def move_headmold():
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        HEADMOLD.w()
        print("w")
    elif pressed_key[pygame.K_a]:
        HEADMOLD.a()
        print("a")
    elif pressed_key[pygame.K_s]:
        HEADMOLD.s()
        print("s")
    elif pressed_key[pygame.K_d]:
        HEADMOLD.d()
        print("d")
def get_img(progress):
    if progress == 1:
        return pygame.image.load('headmold_animation0001.png')
    elif progress == 2:
        return pygame.image.load('headmold_animation0002.png')
    elif progress == 3:
        return pygame.image.load('headmold_animation0003.png')
loc = 0 #로비와 인게임 상태를 저장
LOBBY = 0
INGAME = 0
running = True #역시 chat gptㅎㅎ 이거 제출 직전에 지워야됨
while running:
    elapsed = clock.get_time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 사용자가 창 크기를 변경했을 때 발생하는 이벤트 처리 (선택 사항)
        elif event.type == pygame.VIDEORESIZE:
            # 새로운 창 크기를 가져옵니다.
            new_width, new_height = event.size
            screen_width = new_width
            screen_height = new_height
            main_bread = pygame.transform.scale(MAIN_BREAD,(screen_width,screen_height))

    screen.fill((0,0,0))

    if loc == LOBBY:
        pass
    elif loc == INGAME:
        move_headmold()
        camPos = HEADMOLD.HeadPos
    screen.blit(main_bread,(0,0))
    pygame.display.flip()

    clock.tick(60) #초당 60프레임
pygame.quit()
print('도윤이바')
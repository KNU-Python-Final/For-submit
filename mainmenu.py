#23.11.15
#이스터에그 하나 추가함 -> score 1라운드와 연결
#23.11.16
#사운드 추가함
#23.11.17
#옵션 추가 중
#옵션에서 나올 시 이스터에그 다시 생기는 버그 발견 -> 해결
#back 눌렀을 때도 설정 바뀌는 오류 발견ㄴ....ㅜㅜㅜㅠ => 리스트로 그 전 눌ㄹ렀던 애들 받으면 답 없음. 무한루프라 1111111이런식으로 나옴.
#23.11.20
#1~3라운드 다 이음
import pygame
import time
import sys
import pacman_2
import option
import resources.save_files

sound = 1

pygame.mixer.init() #사운드 초기화
pygame.init() #pygame 초기화

WIDTH = 900
HEIGHT = 950 #창 가로세로 상수로 정해두고 시작 ->이거 해상도마다 다르게 보일 수 있음
fps = 60
timer = pygame.time.Clock() #속도 제어 위해서
screen = pygame.display.set_mode([WIDTH, HEIGHT]) #창 가로세로 정하기


easter_egg1=[0,0,0,0,0,0] #1번 이스터 조건
easter = 0 # 1번 이스터 상자를 떨궜는지
easter_now = [0,0] #이스터 에그 발견 현황 -> 1번 이스터 상자 열기까지 했는지
global score # score 공유 -> 이스터 에그 때문
global is_earned
is_earned = False

score = 0
score, selected_image = resources.save_files.load()

# 사운드 가져오기
click_easter = pygame.mixer.Sound("assets/sounds/click_easter.wav")
open_the_box = pygame.mixer.Sound("assets/sounds/open_the_box.wav")
box_drop = pygame.mixer.Sound("assets/sounds/box_drop.wav")
button_sound = pygame.mixer.Sound("assets/sounds/button.wav")
button_sound.set_volume(0.5)

def Button(img, click_img, x, y, width, height, sound , score = None, action = None,func = None): #sound : 소리 여부    action : 실행할 함수  func : 어떤 함수에서 들어갔는지 -> main_menu에서 들어갈 떄만 실행되는 애 있었으면 해서..
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()#클릭시
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        screen.blit(click_img,(x,y))
        if func != None:
            pygame.draw.polygon(screen, (195,195,195), [[x-50, y+height//2 - 20], [x-50,y+height//2+20], [x-30, y+height//2]], 5)
        if click[0] and action != None and score != None: #왼쪽 마우스 눌린 경우 + 이후 실행할 함수 있는 경우 + score주는 경우 -> 걍 사실상 pacman실행
            if func != None:
                pygame.draw.polygon(screen, (255, 255, 255),
                                [[x - 50, y + height // 2 - 20], [x - 50, y + height // 2 + 20],
                                 [x - 30, y + height // 2]], 5)
                pygame.draw.polygon(screen, 'Red', [[x - 50, y + height // 2 - 20], [x - 50, y + height // 2 + 20],
                                                [x - 30, y + height // 2]], 5)
            pygame.display.flip()
            if sound == 1:
                button_sound.play(0)
            time.sleep(1) #1초 지연
            action(score)
        elif click[0] and action != None and score == None:
            if func != None:
                pygame.draw.polygon(screen, (255, 255, 255),
                                [[x - 50, y + height // 2 - 20], [x - 50, y + height // 2 + 20],
                                 [x - 30, y + height // 2]], 5)
                pygame.draw.polygon(screen, 'Red', [[x - 50, y + height // 2 - 20], [x - 50, y + height // 2 + 20],
                                                [x - 30, y + height // 2]], 5)
            pygame.display.flip()
            if sound == 1:
                button_sound.play(0)
            time.sleep(1)  # 1초 지연
            action()
        elif click[0] and action == None: #왼쪽 마우스 눌린 경우 + 이후 실행할 함수 없는 경우 -> 아직 버튼에 함수 안 이은 상태일 때
            if func != None:
                pygame.draw.polygon(screen, (255, 255, 255), [[x - 50, y + height // 2 - 20], [x - 50, y + height // 2 + 20],
                                                    [x - 30, y + height // 2]], 5)
                pygame.draw.polygon(screen, 'Red', [[x - 50, y + height // 2 - 20], [x - 50, y + height // 2 + 20],
                                                [x - 30, y + height // 2]], 5)
            pygame.display.flip()
            if sound == 1:
                button_sound.play(0)
    else:
        if func != None:
            pygame.draw.polygon(screen, (0, 0, 0),[[x - 50, y + height // 2 - 20], [x - 50, y + height // 2 + 20], [x - 30, y + height // 2]],5)
        screen.blit(img, (x, y))
        pygame.display.flip()


def chain_letters(easter_now,sound): #이스터 에그 보물상자 열 경우 텍스트와 사운드~ sound : 소리여부
    if easter_now[0] == 0 and sound == 1:
        open_the_box.play(0)
    easter_now[0] = 1
    font = pygame.font.Font("assets/pacman_main_menu_images/NPSfont_regular.ttf", 26)
    chain_letter = font.render(f'강남대 구모씨가 숨긴 이스터에그를 발견하셨습니다! 남은 이스터에그 :  {easter_now.count(1)}개', True,
                            'green')
    screen.blit(chain_letter, (50, 400))
    chain_letter = font.render(f'Extra Coin +100000', True,
                               'red')
    screen.blit(chain_letter, (300, 450))
    global score
    global is_earned
    if not is_earned:
        score += 100000
        resources.save_files.save(score, selected_image)  # 게임 종료 시 점수 저장
        is_earned = True

def quitgame():
    pygame.quit()
    sys.exit()
def main_menu(WIDTH,HEIGHT,easter,easter_now,sound):
    screen.fill('black')  # 스크린 색
    pacman_logo = pygame.transform.scale(pygame.image.load(f'assets/pacman_main_menu_images/pacman_logo.png'), (600, 300))
    image = []

    #사운드 가져오기
    #bgm = pygame.mixer.Sound("assets/sounds/pacman_beginning.wav")

    #이미지 가져오기
    pacman = pygame.transform.scale(pygame.image.load(f'assets/pacman_main_menu_images/pacman.png'),(45, 45))
    black1 = pygame.transform.scale(pygame.image.load(f'assets/pacman_main_menu_images/black.png'), (45, 45))
    black2 = pygame.transform.scale(pygame.image.load(f'assets/pacman_main_menu_images/black.png'), (150, 120))
    red_ghost = pygame.transform.scale(pygame.image.load(f'assets/pacman_main_menu_images/red_ghost.png'),(45,45))
    blue_ghost = pygame.transform.scale(pygame.image.load(f'assets/pacman_main_menu_images/blue_ghost.png'), (45, 45))
    pink_ghost = pygame.transform.scale(pygame.image.load(f'assets/pacman_main_menu_images/pink_ghost.png'), (45, 45))
    orange_ghost = pygame.transform.scale(pygame.image.load(f'assets/pacman_main_menu_images/orange_ghost.png'), (45, 45))
    start_img = pygame.transform.scale(pygame.image.load(f'assets/pacman_main_menu_images/START.png'), (208,50))
    options_img = pygame.transform.scale(pygame.image.load(f'assets/pacman_main_menu_images/OPTIONS.png'), (230, 65))
    exit_img = pygame.transform.scale(pygame.image.load(f'assets/pacman_main_menu_images/EXIT.png'),(160, 52))
    click_start_img = pygame.transform.scale(pygame.image.load(f'assets/pacman_main_menu_images/CLICK_START.png'), (208, 50))
    click_options_img = pygame.transform.scale(pygame.image.load(f'assets/pacman_main_menu_images/CLICK_OPTIONS.png'),(230, 65))
    click_exit_img = pygame.transform.scale(pygame.image.load(f'assets/pacman_main_menu_images/CLICK_EXIT.png'), (160, 52))
    closed_treasure_box = pygame.transform.scale(pygame.image.load(f'assets/pacman_main_menu_images/closed_treasure_box.png'), (150, 120))
    opened_treasure_box = pygame.transform.scale(pygame.image.load(f'assets/pacman_main_menu_images/opened_treasure_box.png'),
                                            (150, 120))



    image.append(pacman)
    image.append(red_ghost)
    image.append(pink_ghost)
    image.append(blue_ghost)
    image.append(orange_ghost)
    light_yellow = (255, 255, 150)

    menu = True
    while menu:

        for event in pygame.event.get():  # 모든 이벤트들 리스트로 해서 event에 하나씩 for문으로 넣어줌
            if event.type == pygame.QUIT:
                quitgame()
            #이스터에그 -> 모든 유령과 팩맨, 코인 눌러서 없애기
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #왼쪽 마우스 클릭
                    mouse_x, mouse_y = event.pos
                    for i in range(len(image)):
                        if WIDTH // 2 - 100 + i*50 + 45 > mouse_x > WIDTH // 2 - 100 + i*50 and 370 + 45 > mouse_y > 370 and not easter and not easter_now[0]:
                            if easter_egg1[i] == 0 and sound == 1:
                                click_easter.play(0)
                            easter_egg1[i] = 1
                            screen.blit(black1,(WIDTH // 2 - 100 + i*50, 370))
                    if WIDTH // 2 - 125 + 10 > mouse_x > WIDTH // 2 - 125 - 10 and 405 > mouse_y > 385 and not easter and not easter_now[0]:
                        if easter_egg1[5] == 0 and sound == 1:
                            click_easter.play(0)
                        easter_egg1[5] = 1
                        screen.blit(black1, (WIDTH // 2 - 125 - 10, 395 - 10))
                    #이스터에그 깨고 보물상자 나와서 그 보물상자 누르면 -> 보물상자 열리고 행운의 편지 등장
                    elif (WIDTH//2 - 75 + 150 > mouse_x > WIDTH//2 - 75) and (350+120 > mouse_y > 350) and easter: #상자 나왔지만 아직 안 열었음
                        screen.blit(black2, (WIDTH // 2 - 75, 350))
                        screen.blit(opened_treasure_box, (WIDTH // 2 - 75, 350))
                        time.sleep(1/4)  # 1초 지연
                        chain_letters(easter_now,sound)
                        pygame.display.flip()
        if easter and easter_now[0]:
            screen.blit(opened_treasure_box, (WIDTH // 2 - 75, 350))
            chain_letters(easter_now,sound)

        screen.blit(pacman_logo, (WIDTH//2-300,100))
        if easter == False and easter_now[0] == False:
            # 그 이미지의 이스터에그 안눌렀을 때만 가능
            if easter_egg1[5] == 0:
                pygame.draw.circle(screen, light_yellow, (WIDTH // 2 - 125, 395), 10)
            for i in range(len(image)): #로고랑 그 메뉴들 사이에 있는 유령이랑 팩맨 이미지 그리기
                if easter_egg1[i] == 0:
                    screen.blit(image[i], (WIDTH // 2 - 100 + i*50, 370))


        # 이스터에그 조건 확인 -> 다 했으면 보물상자 등장
        if easter == False and easter_now[0] == False:
            for i in range(len(easter_egg1)):
                if easter_egg1.count(1) == 6:
                    time.sleep(1/8)  # 1초 지연
                    if easter == False:
                        if sound == 1:
                            box_drop.play(0)
                        easter = True
                        screen.blit(closed_treasure_box,(WIDTH//2 - 75 ,350))
                        pygame.display.flip()




        font = pygame.font.Font("assets/pacman_main_menu_images/neodgm.ttf", 30)
        #우리 이름
        name_text = font.render(f'파이썬 응용 - 구서연 김민재 양현준 이윤석', True,
                                                   'white')  # antialias : True -> 선 부드럽게..
        font = pygame.font.Font("assets/pacman_main_menu_images/emulogic.ttf", 30)
        screen.blit(name_text, (150, 0))

        resources.save_files.save(score, selected_image)  # 게임 종료 시 점수 저장
        startButton = Button(start_img, click_start_img, WIDTH // 2-208//2, 450+100, 208,50, sound, score, pacman_2.pacman,main_menu)
        opionButton = Button(options_img, click_options_img, WIDTH // 2 - 225 // 2, 450+200, 230, 65,sound,[easter,easter_now], action = option.options,func = main_menu)
        exitbutton = Button(exit_img, click_exit_img, WIDTH // 2 - 160 // 2, 450+330, 160, 52, sound,None, quitgame,func = main_menu)

        timer.tick(fps)
        pygame.display.flip()  # 화면 전체 업데이트
if __name__ == "__main__": # 여기 py안에서 실행될 때만
    main_menu(WIDTH,HEIGHT,easter,easter_now,sound)

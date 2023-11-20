import pygame
import random
import time
from datetime import datetime
import round3


def round2(player_score):
    # 1. 게임 초기화
    pygame.init()
    coin_list = []
    last_bullet_time = 0
    bullet_cooldown = 500  # 500ms = 0.5초

    # 2. 게임창 옵션 설정
    size = [900, 950]
    screen = pygame.display.set_mode(size)

    title = "2R"
    pygame.display.set_caption(title)

    # 3. 게임 내 필요한 설정
    clock = pygame.time.Clock()  # 시간

    class obj:
        def __init__(self):  # 초기화 함수
            self.x = 0
            self.y = 0
            self.move = 0

        def put_image(self, address):
            if address[-3:] == "png":  # png 파일인지 확인
                self.img = pygame.image.load(address).convert_alpha()  # png의 경우 투명도(alpha)를 지원
            else:
                self.img = pygame.image.load(address)
                self.sx, self.sy = self.img.get_size()

        def change_size(self, sx, sy):  # 이미지의 크기 변경
            self.img = pygame.transform.scale(self.img, (sx, sy))
            self.sx, self.sy = self.img.get_size()

        def show(self):  # 객체의 img를 x,y에 보여주기
            screen.blit(self.img, (self.x, self.y))

    '''
    .x = x축 위치, .y = y축 위치
    .sx = 가로 크기,.sy = 세로 크기
    '''

    # 점수 저장 함수
    def save_score(score):
        with open("score.txt", "w") as f:  # score.txt 파일을 쓰기모드("w")로 열기, with 구문을 사용하여 작업 후 파일 닫기
            f.write(str(score))  # score를 문자열로 파일에 기록

    # 점수 불러오기 함수
    '''
    try - except를 이용하여 예외(파일이 존재하지 않은 경우)를 처리
    '''

    # 히트박스
    def circle_crash(obj1, obj2):
        center1 = (obj1.x + obj1.sx / 2, obj1.y + obj1.sy / 2)
        center2 = (obj2.x + obj2.sx / 2, obj2.y + obj2.sy / 2)

        distance = ((center1[0] - center2[0]) ** 2 + (center1[1] - center2[1]) ** 2) ** 0.5  # 중심 사이의 거리 계산
        radius_sum = (obj1.sx / 2) + (obj2.sx / 2)

        return distance <= radius_sum


    # ss = SpaceShip = player
    ss = obj()

    pacman_images = []
    for i in range(1, 5):
        pacman_images.append(pygame.transform.scale(pygame.image.load(f'assets/player_images/{i}.png'), (50, 50)))

    ss.put_image("assets/player_images/1.png")  # 시작 이미지 설정
    ss.change_size(50, 50)  # 이미지 크기 조정

    ss.x = round(size[0] / 2 - ss.sx / 2)
    ss.y = size[1] - ss.sy - 15
    ss.move = 17  # 속도

    left_go = False
    right_go = False
    space_go = False

    bullet_list = []
    ghost_list = []

    black = (0, 0, 0)
    white = (255, 255, 255)
    k = 0

    is_gameovered = False
    kill = 0
    loss = 0

    # 4-0. 게임 시작 대기화면
    is_stopped = False  # Start/Stop Boolean
    while not is_stopped:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_stopped = True
        screen.fill(black)
        font = pygame.font.Font("assets/2round_images/SOYO.ttf", 20)
        text = font.render("PRESS SPACE KEY TO START THE GAME", True, (255, 255, 255))
        screen.blit(text, (245, round(size[1] / 2 - 50)))
        pygame.display.flip()

    # 4. 메인 이벤트
    start_time = datetime.now()
    is_stopped = False
    while not is_stopped:

        # 4-1. FPS 설정
        clock.tick(60)  # 60 fps
        current_time = pygame.time.get_ticks()  # 현재 시간을 밀리세컨드 단위로 가져옴

        # 4-2. 각종 입력 감지
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_stopped = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left_go = True
                elif event.key == pygame.K_RIGHT:
                    right_go = True
                elif event.key == pygame.K_SPACE:
                    space_go = True
                    k = 0
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left_go = False
                elif event.key == pygame.K_RIGHT:
                    right_go = False
                elif event.key == pygame.K_SPACE:
                    space_go = False
        current_image_index = k // 10 % len(pacman_images)  # 10프레임마다 이미지 변경
        ss.img = pacman_images[current_image_index]  # 현재 이미지 업데이트

        # 4-3. 입력, 시간에 따른 변화
        now_time = datetime.now()
        delta_time = round((now_time - start_time).total_seconds())

        if delta_time > 20:
            is_stopped = True
            is_gameovered = True
            TO = 1

        if left_go == True:
            ss.x = ss.x - ss.move
            # player가 왼쪽 밖으로 나가지 않도록 조정
            if ss.x < 0:
                ss.x = 0
        elif right_go == True:
            ss.x = ss.x + ss.move
            # player가 오른쪽 밖으로 나가지 않도록 조정
            if ss.x >= size[0] - ss.sx:
                ss.x = size[0] - ss.sx
        if space_go == True and player_score >= 10 and current_time - last_bullet_time > bullet_cooldown:  # 총알 속도 고정
            last_bullet_time = current_time  # 마지막 총알 발사 시간 업데이트
            # mm = 총알
            mm = obj()
            mm.put_image("assets/2round_images/bullet.png")
            mm.change_size(5, 15)
            mm.x = round(ss.x + ss.sx / 2 - mm.sx / 2)  # 총알의 히트박스
            mm.y = ss.y - mm.sy - 10  # player의 주둥이보다 조금 더 앞에서 총알이 나가도록 조정
            mm.move = 20
            bullet_list.append(mm)
            player_score -= 10  # score 차감
        '''
        if 문 밖에 k가 있는 이유 :
        k는 게임의 메인루프가 반복 될때마다 증가
        프레임마다 이미지를 변경할 수 있도록 함
        '''
        k = k + 1

        d_list = []  # delete list
        for i in range(len(bullet_list)):
            m = bullet_list[i]
            m.y = m.y - m.move
            if m.y <= - m.sy:
                d_list.append(i)
        for d in d_list:
            del bullet_list[d]

        if random.random() > 0.85:  # 20% 확률 (0 ~ 1)
            aa = obj()
            ghost_images = ["assets/2round_images/orange_ghost.png", "assets/2round_images/pink_ghost.png", "assets/2round_images/red_ghost.png", "assets/2round_images/blue_ghost.png"]
            ghost_image = random.randrange(0, 4)
            aa.put_image(ghost_images[ghost_image])  # 이미지를 반복하여 생성
            aa.change_size(40, 40)
            aa.x = random.randrange(0, size[0] - aa.sx - round(ss.sx / 2))  # 유령 x좌표
            aa.y = 10  # 유령 y좌표
            if ghost_image == 0:
                aa.move = 22
            elif ghost_image == 1:
                aa.move = 18
            elif ghost_image == 2:
                aa.move = 16
            elif ghost_image == 3:
                aa.move = 13

            ghost_list.append(aa)

        if random.random() > 0.9:  # 5% 확률로 코인 생성
            coin = obj()
            coin.put_image("assets/2round_images/coin.png")
            coin.change_size(20, 20)  # 코인의 크기 설정
            coin.x = random.randrange(0, size[0] - coin.sx)
            coin.y = 10  # 코인의 초기 위치
            coin.move = 8  # 코인의 이동 속도
            coin_list.append(coin)

        # 코인 이동
        coin_delete_list = []
        for i in range(len(coin_list)):
            c = coin_list[i]
            c.y = c.y + c.move
            if c.y >= size[1]:
                coin_delete_list.append(i)

        # 코인과 우주선의 충돌 감지
        for coin in coin_list[:]:
            if circle_crash(coin, ss):
                coin_list.remove(coin)
                player_score += 10  # 플레이어 점수 증가

        # 코인 삭제 로직
        for d in reversed(coin_delete_list):
            del coin_list[d]

        d_list = []
        for i in range(len(ghost_list)):
            a = ghost_list[i]
            a.y = a.y + a.move
            if a.y >= size[1]:
                d_list.append(i)
        d_list.reverse()
        for d in d_list:
            del ghost_list[d]
            loss = loss + 1

        dm_list = []
        da_list = []

        for i in range(len(bullet_list)):
            for j in range(len(ghost_list)):
                m = bullet_list[i]
                a = ghost_list[j]
                if circle_crash(m, a) == True:
                    dm_list.append(i)
                    da_list.append(j)
        dm_list = list(set(dm_list))
        da_list = list(set(da_list))

        for dm in dm_list:
            del bullet_list[dm]
        for da in da_list:
            del ghost_list[da]
            kill = kill + 1

        for i in range(len(ghost_list)):
            a = ghost_list[i]
            if circle_crash(a, ss) == True:
                is_stopped = True
                is_gameovered = True

        # 4-4. 그리기
        screen.fill(black)
        ss.show()
        for m in bullet_list:
            m.show()
        for a in ghost_list:
            a.show()
        for c in coin_list:
            c.show()

        font = pygame.font.Font("assets/2round_images/SOYO.ttf", 20)
        text_kill = font.render("killed : {} loss : {}".format(kill, loss), True, (255, 255, 0))
        screen.blit(text_kill, (10, 5))

        text_time = font.render("time : {}".format(delta_time), True, (255, 255, 255))
        screen.blit(text_time, (size[0] - 100, 5))

        text_score = font.render("score : {}".format(player_score), True, (255, 255, 255))
        screen.blit(text_score, (size[0] - 230, 5))

        # 4-5. 업데이트
        pygame.display.flip()

    # 5. 게임 종료
    while is_gameovered:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_score(player_score)  # 게임 종료 시 점수 저장
                is_gameovered = 0
        font = pygame.font.Font("assets/2round_images/SOYO.ttf", 40)
        text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(text, (320, round(size[1] / 2 - 50)))
        time.sleep(3)
        round3.round3(player_score)
        pygame.display.flip()
    pygame.quit()


round2(10000)
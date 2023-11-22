import pygame
import time
import resources.images.characters
import resources.save_files

def round3(score):
    pygame.init()

    player_score, selected_image = resources.save_files.load()

    # 초기 설정 및 이미지 로드
    WIDTH, HEIGHT = 900, 950
    screen = pygame.display.set_mode([WIDTH, HEIGHT]) # 창의크기 설정
    pygame.display.set_caption("3round") # 제목 설정

    font = pygame.font.SysFont('arial', 24)
    price_font = pygame.font.SysFont('arial', 30)
    shop_font = pygame.font.SysFont('arial', 40)
    button_font = pygame.font.SysFont('arial', 40)

    button_colors = [(255, 165, 0), (0, 191, 255), (255, 69, 0), (138, 43, 226), (128, 128, 128)] # 버튼의 색상(RGB) 지정

    # 이미지 경로 지정
    
    exit_image_path = './assets/3round_images/etc/exit.png'
    background_image_path = './assets/3round_images/etc/bg.png'

    exit_img = pygame.transform.scale(pygame.image.load(exit_image_path), (40, 40))
    background_image = pygame.image.load(background_image_path)

    def get_image(name):
            return pygame.transform.scale(pygame.image.load(resources.images.characters.get_image_path(selected_image)), (300, 300))

    prices = {
        resources.images.characters.king_str : 100000,
        resources.images.characters.angel_str: 60000,
        resources.images.characters.leaf_str: 80000,
        resources.images.characters.santa_str: 90000
    }
    selected_price = None
    selected_image = ''
    buy_button = None
    insufficient_score_message = False
    message_start_time = 0

    player_score = score
    run = True
    while run:
        screen.blit(background_image, (0, 0))

        # 버튼 4개 그리기
        button_king = pygame.draw.rect(screen, button_colors[0], (70, 215, 300, 70)) # x좌표, y좌표, 너비, 높이
        button_angel = pygame.draw.rect(screen, button_colors[1], (70, 475, 300, 70))
        button_leaf = pygame.draw.rect(screen, button_colors[2], (70, 345, 300, 70))
        button_santa = pygame.draw.rect(screen, button_colors[3], (70, 605, 300, 70))

        for event in pygame.event.get(): # 이벤트 순회
            if event.type == pygame.QUIT:
                run = False # 창 끄기
            if event.type == pygame.MOUSEBUTTONDOWN: # 마우스 버튼을 클릭했을 때
                mouse_pos = event.pos # 클릭한 위치를 변수에 지정
                if button_king.collidepoint(mouse_pos): # button_king의 좌표 안에서 마우스 클릭 했다면
                    selected_image = resources.images.characters.king_str # 이미지 업데이트
                    selected_price = prices[resources.images.characters.king_str]
                elif button_angel.collidepoint(mouse_pos):
                    selected_image = resources.images.characters.angel_str
                    selected_price = prices[resources.images.characters.angel_str]
                elif button_leaf.collidepoint(mouse_pos):
                    selected_image = resources.images.characters.leaf_str
                    selected_price = prices[resources.images.characters.leaf_str]
                elif button_santa.collidepoint(mouse_pos):
                    selected_image = resources.images.characters.santa_str
                    selected_price = prices[resources.images.characters.santa_str]
                
                if buy_button and buy_button.collidepoint(mouse_pos):
                    if player_score >= selected_price:
                        player_score -= selected_price
                        resources.save_files.save(player_score, selected_image)
                    # elif player_score < selected_price:
                    #     print("점수가 부족합니다")
                    else:
                        insufficient_score_message = True
                        message_start_time = time.time()

                elif button_heart_version.collidepoint(mouse_pos):
                    if selected_image == 'king':
                        selected_image = 'heart_king'
                    elif selected_image == 'heart_king':
                        selected_image = 'king'
                    if selected_image == 'angel':
                        selected_image = 'heart_angel'
                    elif selected_image == 'heart_angel':
                        selected_image = 'angel'
                    if selected_image == 'leaf':
                        selected_image = 'heart_leaf'
                    elif selected_image == 'heart_leaf':
                        selected_image = 'leaf'
                    if selected_image == 'santa':
                        selected_image = 'heart_santa'
                    elif selected_image == 'heart_santa':
                        selected_image = 'santa'

                elif restart_button.collidepoint(mouse_pos):
                    run = False
                elif exit_button.collidepoint(mouse_pos):
                    run = False

        if not selected_image == '': # 이미지가 할당 되었는지 확인 (비어있지 않다면)
            screen.blit(get_image(selected_image), (500, 300)) # 500, 300에 지정된 이미지 그리기
            buy_button = pygame.draw.rect(screen, button_colors[4], (520, 675, 250, 50)) # (520, 675)에 250x50 크기의 버튼 생성
            buy_text = button_font.render('BUY', True, (255, 255, 255)) # 텍스트 생성
            # buy_button 중앙에 buy_text 배치
            screen.blit(buy_text, (buy_button.x + (buy_button.width - buy_text.get_width()) // 2, buy_button.y + (buy_button.height - buy_text.get_height()) // 2))
            if selected_price is not None:
                price_text = price_font.render(f'{selected_price}', True, (255, 255, 255))
                screen.blit(price_text, (520, 640))  # 가격 텍스트 위치 조정 필요
        score_text = font.render(f'Score: {player_score}', True, (255, 255, 255)) # 텍스트 렌더링
        screen.blit(score_text, (10, 10)) # 렌더링된 텍스트를 화면에 표시

        king_text = font.render('King', True, (0, 0, 0)) # king_text 렌더링
        angel_text = font.render('Angel', True, (0, 0, 0)) # angel_text 렌더링
        leaf_text = font.render('Leaf', True, (0, 0, 0)) # leaf_text 렌더링
        santa_text = font.render('Santa', True, (0, 0, 0)) # Santo_text 렌더링

        button_texts = [king_text, angel_text, leaf_text, santa_text]
        button_positions = [(70, 215), (70, 475), (70, 345), (70, 605)] # 버튼의 위치 지정
        # button_texts, button_position을 결합하여 새로운 튜플 생성 >> text 와 text의 좌표를 생성
        for text, (x, y) in zip(button_texts, button_positions):
            screen.blit(text, (x + 150 - text.get_width() // 2, y + 35 - text.get_height() // 2)) # 텍스트를 버튼의 중앙에 오도록 배치

        button_heart_version = pygame.draw.rect(screen, (255, 255, 255), (550, 250, 30, 30))
        exit_button = pygame.draw.rect(screen, (255, 255, 255), (860, 910, 40, 40))
        restart_button = pygame.draw.rect(screen, (255, 255, 255), (820, 910, 40, 40))


        shop_text = shop_font.render('SHOP', True, (255, 255, 255)) # shop 렌더링
        shop_text_rect = shop_text.get_rect(center=(WIDTH // 2, 50)) # shop rect 렌더링
        pygame.draw.rect(screen, (128, 128, 128), shop_text_rect.inflate(20, 20)) # inflate = 사각형을 텍스트 영역보다 20 픽셀씩 크기 생성
        screen.blit(shop_text, shop_text_rect) # 렌더링된 텍스트를 화면에 표시
        
        if insufficient_score_message:
            current_time = time.time()
            if current_time - message_start_time <= 1:  # 1초간 메시지 표시
                insufficient_score_text = font.render("No score", True, (255, 0, 0))
                screen.blit(insufficient_score_text, (WIDTH / 2 - insufficient_score_text.get_width() / 2, HEIGHT / 2))
            else:
                insufficient_score_message = False  # 1초가 지나면 메시지 표시를 중단

        screen.blit(exit_img, exit_button.topleft)
        pygame.display.update()

    pygame.quit()
round3(100000)
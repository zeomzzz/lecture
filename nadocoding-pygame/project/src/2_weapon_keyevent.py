import os # os 모듈 : 운영체제와의 상호작용을 도움
import pygame

#################################################################
# 기본 초기화 (반드시 해야 하는 것)
pygame.init() # 초기화

# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Pang")

# FPS
clock = pygame.time.Clock()

#################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기 : 스테이지 위에서 캐릭터가 좌우로 이동
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # stage 높이 계산해서 그 높이 위에서 공 튀김, 캐릭터를 위치

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

# 캐릭터 이동 방향
character_to_x = 0

# 캐릭터 이동 속도
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한 번에 여러 발 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 10

# 이벤트 루프
running = True
while running :
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT : 
            running = False
        
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT : # 캐릭터를 왼쪽으로
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT : # 캐릭터를 오른쪽으로
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE : # space 누르면 무기 발사
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2) # 캐릭터의 중앙에 무기를 추가
                weapon_y_pos = character_y_pos # 캐릭터의 머리 위에서 무기 발사
                weapons.append([weapon_x_pos, weapon_y_pos]) # 무기 리스트에 무기 위치 추가

        if event.type == pygame.KEYUP : # KEYUP 하면 더 이상 움직이지 않음
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                character_to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width
    
    # 무기 위치 조정 : y좌표만 변경
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons] # 무기 위치를 위로 올림

    # 천장에 닿은 무기 없애기
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0] # 천장에 닿지 않은 무기만 저장
    
    # 4. 충돌 처리 (이미지 간의 충돌 처리)
    
    # 5. 화면에 그리기 (코드 순서대로 그려짐)
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons : # 무기 list의 모든 무기를 그리도록 for문 사용
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()
import pygame
import random

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Game Quiz1") # 게임 이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("/Users/zeommi/Documents/python/pygame_basic/background.png")

# 캐릭터 불러오기
character = pygame.image.load("/Users/zeommi/Documents/python/pygame_basic/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)  # 가로 : 화면 중앙
character_y_pos = screen_height - character_height # 세로 : 화면 가장 아래

# 이동할 좌표
to_x = 0

# 이동 속도
character_speed = 0.6

# 적 enemy 캐릭터
enemy = pygame.image.load("/Users/zeommi/Documents/python/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = random.uniform(0, screen_width - enemy_width) # x좌표는 랜덤
enemy_y_pos = 0 # 화면 가장 위
enemy_speed = 12

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트(None = Default), 크기)

# 총 시간
total_time = 60

# 시작 시간
start_ticks = pygame.time.get_ticks() # 현재 tick을 받아옴

# 이벤트 루프
running = True # 게임이 진행중인가?
while running :
    dt = clock.tick(60) # 게임 화면의 초당 프레임 수를 설정

    for event in pygame.event.get() : # 어떤 이벤트가 발생 하였는가?
        if event.type == pygame.QUIT : # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님
        if event.type == pygame.KEYDOWN : # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT : # 캐릭터 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT : # 캐릭터를 오른쪽으로
                to_x += character_speed
        
        if event.type == pygame.KEYUP : # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0

    character_x_pos += to_x * dt

    # 가로 경계값 처리
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height :
        character_y_pos = screen_height - character_height
    
    # enemy 이동

    enemy_y_pos += enemy_speed

    if enemy_y_pos >= 640 :
        enemy_x_pos = random.uniform(0, screen_width - enemy_width)
        enemy_y_pos = 0

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos # enemy는 움직이지 않지만 enemy_rect에 정보 업데이트 하기 위해 설정 (안하면 그냥 그리기만 한게 됨)
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect) :
        print("충돌했어요")
        running = False
    
    screen.blit(background, (0, 0)) # 배경 그리기 : (0, 0) 게임 창의 맨 왼쪽 위. (0, 0) 기준으로 오른쪽 아래쪽으로 그려짐
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 캐릭터 그리기

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms인 경과 시간을 초(s)로 바꾸기 위해 /1000

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255)) # render : 실제로 글자를 그림 , ms 자르고 초 단위로만 남은 시간 표시하기 위해 int()
    # 출력할 글자(잔여 시간), True, 글자 색상
    screen.blit(timer, (10, 10)) # 타이머 그림

    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0 :
        print("타임아웃")
        running = False

    pygame.display.update() # 게임 화면을 다시 그리기 (이 부분이 없으면 background가 호출되지 않음)

# 종료 전 잠시 대기
pygame.time.delay(2000) # 2초(2000ms) 정도 대기

# running false 되면 pygame 종료
pygame.quit()
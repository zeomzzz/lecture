import pygame

pygame.init() # 초기화

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("/Users/zeommi/Documents/python/pygame_basic/background.png")

# 이벤트 루프
running = True # 게임이 진행중인가?
while running :
    for event in pygame.event.get() : # 어떤 이벤트가 발생 하였는가?
        if event.type == pygame.QUIT : # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님
    
    # screen.fill((0, 0, 255)) # 이미지 불러오지 않고 RGB 색상값 이용하여 채움
    screen.blit(background, (0, 0)) # 배경 그리기 : (0, 0) 게임 창의 맨 왼쪽 위. (0, 0) 기준으로 오른쪽 아래쪽으로 그려짐

    pygame.display.update() # 게임 화면을 다시 그리기 (이 부분이 없으면 background가 호출되지 않음)

# running false 되면 pygame 종료
pygame.quit()

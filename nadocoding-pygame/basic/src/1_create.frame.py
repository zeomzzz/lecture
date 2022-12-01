# pygame 잘 설치 됐는지 확인
import pygame

pygame.init() # 초기화 (pygame import 후 반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 어떤 창이 떳다가 사라짐 : 프로그램이 실행은 되는데 밑에 다른 프로그램이 없음. 그래서 창이 떳다가 바로 종료됨
# 따라서 프로그램이 종료되지 않도록 어디선가 대기해야함. 사용자가 키 입력하거나 마우스 움직이거나 하는 동작 검사하는 event roop 가 실행되고 있어서 창이 꺼지지 않음

# 이벤트 루프
running = True # 게임이 진행중인가?
while running :
    for event in pygame.event.get() : # 어떤 이벤트가 발생 하였는가? pygame 쓰기 위해 무조건 적어야 하는 부분. 이벤트 루프는 프로그램이 종료되지 않도록 대기하며 사용자 움직임 검사. 들어오면 맞는 움직임 할 것
        if event.type == pygame.QUIT : # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

# running false 되면 pygame 종료
pygame.quit()

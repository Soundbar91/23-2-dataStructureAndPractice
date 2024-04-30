from isValidPos import isValidPos
from Map import map
import os

# 미로 맵을 출력하는 함수
def drawMaze(here) :
    # 화면을 지우고 미로를 출력하기 위해 사용
    os.system('cls')
    # 가로와 세로의 크기를 저장할 변수 선언
    w = len(map[0])
    h = len(map)

    # 반복문을 통해 2차원 리스트에 저장된 미로를 출력
    # 0 = 길, 1 = 벽, . = 지나간 곳, x = 탈출구, e = 플레이어
    for i in range(h) :
        for j in range(w) :
            if map[i][j] == '0' : print('  ', end="")
            elif map[i][j] == '1' : print('■', end="")
            elif map[i][j] == '.' : print('√', end="")
            elif map[i][j] == 'x' : print('→', end="")
            elif map[i][j] == 'e' : print('★', end="")
        print()

    # 매개변수로 받은 현재 위치를 출력
    print("현재 위치:", here)
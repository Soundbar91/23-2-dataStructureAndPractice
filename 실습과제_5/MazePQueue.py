from PriorityQueue import *
from isValidPos import isValidPos
from DrawMaze import drawMaze
from Map import map
# 최소 거리를 계산하기 위해 포함한 모듈
import math
# 딜레이 기능을 사용하기 위해 포함한 모듈
import time

# 출구의 위치를 저장하는 변수
ox, oy = 0, 0

# 출구의 위치를 탐색하는 함수
def Find_Out() : 
    global ox, oy
    # 맵에서 출구의 위치를 탐색 후 ox, oy에 좌표를 저장
    for i in range(len(map)) :
        for j in range(len(map[0])) :
            if map[i][j] == 'x' : 
                ox, oy = j, i

# 현재의 위치에서 출구의 위치까지의 유클리디언 거리를 계산하여 반환
def dist(x, y) :
    (dx, dy) = (ox - x, oy - y)
    return math.sqrt(dx*dx + dy*dy)

# 최소거리를 통해 미로를 탐색하는 함수
def MySmartSearch(Initial_location) :
    # 출구의 위치를 찾는다
    Find_Out()
    # 우선순위 큐를 선언
    q = PriorityQueue(100)
    # 튜플에 초기 위치를 추가
    # 초기 위치와 초기 위치부터 출구의 위치까지의 유클리디언 거리를 우선순위 큐에 enqueue
    (x, y) = Initial_location
    q.enqueue((x, y, -(dist(x, y))))

    # 우선순위 큐가 공백 상태가 될 때까지 출구를 찾는다
    while not q.isEmpty() :
        # 우선순위 큐에서 요소를 반환 받는다.
        here = q.dequeue()
        x, y, _ = here

        # 우선순위 큐에서 반환 받은 요소(좌표)의 값이 x인 경우 탈출 성공
        if (map[y][x] == 'x') : 
            map[y][x] = 'e'
            drawMaze(here)
            return True

        # 그렇지 않은 경우, 그 위치로 움직이고 탐색을 한다.
        else :
            map[y][x] = 'e'
            # 위치의 값을 e로 변경
            # 상하좌우 순으로 탐색을 하고, 움직일 수 있다면 우선 순위 큐에 좌표와 유클리디언 거리를 듀플로 enqueue
            if isValidPos(x, y - 1) : q.enqueue((x, y - 1, -dist(x, y - 1)))
            if isValidPos(x, y + 1) : q.enqueue((x, y + 1, -dist(x, y + 1)))
            if isValidPos(x - 1, y) : q.enqueue((x - 1, y, -dist(x - 1, y)))
            if isValidPos(x + 1, y) : q.enqueue((x + 1, y, -dist(x + 1, y)))
        # 위치의 값을 .으로 변경
        drawMaze(here)
        map[y][x] = '.'
        # 딜레이를 줘 게임 상황을 볼 수 있게 한다.
        time.sleep(0.5)

    # 탐색에 실패 했다면 False 반환
    return False
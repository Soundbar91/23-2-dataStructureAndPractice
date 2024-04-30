from CircularQueue import CircularQueue
from isValidPos import isValidPos
from DrawMaze import drawMaze
from Map import map
# 딜레이 기능을 사용하기 위해 포함한 모듈
import time

# 너비우선탐색을 통해 미로의 출구를 탐색하는 함수
# 매개변수로 초기 위치를 전달 받는다.
def BFS(Initial_location) :
    # 원형 큐를 선언하고, 전달받은 초기 위치를 원형 큐에 enqueu
    que = CircularQueue(100)
    que.enqueue(Initial_location)

    # 원형 큐가 공백 상태가 될 때까지 너비우선탐색을 한다.
    while not que.isEmpty() :
        # 원형 큐에서 dequeue에서 요소를 반환 받는다.
        here = que.dequeue()
        x, y = here

        # 원형 큐에서 반환 받은 요소(좌표)의 값이 x인 경우 탈출 성공
        if (map[y][x] == 'x') : 
            map[y][x] = 'e'
            drawMaze(here)
            return True

        # 그렇지 않은 경우, 그 위치로 움직이고 너비우선탐색을 한다.
        else :
            # 위치의 값을 e로 변경
            # 상하좌우 순으로 탐색을 하고, 움직일 수 있다면 원형 큐에 해당 좌표를 enqueue
            map[y][x] = 'e'
            if isValidPos(x, y - 1) : que.enqueue((x, y - 1))
            if isValidPos(x, y + 1) : que.enqueue((x, y + 1))
            if isValidPos(x - 1, y) : que.enqueue((x - 1, y))
            if isValidPos(x + 1, y) : que.enqueue((x + 1, y))
        # 위치의 값을 .으로 변경
        drawMaze(here)
        map[y][x] = '.'
        # 딜레이를 줘 게임 상황을 볼 수 있게 한다.
        time.sleep(0.5)

    # 탐색에 실패 했다면 False 반환
    return False
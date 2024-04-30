from ArrayStack import ArrayStack
from isValidPos import isValidPos
from DrawMaze import drawMaze
from Map import map
# 딜레이 기능을 사용하기 위해 포함한 모듈
import time

# 깊이우선탐색을 통해 미로의 출구를 탐색하는 함수
# 매개변수로 초기 위치를 전달 받는다.
def DFS(Initial_location) :
    # 스택을 선언하고, 초기 위치를 스택에 push
    stack = ArrayStack(100)
    stack.push(Initial_location)

    # 스택이 공백 상태가 될 때까지 깊이우선탐색을 한다.
    while not stack.isEmpty() :
        # 스택에서 pop해서 요소를 반환 받는다.
        here = stack.pop(100)
        (x, y) = here

        # 스택에서 반환 받은 요소(좌표)의 값이 x인 경우 탈출 성공
        if (map[y][x] == 'x') : 
            map[y][x] = 'e'
            drawMaze(here)
            return True

        # 그렇지 않은 경우, 그 위치로 움직이고 깊이우선탐색을 한다.
        else :
            # 위치의 값을 e로 변경
            # 상하좌우 순으로 탐색을 하고, 움직일 수 있다면 스택에 해당 좌표를 push
            map[y][x] = 'e'
            if isValidPos(x, y - 1) : stack.push((x, y - 1))
            if isValidPos(x, y + 1) : stack.push((x, y + 1))
            if isValidPos(x - 1, y) : stack.push((x - 1, y))
            if isValidPos(x + 1, y) : stack.push((x + 1, y))
        # 위치의 값을 .으로 변경
        drawMaze(here)
        map[y][x] = '.'
        # 딜레이를 줘 게임 상황을 볼 수 있게 한다.
        time.sleep(0.5)

    # 탐색에 실패 했다면 False 반환
    return False
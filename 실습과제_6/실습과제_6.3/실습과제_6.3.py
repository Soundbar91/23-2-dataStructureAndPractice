import os
import time

# 클래스로 구현한 단순연결노드
class Node :
    # 단순연결노드의 생성자
    # elem : 자료, link : 링크(디폴트 값으로 None)
    def __init__(self, elem, link = None) :
        self.data = elem
        self.link = link

# 클래스로 구현한 원형연결구조 큐
class LinkedQueue : 
    
    # 큐의 생성자
    # 후단만 관리하면 되게 때문에 tail, 초기값은 None
    def __init__(self) :
        self.tail = None

    # 큐의 공백상태를 검사하기 위한 함수
    def isEmpty(self) : return self.tail == None

    # 큐에 요소를 전단에서 삽입하는 함수
    def enqueue(self, item) :
        # 데이터는 item, 링크는 None인 노드 선언
        node = Node(item, None)

        # 공백 상태인 경우,
        if self.isEmpty() :
            # 선언한 노드의 링크와 tail은 노드를 가르킨다.
            node.link = node
            self.tail = node
        
        # 공백상태가 아닌 경우
        else :
            # 선언한 노드의 링크는 tail의 링크가 가르키고 있는 노드를 가르킨다.
            node.link = self.tail.link
            # tail이 가르키고 있는 노드의 링크는 node를 가르킨다.
            self.tail.link = node
            # tail은 노드를 가르킨다.
            self.tail = node

    # 큐에 요소를 후단에서 제거하는 함수
    def dequeue(self) :
        if not self.isEmpty() :
            # 후단의 데이터를 저장
            data = self.tail.link.data
            # 전단과 후단이 같다면 기존에 노드는 한개가 있었으므로, None를 가르키도록 한다.
            if self.tail.link == self.tail :
                self.tail = None
            else : 
                # 그외의 경우에는 후단은 후단의 링크가 가르키는 노드를 가르키도록 한다.
                self.tail.link = self.tail.link.link
            # 반환값으로 후단의 데이터를 반환
            return data
    
    # 큐의 크기를 반환하는 함수
    def size(self) :
        # 공백상태인 경우 0을 반환
        if self.isEmpty() : return

        else :
            # 초기 카운터의 값은 1
            # node는 후단을 가르키도록 함
            count = 1
            node = self.tail.link
            
            # node가 전단이 될때까지 node의 링크를 타고 다음 노드로 넘어감
            # 넘아갈 때마다 카운터는 1 증가
            while not node == self.tail :
                node = node.link
                count += 1

            # 반환 값으로 count 반환
            return count
    
    # 큐에 저장된 정보를 문자열로 반환하기 위한 연산자 중복 함수
    def __str__(self) :
        # 노드의 정보를 저장할 리스트 선언
        arr = []

        if not self.isEmpty() :
            # node는 후단을 가르키도록 함
            node = self.tail.link

            # node가 전단이 될때까지 node의 링크를 타고 다음 노드로 넘어감
            # 넘아갈 때마다 node의 데이터를 리스트에 추가
            while not node == self.tail :
                arr.append(node.data)
                node = node.link
            # 마지막 데이터를 리스트에 추가
            arr.append(node.data)

        # 리스트를 문자열로 변환해서 반환
        return str(arr)

# 미로 맵
map = [['1','1','1','0','1','1','0','1','1','0','0','0','1','1','1'],
       ['e','0','1','0','1','0','0','0','0','1','1','0','1','0','0'],
       ['1','0','1','0','0','0','1','0','1','0','0','0','0','0','1'],
       ['0','0','0','0','1','0','1','1','1','0','1','1','1','0','0'],
       ['0','1','0','1','1','1','1','0','0','0','1','0','1','0','1'],
       ['0','1','0','0','0','0','0','0','1','1','1','0','0','0','1'],
       ['1','1','0','1','1','1','1','0','1','0','1','0','1','1','1'],
       ['0','0','0','0','0','0','0','0','0','0','0','0','1','1','1'],
       ['0','1','1','1','0','1','1','1','1','1','1','0','1','1','1'],
       ['1','1','0','0','0','1','1','1','1','1','1','0','1','1','1'],
       ['1','1','0','1','1','1','1','1','1','1','1','0','0','0','x']]

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

def isValidPos(x, y) :
    if 0 <= x < len(map[0]) and 0 <= y < len(map) :
        if map[y][x] == '0' or map[y][x] == 'x' : return True
    return False

# 너비우선탐색을 통해 미로의 출구를 탐색하는 함수
# 매개변수로 초기 위치를 전달 받는다.
def BFS(Initial_location) :
    # 연결된 큐를 선언하고, 전달받은 초기 위치를 큐에 enqueu
    que = LinkedQueue()
    que.enqueue(Initial_location)

    # 큐가 공백 상태가 될 때까지 너비우선탐색을 한다.
    while not que.isEmpty() :
        # 원형 큐에서 dequeue에서 요소를 반환 받는다.
        here = que.dequeue()
        x, y = here

        # 큐에서 반환 받은 요소(좌표)의 값이 x인 경우 탈출 성공
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

# 미로찾기 메인 함수
def main() :
    
    # 초기 위치를 저장하는 튜플
    here = (0, 0)
    # 반복문을 통해 맵에서 초기 위치를 찾아 튜플에 저장
    for i in range(len(map)) :
        for j in range(len(map[0])) :
            if map[i][j] == 'e' : 
                here = (j, i)
    drawMaze(here)

    result = BFS(here)

    # result의 값에 따라 출력하는 메세지가 다르도록 작성
    print(' --> 미로탐색 성공' if result else ' --> 미로탐색 실패')

main()
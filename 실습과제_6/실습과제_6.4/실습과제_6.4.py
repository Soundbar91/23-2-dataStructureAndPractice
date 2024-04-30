import os
import time

# 전단과 후단 노드의 정보를 가지고 있는 노드
# prev는 전단 노드, next는 후단 노드
class DNode :
    def __init__ (self, elem, prev = None, next = None) :
        self.data = elem
        self.prev = prev
        self.next = next

# 클래스로 구현한 이중연결구조 덱
class DoublyLinkedDeque :
    
    # 덱의 생성자
    # 전단 노드와 후단 노드를 가르키는 front와 rear를 관리한다. 초기값은 None
    def __init__(self) :
        self.front = None
        self.rear = None

    # 덱의 공백상태를 점검하는 함수
    # 전단 혹은 후단 아무거나 확인해도 됨
    def isEmpty(self) : return self.front == None
    
    # 전단에서 요소 E 를 삽입하는 함수
    def addFront(self, E) :
        # 데이터 E, 다음 노드의 링크를 front가 가르키는 노드를 가르키는 노드 선언
        node = DNode(E, None, self.front)
        
        # 공백상태인 경우
        if self.isEmpty() :
            # 전단과 후단 둘다 node를 가르킴
            self.front = self.rear = node
        else : 
            # front가 가르키는 노드의 이전 노드의 링크를 node로 설정
            self.front.prev = node
            # front는 node를 가르킴
            self.front = node

    # 후단에서 요소 E 를 삽입하는 함수
    def addRear(self, E) :
        # 데이터 E, 이전 노드의 링크를 front가 가르키는 노드를 가르키는 노드 선언
        node = DNode(E, self.rear, None)
        
        # 공백상태인 경우
        if self.isEmpty() :
            # 전단과 후단 둘다 node를 가르킴
            self.front = self.rear = node
        else : 
            # rear가 가르키는 노드의 이전 노드의 링크를 node로 설정
            self.rear.next = node
            # rear는 node를 가르킴
            self.rear = node

    # 전단에서 노드를 삭제하는 함수
    def deleteFront(self) :
        if not self.isEmpty() :
            # front가 가르키는 노드의 데이터를 저장
            data = self.front.data
            # front는 다음 노드를 가르도록 함
            self.front = self.front.next
            
            # 다음 노드가 None인 경우 공백상태임
            if self.front == None :
                self.rear = None
            # 그외의 경우에는 front가 가르키는 노드의 이전 노드의 링크를 None로 설정
            else :
                self.front.prev = None
            
            # 반환 값으로 data를 반환
            return data
    
    # 후단에서 노드를 삭제하는 함수
    def deleteRear(self) :
        if not self.isEmpty() :
            # rear가 가르키는 노드의 데이터를 저장
            data = self.rear.data
            # rear는 이전 노드를 가르도록 함
            self.rear = self.rear.prev
            
            # 이전 노드가 None인 경우 공백상태임
            if self.rear == None :
                self.front = None
            # 그외의 경우에는 rear가 가르키는 노드의 다음 노드의 링크를 None로 설정
            else :
                self.rear.next = None
            
            return data

    # 덱에 저장된 데이터를 문자열로 출력하기 위한 연산자 중복 함수
    def __str__(self) :
        # 노드의 정보를 저장할 리스트 선언
        arr = []
        # front가 가르키는 노드에서부터 시작
        node = self.front

        # node가 None 될때까지 node의 링크를 타고 다음 노드로 넘어감
        # 넘아갈 때마다 node의 데이터를 리스트에 추가
        while not node == None :
            arr.append(node.data)
            node = node.next

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

# 깊이우선탐색을 통해 미로의 출구를 탐색하는 함수
# 매개변수로 초기 위치를 전달 받는다.
def DFS(Initial_location) :
    # 스택을 선언하고, 초기 위치를 스택에 push
    stack = DoublyLinkedDeque()
    stack.addRear(Initial_location)

    # 스택이 공백 상태가 될 때까지 깊이우선탐색을 한다.
    while not stack.isEmpty() :
        # 스택에서 pop해서 요소를 반환 받는다.
        here = stack.deleteRear()
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
            if isValidPos(x, y - 1) : stack.addRear((x, y - 1))
            if isValidPos(x, y + 1) : stack.addRear((x, y + 1))
            if isValidPos(x - 1, y) : stack.addRear((x - 1, y))
            if isValidPos(x + 1, y) : stack.addRear((x + 1, y))
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

    result = DFS(here)

    # result의 값에 따라 출력하는 메세지가 다르도록 작성
    print(' --> 미로탐색 성공' if result else ' --> 미로탐색 실패')

main()
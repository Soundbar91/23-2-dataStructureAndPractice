# 연결된 스택에서 노드를 사용
from Node import Node

# 클래스로 구현한 연결된 스택
class LinkedStack :
    # 스택의 생성자
    def __init__(self) :
        # 시작노드를 가르키는 top만 관리하고, 초기 상태는 None
        self.top = None

    # 스택의 공백 상태를 확인하는 함수
    def isEmpty(self) : return self.top == None

    # 스택에 전달받은 변수를 저장하는 함수
    def push(self, e) :
        # 데이터를 e, 링크는 top를 가르키는 노드를 생성
        # top은 해당 노드를 가르킴
        self.top = Node(e, self.top)

    # 스택에 마지막으로 들어온 변수를 빼는 함수
    def pop(self) :
        if not self.isEmpty() :
            # top이 가르키는 노드의 데이터를 저장
            n = self.top.data
            # top은 가리키고 있던 노드의 링크를 타고 다음 노드를 가르킴
            self.top = self.top.link
            # 반환 값으로 n을 반환
            return n
    
    # 스택에 마지막에 들어온 변수를 빼지 않고 확인하는 함수
    def peek(self) :
        if not self.isEmpty() :
            # top이 가르키는 노드의 데이터를 반환
            return self.top.data
    
    # 연결된 스택의 크기를 반환하는 함수
    def size(self) :
        # top이 가르키는 노드를 저장
        # 카운터의 초기 값은 0
        node = self.top
        count = 0

        # node의 값이 None이 될때까지 링크를 계속 타서 다음 노드로 넘어감
        # 넘어 갈 때마다 카운터는 1씩 증가
        while not node == None :
            node = node.link
            count += 1
        
        # 반환값으로 카운터의 값을 반환
        return count
    
    # 결과를 문자열로 출력하기 위한 함수
    def __str__(self) :
        # 스택의 데이터를 저장할 리스트 선언
        # top이 가르키는 노드를 저장
        arr = []
        node = self.top

        # node의 값이 None이 될때까지 링크를 계속 타서 다음 노드로 넘어감
        # 넘어 갈 때마다 노드의 데이터를 리스트에 추가
        while not node == None :
            arr.append(node.data)
            node = node.link

        # 반환 값으로 리스트를 문자열로 변환하여 반환
        return str(arr)
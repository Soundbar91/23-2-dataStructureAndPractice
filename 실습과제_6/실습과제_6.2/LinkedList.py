from Node import Node

# 클래스로 구현한 연결된 리스트
class LinkedList :
    # 리스트의 생성자
    # 시작 노드를 가르키는 head만 관리한다. 초기값은 None
    def __init__(self) :
        self.head = None

    # 리스트의 공백상태를 검사하는 함수
    def isEmpty(self) : return self.head == None

    # pos에 있는 노드를 반환받는 함수
    def getNode(self, pos) :
        # pos가 음수이면 None 반환
        if pos < 0 : return None

        # head가 가르키는 노드를 저장
        # pos가 음수 그리고 node가 None 될 때까지 노드의 링크를 타서 다음 노드로 넘어감
        # 넘어갈 때 마다 pos는 1씩 감소
        node = self.head
        while pos > 0 and node != None :
            node = node.link
            pos -= 1

        # 반환값으로 마지막으로 가르키는 노드를 반환
        return node
    
    # pos 위치에 있는 노드의 데이터를 반환받는 함수
    def getEntry(self, pos) :
        # pos 위치에 있는 노드를 저장
        node = self.getNode(pos)

        # 노드가 None이면 반환값도 None
        # 그 외에는 노드의 데이터 값을 반환
        if node == None : return None
        else : return node.data
    
    # pos 위치에 elem를 삽입하는 함수
    def insert(self, pos, elem) :
        # pos - 1 위치에 있는 노드의 정보를 저장한다
        before = self.getNode(pos - 1)
        
        # 이전 노드가 None일때
        if before == None :
            # 데이터는 elem, 링크는 head를 가르키는 노드를 선언
            # head는 해당 노드를 가르킨다
            self.head = Node(elem, self.head)
        # 이전 노드가 있을 경우
        else :
            # 이전 노드의 링크는 데이터로 elem, 링크는 이전 노드의 링크를 가지고 있는 노드를 가르킴
            node = Node(elem, before.link)
            before.link = node

    # pos 위치에 있는 노드를 삭제하는 함수
    def delete(self, pos) :
        # pos - 1 위치에 있는 노드의 정보를 저장한다
        before = self.getNode(pos - 1)

        # 이전 노드가 None일때
        if before == None :
            # 이전노드가 head이면, head는 head.link를 가르키도록 한다.
            if self.head is not None :
                self.head = self.head.link
        # 이전 노드가 None이 아니면
        elif before.link != None:
            # 이전 노드의 link를 한 단계 건너뛰어 노드를 삭제
            before.link = before.link.link
    
    # 연결된 리스트의 크기를 반환하는 함수
    def size(self) :
        # head이 가르키는 노드를 저장
        # 카운터의 초기 값은 0
        node = self.head
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
        # head이 가르키는 노드를 저장
        arr = []
        node = self.head

        # node의 값이 None이 될때까지 링크를 계속 타서 다음 노드로 넘어감
        # 넘어 갈 때마다 노드의 데이터를 리스트에 추가
        while not node == None :
            arr.append(node.data)
            node = node.link

        # 반환 값으로 리스트를 문자열로 변환하여 반환
        return str(arr)
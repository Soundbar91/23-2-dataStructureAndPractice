from DNode import DNode

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

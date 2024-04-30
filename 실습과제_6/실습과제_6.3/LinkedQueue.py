from Node import Node

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
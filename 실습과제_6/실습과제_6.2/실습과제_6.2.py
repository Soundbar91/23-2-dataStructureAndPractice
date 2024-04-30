# 클래스로 구현한 단순연결노드
class Node :
    # 단순연결노드의 생성자
    # elem : 자료, link : 링크(디폴트 값으로 None)
    def __init__(self, elem, link = None) :
        self.data = elem
        self.link = link

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

# 다항식 Polynomial의 클래스
class Polynomial :

    # Polynomial 클래스 생성자
    # 연결된 리스트를 가진다.
    def __init__(self) :
        self.poly = LinkedList()

    # 사용자로부터 다항식의 최고 차수와 계수를 입력받는 메소드
    def read_poly(self) :
        
        # 사용자로부터 최고 차수를 입력 받음
        degree = eval(input("다항식의 최고 차수를 입력하시오 : "))

        # 사용자로부터 해당 차수의 계수를 입력 받음
        for i in range(0, degree + 1) :
            num = eval(input("x^%d의 계수 : "%(i)))
            self.poly.insert(i, num)

    # 다항식의 차수를 반환하는 메소드
    def degree(self) :
        # 입력한 차수보다 1을 크게 리스트를 선언하였으므로, 1를 뺀 값을 반환
        return self.poly.size() - 1
    
    # 미지수에 매개변수로 전달받은 숫자를 대입하여 계산된 결과를 반환하는 메소드
    def evaluate(self, scalar) : 
        sum = 0

        # 반복문과 리스트의 인덱스, ** 연산를 이용하여 계산
        for i in range(self.poly.size() - 1, -1, -1) :
            sum += self.poly.getEntry(i) * (scalar ** i)
        
        # 반복문을 통해 계산된 합을 반환
        return sum 
   
    # 다항식 두 개를 더하고, 이를 새로운 변수에 저장하고 반환하는 메소드
    def add(self, rhs) :
        # 결과 값을 저장할 객체 변수 선언
        arr = Polynomial()

        # 감시값 변수 선언
        i = self.poly.size() - 1
        j = rhs.poly.size() - 1

        # 0부터 두 다항식 중 차수가 낮은 다항식의 차수까지 더해서 arr에 삽입한다. 
        for k in range(0, min(i, j) + 1) :
            arr.poly.insert(k, self.poly.getEntry(k) + rhs.poly.getEntry(k))

        # 남은 차수의 다항식을 arr에 삽입한다.
        while i != min(i, j) :
            arr.poly.insert(i, self.poly.getEntry(i))
            i -= 1

        # 남은 차수의 다항식을 arr에 삽입한다.
        while j != min(i, j) :
            arr.poly.insert(j, rhs.poly.getEntry(j))
            j -= 1
        
        return arr
    
    # 다항식 두개를 빼고, 이를 새로운 변수에 저장하고 반환하는 메소드
    def subtract(self, rhs) :
        # 결과 값을 저장할 객체 변수 선언
        arr = Polynomial()

        # 감시값 변수 선언
        i = self.poly.size() - 1
        j = rhs.poly.size() - 1
        
        # 0부터 두 다항식 중 차수가 낮은 다항식의 차수까지 빼서 arr에 삽입한다. 
        for k in range(0, min(i, j) + 1) :
            arr.poly.insert(k, self.poly.getEntry(k) - rhs.poly.getEntry(k))

        # 남은 차수의 다항식을 arr에 삽입한다.
        while i != min(i, j) :
            arr.poly.insert(i, self.poly.getEntry(i))
            i -= 1

        # 남은 차수의 다항식을 arr에 삽입한다.
        while j != min(i, j) :
            arr.poly.insert(j, -1 * rhs.poly.getEntry(j))
            j -= 1

        return arr

    # 다항식 두개를 곱하고, 이를 새로운 변수에 저장하고 반환하는 메소드
    def multiply(self, rhs) :
        # 곱해서 나온 결과값을 반환하기 위한 객체 변수 선언
        arr = Polynomial()
        # 결과값을 임시로 저장할 리스트 선언
        emt = [0] * ((self.poly.size() + rhs.poly.size()) - 1)

        # 중첩 반복문을 통해 두 다항식의 곱셈을 진행
        for i in range(0, self.poly.size()) :
            for j in range(0, rhs.poly.size()) : 
                emt[i + j] += self.poly.getEntry(i) * rhs.poly.getEntry(j)
        
        # 임시로 저장한 리스트의 값을 arr에 삽입
        for i in range(0, len(emt)) :
            arr.poly.insert(i, emt[i])
        
        return arr

    # 다항식을 화면에 출력하는 메소드
    def display(self) :
        # 반복문을 통해 화면에 다항식을 출력
        for i in range(self.poly.size() - 1, -1, -1) :
            
            # 값이 0일 경우 continue로 생략
            if self.poly.getEntry(i) == 0 : continue
            # 마지막 항, x^0일 때 출력 
            elif i == 0 : 
                # 음수인 경우 괄호를 같이 출력
                if self.poly.getEntry(i)  < 0 : print("(%3.1f)"%(self.poly.getEntry(i) ))
                # 그 이외의 경우 값을 그대로 출력
                else : print("%3.1f"%(self.poly.getEntry(i) ))
            # 값이 음수일 경우 괄호를 같이 출력
            elif self.poly.getEntry(i) < 0 : print("(%3.1f)x^%d"%(self.poly.getEntry(i) , i), end = " +")
            # 그 외의 경우에는 값을 그대로 출력
            else : print("%3.1fx^%d"%(self.poly.getEntry(i) , i), end = " +")

a = Polynomial()
b = Polynomial()

a.read_poly()
b.read_poly()
c = a.add(b)
print("a 방정식 : ", end = "")
a.display() 
print("b 방정식 : ", end = "")
b.display() 
print("a + b 방정식 : ", end = "") 
c.display()
print("a + b(2) 방정식 : ", c.evaluate(2))

d = a.subtract(b)
print("a - b 방정식 : ", end = "")
d.display() 

e = a.multiply(b)
print("a * b 방정식 : ", end = "")
e.display() 
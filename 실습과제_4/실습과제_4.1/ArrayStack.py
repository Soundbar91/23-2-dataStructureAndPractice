# 클래스로 구현한 스택
class ArrayStack :

    # ArrayStack의 생성자
    def __init__(self, Capacity) :
        # 넘겨받은 용량을 통해 Array를 초기화
        self.Capacity = Capacity
        self.Array = [None] * self.Capacity
        # 상단의 인덱스 -1로 설정
        self.Top = -1

    # 스택이 비었는지 확인하는 함수
    def isEmpty(self) :
        return self.Top == -1
    
    # 스택이 꽉 차있는지 확인하는 함수
    def isFull(self) :
        return self.Top == self.Capacity - 1
    
    # 스택에 전달받은 변수를 저장하는 함수
    def push(self, e) :
        # 스택이 꽉 차있지 않다면 Push
        if not self.isFull() :
            self.Top += 1
            self.Array[self.Top] = e
        else : pass

    # 스택에 마지막으로 들어온 변수를 빼는 함수
    def pop(self) :
        # 스택이 비어있지 않다면 Pop
        if not self.isEmpty() :
            self.Top -= 1
            return self.Array[self.Top + 1]
        else : pass

    # 스택에 마지막에 들어온 변수를 빼지 않고 확인하는 함수
    def peek(self) :
        # 스택이 비어있지 않다면 마지막 변수의 값만 반환
        if not self.isEmpty() :
            return self.Array[self.Top]
        else : pass

    # 결과를 문자열로 출력하기 위한 함수
    def __str__(self) :
        # 인덱스 슬라이싱을 이용하여 문자열로 반환
        return str(self.Array[0:self.Top + 1])
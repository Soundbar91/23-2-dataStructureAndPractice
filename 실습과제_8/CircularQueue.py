# 배열로 구현한 원형 큐
class CircularQueue :

    # CircularQueue의 생성자
    # 배열의 크기를 전달받은 큐의 크기만큼 선언하고 초기화
    # 큐의 마지막 요소의 위치, 처음 요소 앞의 위치를 저장할 변수 선언
    def __init__(self, capacity = 8) :
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0

    # 원형 큐가 공백 상태인지 확인하는 함수
    # front와 rear의 값이 같은 경우 공백 상태로 정의
    def isEmpty(self) :
        return self.front == self.rear
    
    # 원형 큐가 포화 상태인지 확인하는 함수
    # 공백 상태와 구분을 하기 위해 한 칸을 비우는 전략을 사용
    # ex) front와 rear가 모두 0이지만, 원형 큐에 값이 모두 차 있어 한 바퀴를 돈 이후 0를 가리킬 수도 있다.
    # ex) front = 0, rear = 7 -> 0 = (7 + 1) % 8 = 0 -> 배열을 원형으로 구현하는 수식
    def isFull(self) :
        return self.front == (self.rear + 1) % self.capacity
    
    # 원형 큐에 전달받은 요소를 삽입하는 함수
    # 원형 큐가 포화 상태인지를 확인 후, rear의 값을 변경 시키고 배열에서 rear 위치에 요소를 삽입한다
    def enqueue(self, item) :
        if not self.isFull() :
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else : pass

    # 원형 큐에서 맨 앞의 요소를 삭제하는 함수
    # 원형 큐가 공백 상태인지를 확인 후, front의 값을 변경 시키고 배열에서 front 위치에 있는 요소를 반환한다.
    def dequeue(self) :
        if not self.isEmpty() :
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else : pass

    # 원형 큐에서 맨 앞에 요소를 확인하는 함수
    # 원형 큐가 공백 상태인지를 확인 후, 배열에서 맨 앞에 있는 요소를 반환한다.
    def peek(self) :
        if not self.isEmpty() :
            return self.array[(self.front + 1) % self.capacity]
        else : pass

    # 원형 큐의 요소의 수를 구하는 함수이다.
    # rear - front가 음수가 될 수 있기 때문에 용량을 더해 양수로 만들고 용량으로 나눈다.
    # ex) rear = 0, front = 4 -> (0 - 4 + 8) % 8 = 4
    def size(self) :
        return (self.rear - self.front + self.capacity) % self.capacity
    
    # 결과를 문자열로 출력하기 위한 함수(인덱스 슬라이싱)
    # front가 rear보다 작은 경우에는 front + 1 ~ rear까지 출력
    # rear가 front보다 작은 경우에는 front + 1 ~ capacity - 1와 0 ~ rear까지 두 문자열을 더해서 출력한다.
    def __str__(self) :
        if self.front < self.rear :
            return str(self.array[self.front + 1:self.rear + 1])
        else :
            return str(self.array[self.front + 1:self.capacity] + self.array[0:self.rear + 1])
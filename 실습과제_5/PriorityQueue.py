# 정렬되지 않은 배열을 이용한 우선순위 큐 클래스
class PriorityQueue :
    
    # PriorityQueue의 생성자
    # 배열의 크기를 전달받은 큐의 크기만큼 선언하고 초기화
    # size는 요소의 수
    def __init__(self, capacity = 10) :
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    # 우선순위 큐가 공백 상태인지를 확인하는 함수
    # 요소의 개수가 0개이면 공백 상태로 정의
    def isEmpty(self) : return self.size == 0

    # 우선순위 큐가 포화 상태인지를 확인하는 함수
    # 요소의 개수가 용량과 같다면 포화 상태로 정의
    def isFull(self) : return self.size == self.capacity

    # 우선순위 큐에 요소를 삽입하는 함수
    # 우선순위 큐가 포화 상태가 아니면 요소를 추가하고 size를 1 증가 시킨다
    def enqueue(self, e) :
        if not self.isFull() :
            self.array[self.size] = e
            self.size += 1

    # 우선순위가 제일 높은 값의 인덱스를 찾는 함수
    def findMaxIndex(self) :
        # 우선순위 큐가 공백 상태이면 -1를 반환
        if self.isEmpty() : return -1

        # 0번째 위치에 있는 값을 초기 비교 값으로 설정
        # 1번째 위치에 있는 값부터 비교를 시작
        # 비교를 했을 때 큰 값인 경우 해당 값의 인덱스를 highest에 저장
        highest = 0
        for i in range(1, self.size) :
            # 미로찾기에서 -d의 값을 사용하기 위해 2차원 리스트로 비교
            # self.array[i] > self.array[highest]
            if self.array[i][2] > self.array[highest][2] :
                highest = i
        # 제일 큰 값(우선순위가 높은 값)의 인덱스를 반환
        return highest
    
    # 우선순위가 가장 높은 요소를 꺼내 반환하는 함수
    def dequeue(self) :
        # 제일 큰 값의 인덱스를 반환받아 변수에 저장
        highest = self.findMaxIndex()
        if highest != -1 :
            # size를 하나 감소
            # 우선순위가 높은 요소와 마지막에 저장된 요소의 위치를 바꾼다.
            self.size -= 1
            self.array[highest], self.array[self.size] = self.array[self.size], self.array[highest]
            # 우선순위가 높은 요소를 반환
            return self.array[self.size]
    
    # 우선순위가 가장 높은 요소를 확인하는 함수
    def peek(self) :
        # 제일 큰 값의 인덱스를 반환받아 변수에 저장
        highest = self.findMaxIndex()
        if highest != -1 :
            # 해당 위치에 있는 값을 반환
            return self.array[highest]

    # 문자열로 변환하여 출력하는 함수
    # 인덱스 슬라이싱을 이용하여 0 ~ size - 1까지 출력   
    def __str__(self) :
        return str(self.array[0:self.size])
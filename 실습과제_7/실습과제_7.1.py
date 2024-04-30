# 클래스로 구현한 정렬된 집합
class SetSorted :
    # 생성자 / 요소를 저장할 리스트와 크기를 관리한다
    def __init__(self) :
        self.items = list()
        self.Size = len(self.items)

    # 집합의 크기를 반환하는 함수
    def size(self) : return self.Size

    # 집합에 요소가 있는지 검사하는 함수 / O(lon n)
    # 이진 탐색(반복)으로 구현
    def contains(self, item) :
        # 탐색 범위를 저장할 변수 선언
        # 초기값 첫 번째와 마지막 번째의 인덱스
        low = 0
        high = self.size() - 1
        
        # low와 high가 역전이 되면 리스트에 값이 없다
        while (low <= high) :
            # 초기 탐색 범위의 중앙 값을 계산
            middle = (low + high) // 2

            # 중앙값과 요소가 같으면 True를 반환
            # 중앙값이 요소보다 작으면 중앙값보다 앞에 있음 -> 최소 범위를 중앙값의 인덱스보다 1 크게 설정
            # 중앙값이 요소보다 크면 중앙값보다 뒤에 있음 -> 최대 범위를 중앙값의 인덱스보다 1 작게 설정
            if item == self.items[middle] : return True
            elif item > self.items[middle] : low = middle + 1
            else : high = middle - 1

        return False
    
    # 집합에 요소를 삽입하는 함수 / O(n)
    def insert(self, elem) : 
        # 집합에 요소가 있으면 삽입 불가능
        if self.contains(elem) :
            return False
        
        self.items.append(elem)
        self.Size += 1
        
        # 순차 탐색을 이용하여 값을 비교하고 집합을 정렬
        for i in range(self.Size - 1, 0, -1) :
            if self.items[i - 1] <= self.items[i] : break
            self.items[i - 1], self.items[i] = self.items[i], self.items[i - 1]

    # 집합에서 요소를 제거하는 함수 / O(n)
    def delete(self, elem) : 
        self.Size -= 1
        self.items.remove(elem)

    # 두 집합의 합집합을 구하는 함수 / O(n)
    def union(self, setB) :
        # 합집합을 저장할 집합과 두 집합의 인덱스를 관리할 변수 선언
        setC = SetSorted()
        i = 0
        j = 0

        # 인덱스가 집합의 크기보다 커질 때 까지 진행
        while i < self.Size and j < setB.Size :
            data1 = self.items[i]
            data2 = setB.items[j]

            # 정렬된 집합이기 때문에 값을 비교했을 때 큰 요소를 먼저 삽입
            # 이후에 요소를 가져온 집합의 인덱스 증가
            # 만약, 두 값이 같다면 한쪽의 요소만 삽입 후에 두 집합의 인덱스 증가
            if data1 < data2 : 
                setC.items.append(data1)
                i += 1
            elif data1 > data2 :
                setC.items.append(data2)
                j += 1
            else :
                setC.items.append(data1)
                i += 1
                j += 1

        # 리스트에 남은 요소를 삽입
        # 크기가 같지 않은 이상, 비교가 끝난 집합과 아직 비교 할 요소가 남은 집합이 존재
        while i < self.Size :
            setC.items.append(self.items[i])
            i += 1

        while j < setB.Size :
            setC.items.append(setB.items[j])
            j += 1

        # 합집합의 멤버 변수의 크기 증가 이후에 반환
        setC.Size = len(setC.items)
        return setC

    # 두 집합의 교집합을 구하는 함수 / O(n)
    def intersect(self, setB) :
        # 합집합을 저장할 집합과 두 집합의 인덱스를 관리할 변수 선언
        setC = SetSorted()
        i = 0 
        j = 0

        # 인덱스가 집합의 크기보다 커질 때 까지 진행
        while i < self.Size and j < setB.Size:
            data1 = self.items[i]
            data2 = setB.items[j]

            # 값이 같다면 삽입 / 이후 두 집합의 인덱스 증가
            # 정렬된 집합이기 때문에 값을 비교할 때 작은 값을 가진 집합의 인덱스만 증가
            if data1 == data2 :
                setC.items.append(data1)
                i += 1
                j += 1
            elif data1 < data2 : i += 1
            else : j += 1

        # 교집합의 멤버 변수의 크기 증가 이후에 반환
        setC.Size = len(setC.items)
        return setC

    # 두 집합의 차집합을 구하는 함수 / O(n)
    def difference(self, setB) :
        # 합집합을 저장할 집합과 두 집합의 인덱스를 관리할 변수 선언
        setC = SetSorted()
        i = 0 
        j = 0

        # 인덱스가 집합의 크기보다 커질 때 까지 진행
        while i < self.Size and j < setB.Size :
            data1 = self.items[i]
            data2 = setB.items[j]

            """
            # 정렬된 집합이기 때문에 왼쪽 집합의 요소 작으면 오른쪽의 집합에는 해당 요소가 없음
            # -> 왼쪽 요소를 삽입
            # 왼쪽 집합의 요소 크면 오른쪽의 집합에는 해당 요소가 있음
            # -> 오른쪽 집합의 인덱스 증가
            # 값이 같다 -> 두 집합의 인덱스 증가
            """ 
            if data1 < data2 : 
                setC.items.append(data1)
                i += 1
            elif data1 > data2 :
                j += 1
            else :
                i += 1
                j += 1
            
        # 왼쪽 집합에서 비교할 요소가 남은 경우 차집합에 삽입
        while i < self.Size :
            setC.items.append(data1)
            i += 1

        # 차집합의 멤버 변수의 크기 증가 이후에 반환
        setC.Size = len(setC.items)
        return setC

    # 두 집합 간에 "="를 사용하기 위한 연산자 중복 함수 / O(n)
    def __eq__(self, setB) :
        # 두 집합의 크기가 다르면 같지 않음
        if self.Size != setB.Size : return False

        # 반복문을 통해 두 집합의 요소 비교
        for i in range(self.Size) :
            if self.items[i] != setB.items[i] : return False
            
        return True

    # 집합을 출력하는 함수
    def display(self, msg = "") :
        print(msg, self.items)
        

# 다양한 입력에 대한 테스트
a = SetSorted()
a.insert(3)
a.insert(5)
a.insert(4)
a.display("집합 a : ")
print("집합 a에 1의 유무 : ", a.contains(1))
print("집합 a의 크기 : ", a.size())

a.delete(4)
a.display("집합 a에서 4를 삭제 : ")

b = SetSorted()
b.insert(1)
b.insert(4)
b.insert(3)
b.insert(7)
b.display("집합 b : ")

c = a.union(b)
d = a.intersect(b)
e = a.difference(b)

c.display("집합 a와 집합 b의 합집합 : ")
d.display("집합 a와 집합 b의 교집합 : ")
e.display("집합 a와 집합 b의 차집합 : ")
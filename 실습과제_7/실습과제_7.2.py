# 클래스로 구현한 해싱
# 계산된 버킷부터 순서대로 찾는 선형 조사법 사용
class Hash :

    # 생성자 / 해시 테이블의 크기와 해시 테이블을 관리
    def __init__ (self, M) :
        self.M = M
        self.table = [None] * M

    # 해시 함수 / 제산 함수 사용
    # 키 값를 해시 테이블의 크기로 나눈 나머지 반환
    def hashFn(self, key) :
        return key % self.M
    
    # 선형 조사법을 이용해서 해시 테이블에 값을 삽입하는 함수
    def insert(self, key) :
        # 해시 주소와 해시 크기를 저장할 변수 선언
        i = self.hashFn(key)
        count = self.M

        # 카운터가 0이 되면 저장할 버킷이 없음
        while count > 0 :
            # 버킷의 값이 None 혹은 -1 -> 반복문 탈출 후 값 저장
            # -1은 값이 있었다가 제거 되었음을 표시하는 값
            if self.table[i] == None or self.table[i] == -1 : break

            # 해시 주소를 증가 / 해시 주소의 끝까지 가게 되면 처음으로 돌아가게 됨
            # ex) i = 12, self.M = 13 / (12 + 1) % 13 = 0
            i = (i + 1) % self.M
            count -= 1

        # 반복문에서 break을 통해 탈출했다면 count는 0보다 큼 -> 값을 해시 테이블에 삽입
        if count > 0 :
            self.table[i] = key

    # 선형 조사법을 이용해서 해시 테이블에서 값을 탐색하는 함수
    def search(self, key) :
        i = self.hashFn(key)
        count = self.M

        # 카운터가 0이 되면 해시 테이블에 레코드가 없음
        while count > 0 :
            # 버킷의 값이 None -> 탐색 실패
            # 버킷의 값이 키값과 같다 -> 탐색 성공
            if self.table[i] == None : return False
            if self.table[i] == key : return True
            
            i = (i + 1) % self.M
            count -= 1

        return False
    
    # 선형 조사법을 이용해서 해시 테이블에서 값을 삭제하는 함수
    def delete(self, key) :
        i = self.hashFn(key)
        count = self.M

        # 카운터가 0이 되면 해시 테이블에 삭제할 레코드가 없음
        while count > 0 :
            # 버킷의 값과 키값이 같음 -> 해당 버킷에 -1 저장
            # -1은 삭제가 되었음을 표시
            # 버킷의 값이 None -> 해시 테이블에 삭제할 레코드가 없음
            if self.table[i] == key : 
                self.table[i] = -1
                return 
            elif self.table[i] == None : return 

            i = (i + 1) % self.M
            count -= 1
    
    # 해시 테이블을 출력하기 위한 연산자 중복 함수
    def __str__(self) :
        # 해시 테이블을 저장하기 위한 리스트 
        lst = []

        # 반복문을 통해 리스트에 해시 테이블을 저장
        for i in range(self.M) :
            lst.append(self.table[i])

        # 리스트를 문자열로 반환
        return str(lst)

# p.268 테스트 프로그램
data = [45, 27, 88, 9, 71, 60, 46, 38, 26]
hash = Hash(13)

for d in data :
    hash.insert(d)
    print("h(%2d) = %2d" %(d, hash.hashFn(d)) , end = " ")
    print(hash)

print("46 탐색 --> ", hash.search(46))
print("39 탐색 --> ", hash.search(39))

print("60 삭제 --> ", end = "")
hash.delete(60)
print(hash)
print("46 삭제 --> ", end = "")
hash.delete(46)
print(hash)

print("----------------------------------------")

# 다양한 입력에 대한 테스트
data = [35, 62, 71, 20, 1, 30, 50]
hash = Hash(19)

for d in data :
    hash.insert(d)
    print("h(%2d) = %2d" %(d, hash.hashFn(d)) , end = " ")
    print(hash)

print("35 탐색 --> ", hash.search(35))
print("60 탐색 --> ", hash.search(60))

print("50 삭제 --> ", end = "")
hash.delete(50)
print(hash)
print("30 삭제 --> ", end = "")
hash.delete(30)
print(hash)
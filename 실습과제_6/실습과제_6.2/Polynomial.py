from LinkedList import *

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
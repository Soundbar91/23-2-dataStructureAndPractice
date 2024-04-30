# 다항식 Polynomial의 클래스
class Polynomial :

    # Polynomial 클래스 생성자
    def __init__(self, poly = []) :
        self.poly = poly

    # 사용자로부터 다항식의 최고 차수와 계수를 입력받는 메소드
    def read_poly(self) :
        
        # 사용자로부터 최고 차수를 입력 받음
        degree = eval(input("다항식의 최고 차수를 입력하시오 : "))
        # 입력한 차수 + 1로 리스트를 선언
        self.poly = [0] * (degree + 1)

        # 사용자로부터 해당 차수의 계수를 입력 받음
        for i in range(degree, -1, -1) :
            self.poly[i] = eval(input("x^%d의 계수 : "%(i)))

    # 다항식의 차수를 반환하는 메소드
    def degree(self) :
        # 입력한 차수보다 1을 크게 리스트를 선언하였으므로, 1를 뺀 값을 반환
        return len(self.poly) - 1
    
    # 미지수에 매개변수로 전달받은 숫자를 대입하여 계산된 결과를 반환하는 메소드
    def evaluate(self, scalar) : 
        sum = 0

        # 반복문과 리스트의 인덱스, ** 연산를 이용하여 계산
        for i in range(len(self.poly)) :
            sum += self.poly[i] * (scalar ** i)
        
        # 반복문을 통해 계산된 합을 반환
        return sum 
   
    # 다항식 두 개를 더하고, 이를 새로운 변수에 저장하고 반환하는 메소드
    def add(self, rhs) :
        # 다항식 두 개를 더한 후, 저장할 리스트를 선언
        # 크기는 두 개의 리스트 중에서 크기가 제일 큰 크기로 선언
        arr = [0] * max(len(self.poly), len(rhs))

        # 반복문을 통해 두 다항식의 덧셈을 진행
        for i in range(len(self.poly)) :
            arr[i] += self.poly[i]

        for i in range(len(rhs)) :
            arr[i] += rhs[i]
        
        # 반환값은 Polynomial의 객체로 반환
        # 리스트로 반환을 하면 이를 전달받는 변수가 Polynomial 객체 변수가 아닌 그냥 리스트로 선언이 됨
        return Polynomial(arr)
    
    # 다항식 두개를 빼고, 이를 새로운 변수에 저장하고 반환하는 메소드
    def subtract(self, rhs) :
        # 다항식 두 개를 뺀 후, 저장할 리스트를 선언
        # 크기는 두 개의 리스트 중에서 크기가 제일 큰 크기로 선언
        arr = [0] * max(len(self.poly), len(rhs))

        # 반복문을 통해 두 다항식의 뺄셈을 진행
        for i in range(len(self.poly)) :
            arr[i] += self.poly[i]

        for i in range(len(rhs)) :
            arr[i] -= rhs[i]

        # 반환값은 Polynomial의 객체로 반환
        # 리스트로 반환을 하면 이를 전달받는 변수가 Polynomial 객체 변수가 아닌 그냥 리스트로 선언이 됨
        return Polynomial(arr)

    # 다항식 두개를 곱하고, 이를 새로운 변수에 저장하고 반환하는 메소드
    def multiply(self, rhs) :
        # 다항식 두 개를 곱한 후, 저장할 리스트를 선언
        # 크기는 두 개의 리스트 크기를 더한 크기로 선언
        arr = [0] * (len(self.poly) + len(rhs))

        # 중첩 반복문을 통해 두 다항식의 곱셈을 진행
        for i in range(len(self.poly)) :
            for j in range(len(rhs)) :
                arr[i + j] += self.poly[i] * rhs[j]
        
        # 반환값은 Polynomial의 객체로 반환
        # 리스트로 반환을 하면 이를 전달받는 변수가 Polynomial 객체 변수가 아닌 그냥 리스트로 선언이 됨
        return Polynomial(arr)

    # 다항식을 화면에 출력하는 메소드
    def display(self) :
        # 반복문을 통해 화면에 다항식을 출력
        for i in range(len(self.poly) - 1, -1, -1) :
            
            # 값이 0일 경우 continue로 생략
            if self.poly[i] == 0 : continue
            # 마지막 항, x^0일 때 출력 
            elif i == 0 : 
                # 음수인 경우 괄호를 같이 출력
                if self.poly[i] < 0 : print("(%3.1f)"%(self.poly[i]))
                # 그 이외의 경우 값을 그대로 출력
                else : print("%3.1f"%(self.poly[i]))
            # 값이 음수일 경우 괄호를 같이 출력
            elif self.poly[i] < 0 : print("(%3.1f)x^%d"%(self.poly[i], i), end = " +")
            # 그 외의 경우에는 값을 그대로 출력
            else : print("%3.1fx^%d"%(self.poly[i], i), end = " +")

a = Polynomial()
b = Polynomial()

a.read_poly()
b.read_poly()
c = a.add(b.poly)
print("a 방정식 : ", end = "")
a.display() 
print("b 방정식 : ", end = "")
b.display() 
print("a + b 방정식 : ", end = "") 
c.display()
print("a + b(2) 방정식 : ", c.evaluate(2))

d = a.subtract(b.poly)
print("a - b 방정식 : ", end = "")
d.display() 

e = a.multiply(b.poly)
print("a * b 방정식 : ", end = "")
e.display() 
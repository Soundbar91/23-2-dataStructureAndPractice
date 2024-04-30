# 추상 자료형 Time의 클래스
class Time:
    # Time 클래스의 생성자
    # 디폴트 매개변수를 설정하였다.
    def __init__(self, c = "Time", h = 0, m = 0, s = 0) :
        self.c = c
        self.h = h
        self.m = m
        self.s = s

    # 매개변수로 전달 받은 이름, 시, 분, 초로 초기화하는 함수
    def set(self, c, h, m, s) :
        self.c = c
        self.h = h
        self.m = m
        self.s = s

    # 각각 시, 분, 초를 반환하는 함수
    def second(self) : return self.s
    def minute(self) : return self.m
    def hour(self) : return self.h

    # 시각이 오전이면 True 그렇지 않으면 False를 반환하는 함수
    def isAM(self) : return self.h < 12
    # 시각이 t와 같으면 True 그렇지 않으면 False를 반환하는 함수
    def isSame(self, t) : return self.h == t.h and self.m == t.m and self.s == t.s
    
    # t와 시, 분, 초의 합을 t에 저장하고 반환하는 함수
    def add(self, t) : 

        t.s = self.s + t.s
        t.m = self.m + t.m
        t.h = self.h + t.h

        return t
    
    # t와 시, 분, 초의 차이를 t에 저장하고 반환하는 함수
    def difference(self, t) :

        t.s = self.s - t.s
        t.m = self.m - t.m
        t.h = self.h - t.h

        return t
    
    # 시간을 보정하는 함수
    def trim(self) :
        
        # 초가 60을 초과했을 때 보정
        if self.s > 60 :
            self.m += self.s // 60
            self.s = self.s % 60
        # 초가 0 미만일 때 보정
        elif self.s < 0 :
            self.s += 60
            self.m -= 1

        # 분이 60을 초과했을 때 보정
        if self.m > 60 :
            self.h += self.m // 60
            self.m = self.m % 60
        # 분이 0 미만일 때 보정
        elif self.m < 0 :
            self.m += 60
            self.h -= 1

    # 화면에 객체 변수의 이름과 시, 분, 초를 출력하는 함수
    def display(self) :
        print("%s : %2d:%2d:%2d"%(self.c, self.h, self.m, self.s))

# 객체 변수 time1, time2를 선언 후 화면에 출력
time1 = Time("time1", 10, 20, 30)
time1.display()
time2 = Time("time2", 8, 24, 1)
time2.display()

# time1과 time2의 차를 time2에 저장하고 이를 화면에 출력
time1.difference(time2)
print("time1 - time2의 보정 전 ", end="")
time2.display()
# time2의 시, 분, 초를 보정 후 화면에 출력
time2.trim()
print("time1 - time2의 보정 후 ", end="")
time2.display()

# 객체변수 time3, time4를 선언하고 일치 여부를 확인
time3 = Time("time3", 20, 40, 50)
time3.display()
time4 = Time("time4", 20, 10, 50)
time4.display()
print("time3과 time의 일치 여부 : ", time3.isSame(time4))

# time3와 time4의 합을 time4에 저장하고 이를 화면에 출력
time3.add(time4)
print("time3 + time4의 보정 전 ", end="")
time4.display()
# time4의 시, 분, 초를 보정 후 화면에 출력
time4.trim()
print("time3 + time4의 보정 후 ", end="")
time4.display()

# 객체 변수 time5를 선언 후 화면에 출력
time5 = Time("time5", 10,40,35)
time5.display()
# time5의 시간이 오전인지 확인
print("time5이 오전인가요 ? : ", time5.isAM())
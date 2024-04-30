# 난수를 발생시키기 위해 random 모듈을 사용한다.
import random

# random 모듈에 있는 randint 함수 사용한다.
# 10부터 99까지 중 임의의 정수를 발생시켜 Answer 변수에 저장한다.
Answer = random.randint(10, 99)
# 힌트를 주기 위한 Min, Max 변수 선언한다.
Min = 10
Max = 99

# 반복문을 10번 돌려 숫자를 입력받는다
for i in range(1, 11) :

    # 사용자로부터 숫자를 입력받는다.
    # 힌트를 주기 위해 Min, Max 변수의 값도 화면에 출력한다.
    print("숫자를 입력하세요(범위:",Min,"~",Max,"):", end="")
    Guess = eval(input())

    # 정답을 맞혔을 때 화면에 시도 횟수와 성공의 메시지를 출력한다.
    # 이후, 프로그램을 종료한다. 
    if Guess == Answer : 
        print("정답입니다.",i,"번 만에 맞추셨습니다.")
        print("게임이 끝났습니다.")
        exit()
    # 정답을 맞히지 못했을 때 힌트를 화면에 출력한다.
    # Min, Max의 값을 사용자가 입력한 값으로 변경한다.
    elif Answer > Guess :
        print(" 아닙니다. 더 큰 숫자입니다.")
        Min = Guess
    elif Answer < Guess :
        print(" 아닙니다. 더 작은 숫자입니다.")
        Max = Guess

print("정답을 맞추지 못하셨습니다.")
print("게임이 끝났습니다.")

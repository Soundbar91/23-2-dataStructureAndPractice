# 클래스로 구현한 클래스를 사용하기 위해 import
from ArrayStack import ArrayStack

# 후위수식을 계산하는 함수
def EvalPostFix(expr) :
    # 스택의 크기를 1000으로 선언
    s = ArrayStack(100)

    # 반복문을 통해 후위 수식을 계산
    # 매개변수로 받은 수식들이 순서대로 token에 들어옴
    for token in expr :
        # 연산자일 경우 연산을 진행한다.
        if token in "+-*/" :
            # 스택에서 피연산자 2개를 함수에서 선언한 스택 s에서 pop해서 변수에 저장한다.
            val2 = s.pop()
            val1 = s.pop()

            # 연산자의 기호에 따라 연산을 진행하여 결과값을 함수에서 선언한 스택에 push한다.
            if token == '+' : s.push(val1 + val2)
            elif token == '-' : s.push(val1 - val2)
            elif token == '*' : s.push(val1 * val2)
            elif token == '/' : s.push(val1 / val2)

        # 피연산자일 경우 함수에서 선언한 스택 s에 실수형으로 형 변환하여 push한다.
        else :
            s.push(float(token))
    # 결과값을 스택 s에서 pop해서 반환한다.
    return s.pop()
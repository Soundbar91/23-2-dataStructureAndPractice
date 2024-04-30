# 클래스로 구현한 클래스를 사용하기 위해 import
from ArrayStack import ArrayStack

# 연산자의 우선순위를 계산하는 함수
# 연산자들은 스택에서 자신의 우선순위보다 낮은 연산자 위에만 올라 탈수 있다.
def precedence(op) :
    # 입력받은 연산자들의 우선순위를 사칙연산에 따라 값을 반환해준다.
    if op == '(' or op == ')' : return 0
    elif op == '+' or op == '-' : return 1
    elif op == '*' or op == '/' : return 2
    else : return -1

# 중위표기 수식을 후위표기로 변환하는 함수
def InFix2PostFix(expr) : 
    # 크기가 100인 스택을 선언
    s = ArrayStack(100)
    # 후위표기 수식을 저장할 리스트 선언
    Output = []

    # 전달받은 중위표기 수식의 각 항들이 순서대로 term에 대입
    for term in expr :
        # 왼쪽 괄호인 경우 함수에서 선언한 스택 s에 push
        if term in '(' :
            s.push('(')

        # 오른쪽 괄호인 경우 
        elif term in ')' :
            # 왼쪽 괄호가 나올 때까지 스택에서 pop해서 후위표기 수식을 저장할 리스트에 추가한다.
            while not s.isEmpty() :
                op = s.pop()
                # 왼쪽 괄호가 나온 경우 반복문을 탈출
                # 후위 표기식에는 괄호가 없기 때문에 따로 스택에 push하지 않는다.
                if op == '(' : break
                else : Output.append(op)

        # 연산자인 경우
        elif term in "+-*/" :
            while not s.isEmpty() :
                # peek를 통해 마지막으로 push된 연산자를 확인한다.
                op = s.peek()
                # 우선순위가 같거나 높으면 후위 표기식을 저장하는 리스트에 추가
                # s 스택에서는 해당 연산자를 pop
                if(precedence(term) <= precedence(op)) :
                    Output.append(op)
                    s.pop()
                # 우선수위가 낮은 연산자인 경우 반복문을 탈출한다.
                else : break
            # 연산자를 s 스택에 push
            # 스택에 있는 연산자는 term 연산자보다 우선순위가 낮음
            s.push(term)

        # 피연산자인 경우 후위표기식을 저장하는 리스트에 추가
        else : 
            Output.append(term)

    # 마지막으로 스택에 남아있는 연산자들을 리스트에 추가
    while not s.isEmpty() :
        Output.append(s.pop())

    # 후위 표기식이 저장된 리스트를 반환
    return Output
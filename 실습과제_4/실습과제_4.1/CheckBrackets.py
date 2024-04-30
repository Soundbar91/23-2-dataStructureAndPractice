# 클래스로 구현한 스택을 사용하기 위해 import
from ArrayStack import ArrayStack

# 괄호 검사 함수
def CheckBrackets(statement) :
    # 스택의 크기를 1000으로 설정
    Stack = ArrayStack(1000) 
    # 에러 코드, 문자수, 라인수를 저장할 변수 선언
    Error_Code = 0
    Cnt_Line = 0
    Cnt_Word = 0

    # 반복문을 통해 괄호를 검사
    # 횟수는 넘겨받은 리스트의 개수만큼 진행
    for i in range(len(statement)) :
        # 한 줄씩 검사를 진행할 때마다 라인 수를 1 증가시킴
        Cnt_Line += 1

        # statement[0] = 코드 파일에서 첫 번째 줄
        # 한 줄씩 검사를 진행한다.
        for ch in statement[i] :
            # 한 글자씩 검사가 시작될 때마다 글자 수를 1 증가시킴
            Cnt_Word += 1

            # ch가 왼쪽 괄호인 경우 스택에 push한다.
            if ch in '{[(':
                Stack.push(ch)

            # ch가 주석의 시작을 알리는 // 혹은 #인 경우 반복문을 탈출하여 다음 줄을 검사하도록 한다.
            elif ch in '//' or ch in '#' : break

            # ch가 오른쪽 괄호인 경우
            elif ch in '}])' :
                # 스택이 비어있다 = 왼쪽 괄호가 없다
                if Stack.isEmpty() : 
                    # 에러코드 2, 라인 수, 단어 수를 반환
                    Error_Code = 2
                    return Error_Code, Cnt_Line, Cnt_Word

                # 스택이 비어있지 않는 경우
                else :
                    # 스택에서 pop
                    left = Stack.pop()
                    # pop해서 나온 괄호가 ch의 괄호와 짝이 맞지 않으면 조건 3을 위배
                    if (ch == "}" and left != "{") or \
                        (ch == "]" and left != "[") or \
                        (ch == ")" and left != "(") :
                        # 에러코드 3, 라인 수, 단어 수를 반환
                        Error_Code = 3                 
                        return Error_Code, Cnt_Line, Cnt_Word
        # 한 줄 검사가 끝났기 때문에 글자 수를 0으로 초기화
        Cnt_Word = 0
        
    # 검사가 다 끝났는데 스택이 비어있지 않는 경우 조건 1을 위배
    # 오류코드 1, 글자수와 문자수는 0으로 반환
    if Stack.isEmpty() != True : 
        Error_Code = 1
        return Error_Code, 0, 0
    
    # 모든 과정을 다 거쳐서 정상인 경우 오류 코드, 글자수, 문자수 모두 0으로 반환
    return 0, 0, 0
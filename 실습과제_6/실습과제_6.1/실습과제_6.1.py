# 클래스로 구현한 단순연결노드
class Node :
    # 단순연결노드의 생성자
    # elem : 자료, link : 링크(디폴트 값으로 None)
    def __init__(self, elem, link = None) :
        self.data = elem
        self.link = link

# 클래스로 구현한 연결된 스택
class LinkedStack :
    # 스택의 생성자
    def __init__(self) :
        # 시작노드를 가르키는 top만 관리하고, 초기 상태는 None
        self.top = None

    # 스택의 공백 상태를 확인하는 함수
    def isEmpty(self) : return self.top == None

    # 스택에 전달받은 변수를 저장하는 함수
    def push(self, e) :
        # 데이터를 e, 링크는 top를 가르키는 노드를 생성
        # top은 해당 노드를 가르킴
        self.top = Node(e, self.top)

    # 스택에 마지막으로 들어온 변수를 빼는 함수
    def pop(self) :
        if not self.isEmpty() :
            # top이 가르키는 노드의 데이터를 저장
            n = self.top.data
            # top은 가리키고 있던 노드의 링크를 타고 다음 노드를 가르킴
            self.top = self.top.link
            # 반환 값으로 n을 반환
            return n
    
    # 스택에 마지막에 들어온 변수를 빼지 않고 확인하는 함수
    def peek(self) :
        if not self.isEmpty() :
            # top이 가르키는 노드의 데이터를 반환
            return self.top.data
    
    # 연결된 스택의 크기를 반환하는 함수
    def size(self) :
        # top이 가르키는 노드를 저장
        # 카운터의 초기 값은 0
        node = self.top
        count = 0

        # node의 값이 None이 될때까지 링크를 계속 타서 다음 노드로 넘어감
        # 넘어 갈 때마다 카운터는 1씩 증가
        while not node == None :
            node = node.link
            count += 1
        
        # 반환값으로 카운터의 값을 반환
        return count
    
    # 결과를 문자열로 출력하기 위한 함수
    def __str__(self) :
        # 스택의 데이터를 저장할 리스트 선언
        # top이 가르키는 노드를 저장
        arr = []
        node = self.top

        # node의 값이 None이 될때까지 링크를 계속 타서 다음 노드로 넘어감
        # 넘어 갈 때마다 노드의 데이터를 리스트에 추가
        while not node == None :
            arr.append(node.data)
            node = node.link

        # 반환 값으로 리스트를 문자열로 변환하여 반환
        return str(arr)

# 괄호 검사 함수
def CheckBrackets(statement) :
    # 연결된 스택 선언
    Stack = LinkedStack() 
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

# 오류코드를 검사하여 어떤 오류가 있는지 출력하는 함수
def Check_Error(Error_Code, Error_Line, Error_Index) :
    
    # 에러 코드가 0이면 이상이 없음을 출력
    if Error_Code == 0 : print("이상 없음")
    # 에러 코드가 1이면 조건 1을 위배했음을 출력
    # 조건 1을 위배했을 때는 왼쪽 괄호의 위치를 출력하기 애매하다고 판단되어 라인수와 문자수는 출력하지 않음
    elif Error_Code == 1 : 
        print("조건 1. 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 다릅니다.")
    # 에러 코드가 2이면 조건 2을 위배했음을 출력
    # 조건 2을 위배했을 때 오류가 생긴 라인 수와 문자 수를 출력
    elif Error_Code == 2 : 
        print("조건 2. 왼쪽 괄호가 오른쪽 괄호보다 먼저 나오지 않았습니다.")
        print("%d라인 %d번째 문자에서 오류가 생겼습니다"%(Error_Line, Error_Index))
    # 에러 코드가 3이면 조건 3을 위배했음을 출력
    # 조건 3을 위배했을 때 오류가 생긴 라인 수와 문자 수를 출력
    elif Error_Code == 3 : 
        print("조건 3. 다른 타입의 괄호 쌍이 서로 교차했습니다.")
        print("%d라인 %d번째 문자에서 오류가 생겼습니다"%(Error_Line, Error_Index))

def main() :
    # 사용자로부터 파일 이름을 입력받는다.
    Input_FileName = input("파일 이름을 입력하세요 (같은 디렉토리 파일명) : ")
    
    # 입력받은 파일을 읽기 모드로 오픈한다.
    # 주석을 읽는 과정에서 cp949 오류가 생겨 encoding = 'UTF-8'를 추가
    InFile = open(Input_FileName, "r", encoding='UTF-8')
    # 파일의 각 줄을 원소로 하는 리스트를 str 변수에 저장
    str = InFile.readlines()
    # 괄호 검사 함수에 매개 변수로 str을 전달
    # 반환 값으로 오류 코드, 라인수, 문자수를 받는다.
    Error_Code, Error_Line, Error_Index = CheckBrackets(str)
    # open했던 파일을 닫는다.
    InFile.close()
    # 반환 받은 오류 코드, 라인수, 문자수를 함수에 전달한다.
    Check_Error(Error_Code, Error_Line, Error_Index)

main()
# CheckBrackets.py로부터 CheckBrackets 함수를 사용하기 위해 import
from CheckBrackets import CheckBrackets

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
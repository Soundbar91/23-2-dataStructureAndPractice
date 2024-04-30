# 클래스로 구현한 스택을 사용하기 위해 import
from ArrayStack import ArrayStack
# InFix2PostFix.py에서 중위 표기식을 후위 표기식으로 변환하는 InFix2PostFix를 사용하기 위해 import
from InFix2PostFix import InFix2PostFix
# EvalPostFix.py에서 후위 표기식을 계산하는 EvalPostFix를 사용하기 위해 import
from EvalPostFix import EvalPostFix

# 사용자로부터 수식을 입력받는다
# 공백으로 구분하기 위해 split()를 사용
InFix_Array = list(input("입력 수식(공백문자로 분리) = ").split())

# 입력받은 중위 표기 수식을 출력
print("중위표기 : ", InFix_Array)
# 중위 표기 수식을 후위 표기식으로 표현하는 함수에 전달
# 후위 표기식으로 바뀐 수식을 출력
print("후위표기 : ", InFix2PostFix(InFix_Array))
# 후위 표기식을 계산하는 함수로 후위 표기식을 전달
# 해당 수식을 계산한 결과를 출력
print("계산결과 : ", EvalPostFix(InFix2PostFix(InFix_Array)))
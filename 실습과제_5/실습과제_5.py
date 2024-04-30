from DrawMaze import *
from MazeBFS import *
from MazeDFS import *
from MazePQueue import *
from Map import *

# 미로찾기 메인 함수
def main() :
    
    # 초기 위치를 저장하는 튜플
    here = (0, 0)
    # 반복문을 통해 맵에서 초기 위치를 찾아 튜플에 저장
    for i in range(len(map)) :
        for j in range(len(map[0])) :
            if map[i][j] == 'e' : 
                here = (j, i)
    drawMaze(here)

    # 탐색이 실패 혹은 종료 키를 입력할 때까지 미로 탐색
    while True :
        # 사용자로부터 문자를 입력받는다.
        print("\n탐색 방법 1 = DFS, 2 = BFS, 3 = PQueue, q = 종료 ==> ", end="")
        Input_Num = input()

        # exit()를 이용하여 프로그램을 종료
        if Input_Num == 'q':
            exit()
        # 깊이우선탐색 함수를 호출하고, 반환값을 result에 저장
        elif Input_Num == '1':
            result = DFS(here)
        # 너비우선탐색 함수를 호출하고, 반환값을 result에 저장
        elif Input_Num == '2':
            result = BFS(here)
        # 유클리디언 거리를 이용한 탐색 함수를 호출하고, 반환값을 result에 저장
        elif Input_Num == '3':
            result = MySmartSearch(here)
        else:
            pass
        
        # result의 값에 따라 출력하는 메세지가 다르도록 작성
        print(' --> 미로탐색 성공' if result else ' --> 미로탐색 실패')
        
        # 값이 변경된 map를 다시 초기화
        for i in range(len(map)) :
            for j in range(len(map[0])) :
                map[i][j] = org[i][j]

main()
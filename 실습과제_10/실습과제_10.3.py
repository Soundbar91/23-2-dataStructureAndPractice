# 자신만의 그래프의 노드 리스트
vertex = ['1', '2', '3', '4', '5', '6', '7', '8']
# 인접 행렬로 표현한 자신만의 그래프
adjMat = [[0, 0, 1, 0, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 1, 0],
          [1, 0, 0, 0, 1, 0, 1, 1],
          [0, 0, 0, 0, 1, 0, 0, 0],
          [1, 0, 1, 1, 0, 0, 0, 0],
          [1, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 0, 0, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 0]]

"""
너비우선탐색(인접 행렬 방식)
매개 변수로 노드 리스트, 방문할 인접 리스트, 시작할 노드의 인덱스를 넘김
방문 리스트는 노드 리스트만큼 크기가 설정이 되있으며 기본값은 False로 설정
방문한 노드에 대해서는 True로 변경하여 방문의 여부를 구별
"""
from queue import Queue
def BFS(vtx, aList, s):
    # visited 리스트 선언
    n = len(vtx)
    visited = [False]*n
    
    # 너비우선탐색에서 사용될 큐 선언
    # 초기 값으로 탐색 시작 인덱스를 put -> 이후 시작 노드에 해당되는 visited 값 Ture로 변경
    Q = Queue()
    Q.put(s)
    visited[s] = True

    """
    반복문을 통해 노드 탐색    
    큐에서 값을 얻고 해당 값을 출력
    
    반복문을 통해 탐색한 노드에서 방문이 가능한 노드 탐색
    방문이 가능한 노드인 경우 큐에 해당 값을 put, 탐색 가능한 노드에 해당되는 visited 값 True로 변경
    """
    while not Q.empty() :
        s = Q.get()
        print(vtx[s], end=' ')
        for v in range(len(aList[s])) :
            if aList[s][v] == 1 and visited[v] == False :
                Q.put(v)
                visited[v] = True

print('BFS(출발:A): ', end="")
BFS(vertex, adjMat, 0)
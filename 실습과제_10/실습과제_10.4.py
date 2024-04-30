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

from queue import Queue
"""
너비우선탐색을 통해 신장트리를 구하는 함수
매개 변수로 노드 리스트, 방문할 인접 행렬, 시작할 노드의 인덱스, 방문 리스트를 넘김
"""
def ST_BFS(vtx, adj, s, visited) :
    # 탐색 시작 노드의 값을 큐에 넣고 해당되는 visited 값을 True로 변경
    visited[s] = True
    Q = Queue()
    Q.put(s)
    
    """
    반복문을 이용하여 신장 트리를 출력
    탐색한 노드에서 방문 가능한 노드를 탐색 후 큐에 put, 탐색 가능한 노드에 해당되는 visited 값 True로 변경
    이후 신장트리를 출력
    """
    while not Q.empty() :
        s = Q.get()
        for v in range(len(adj[s])) :
            if adj[s][v] == 1 and visited[v] == False :
                Q.put(v)
                visited[v] = True
                print("(", vtx[s], vtx[v], ")", end=' ')

print('신장트리(BFS): ', end="")
ST_BFS(vertex, adjMat, 0, [False]*len(vertex))
print()
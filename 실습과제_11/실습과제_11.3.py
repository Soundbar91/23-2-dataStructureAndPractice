# 무한대를 표시하는 값
INF = 9999
# 가중치 합을 저장할 변수
MST_Wight = 0

# dist가 최소인 정점 탐색 함수
def getMinVertex(dist, selected) :
    minv = 0
    mindist = INF
    
    # 정점들 중에서 아직 방문하지 않음 & dist가 가장 작은 정점을 탐색
    for v in range(len(dist)) :
        if selected[v] ==False and dist[v]<mindist :
            mindist = dist[v]
            minv = v
    return minv

def MSTPrim(vertex, adj) :
    vsize = len(vertex)         # 노드의 개수
    dist = [INF] * vsize        # MST에서 i번째 정점까지의 가장 가까운 거리를 저장하는 리스트 -> 초기값은 INF
    selected = [False] * vsize  # 방문의 여부를 저장하는 리스트 -> 초기값은 False
    dist[0] = 0                 # 첫번째 노드에서 출발
    global MST_Wight
    
    for i in range(vsize) :
        # getMinVertex() 함수를 이용하여 아직 방문하지 않은 정점에서 최소 dist 정점을 찾아 방문
        u = getMinVertex(dist, selected)
        selected[u] = True
        print(vertex[u], end=' ')

        """
        위에서 방문한 노드에서 방문하지 않는 노드 탐색 
        해당 노드 중에서 가중치가 시작 노드에서의 가중치보다 작은 경우 가중치를 최신화
        """
        for v in range(vsize) :
            if (adj[u][v] != None) :
                if not selected[v] and adj[u][v]< dist[v] :
                    dist[v] = adj[u][v]
    print()
    MST_Wight = sum(dist)
    
vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [[None, 5, None, None, None, 2, None],
          [5, None, None, None, 10, None, 3],
          [None, None, None, 1, 6, 7, None],
          [None, None, 1, None, 3, None, 11],
          [None, 10, 6, 3, None, 3, 15],
          [2, None, 7, None, 3, None, None],
          [None, 3, None, 11, 15, None, None]]

MSTPrim(vertex, weight)
print("가중치 : %d" % MST_Wight)
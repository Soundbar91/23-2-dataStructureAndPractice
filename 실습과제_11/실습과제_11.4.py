# 무한대를 표시하는 값
INF = 999

# 최단 정점을 선택하는 함수
def choose_vertex(dist, found) :
    min = INF
    minpos = -1

    # 매개변수로 받은 found 리스트에서 아직 방문하지 않는 노드에서 최소 dist를 가지고 있는 정점을 탐색
    for i in range(len(dist)) :
        if dist[i]< min and found[i]==False :
            min = dist[i]
            minpos = i
    return minpos

# Dijkstra 알고리즘
# 매개변수 : 정점 리스트, 인접 행렬, 시작 노드
def shortest_path_dijkstra(vertex, adj, start) :
    vsize = len(vertex)         # 노드의 개수
    dist = list(adj[start])     # dist 초기화 / 초기값은 시작 노드에 해당하는 인접 리스트
    path = [start] * vsize      # path 초기화 / 초기값은 시작 노드
    found= [False] * vsize      # fount초기화 / 초기값은 False

    # 시작 노드 방문
    found[start] = True
    dist[start] = 0

    for i in range(vsize) :
        print("Step%2d: "%(i+1), dist)
        """
        dist와 방문 리스트를 매개변수로 전달
        dist에서 아직 방문하지 않고 최단 dist를 가진 노드 탐색
        이후 해당 노드 방문
        """
        u = choose_vertex(dist, found)
        found[u] = True

        """
        모든 정점에 대해서 방문하지 않는 노드를 검사
        새롭게 탐색한 노드(u)를 거쳐서 가는 가중치가 더 짧은 경우 해당 dist 갱신
        이후, 방문하지 않는 노드(w)의 최단 경로상의 이전 노드는 새롭게 탐색한 노드(u)가 됨
        """
        for w in range(vsize) :
            if not found[w] :
                if (dist[u] + adj[u][w] < dist[w]) :
                    dist[w] = dist[u] + adj[u][w]
                    path[w] = u

    return path

vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [[0, 5, INF, INF, INF, 2, INF],
          [5, 0, INF, INF, 10, INF, 3],
          [INF, INF, 0, 1, 6, 7, INF],
          [INF, INF, 1, 0, 3, INF, 11],
          [INF, 10, 6, 3, 0, 3, 15],
          [2, INF, 7, INF, 3, 0, INF],
          [INF, 3, INF, 11, 15, INF, 0]]

print("Shortest Path By Dijkstra Algorithm")
start = 0
path = shortest_path_dijkstra(vertex, weight, start)

for end in range(len(vertex)) :
    if end != start :
        print("[최단경로: %s->%s] %s" %(vertex[start], vertex[end], vertex[end]), end='')
        while (path[end] != start) :
            print(" <- %s" % vertex[path[end]], end='')
            end = path[end]
        print(" <- %s" % vertex[path[end]])

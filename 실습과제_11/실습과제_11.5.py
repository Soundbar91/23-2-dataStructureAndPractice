# 각 노드의 부모노드 인덱스가 저장되는 리스트
parent = []
# 노드의 전체 집합의 개수
set_size = 0
# 가중치 합을 저장할 변수
MST_Wight = 0

# Union-Find의 초기화 함수
def init_set(nSets) :
    """
    매개변수로 받은 전체 집합의 개수를 전역변수에 저장
    반복문을 이용하여 보무노드 인덱스가 저장되는 전역 리스트 초기화
    초기화 단계에서는 각 노드가 고유의 집합 -> 각 노드가 부모 노드임 -> -1로 초기화
    """
    global set_size, parent 
    set_size = nSets
    for i in range(nSets):
        parent.append(-1)

# 매개 변수로 받은 노드가 속하는 집합(트리)의 부모노드를 탐색하는 함수
def find(id) :
    """
    반복문을 이용하여 부모노드 탐색
    부모노드의 경우 parent 리스트에 -1로 저장이 되어있음
    """
    while (parent[id] >= 0) :
        id = parent[id]
    return id

# 매개변수로 받은 두 집합을 병합하는 함수
def union(s1, s2) :
    """
    매개 변수로 받은 두 집합을 병합 -> 현재는 s1이 s2에 병합됨
    parent 리스트에 저장된 s1의 부모 노드를 s2로 변경하여 병합
    병합이 되었기 때문에 전체 집합의 개수 -1
    """
    global set_size
    parent[s1] = s2
    set_size = set_size - 1


# Kruskal의 MST 알고리즘
def MSTKruskal(vertex, adj) :
    # 정점의 개수와 init_set 함수를 이용하여 초기화 진행
    vsize = len(vertex)
    init_set(vsize)
    global MST_Wight
    
    # 매개변수로 받은 인접행렬의 간선을 반복문을 이용하여 튜플 형태로 리스트에 저장
    eList = []
    for i in range(vsize-1) :
        for j in range(i+1, vsize) :
            if adj[i][j] != None :
                eList.append((i,j,adj[i][j]))

    # 간선 리스트를 가중치의 오름차순으로 정렬
    # 람다 함수를 이용 / 튜플로 저장된 간선에서 가중치(e[2])를 비교해서 정렬
    eList.sort(key= lambda e : e[2], reverse=False)

    # Kruskal의 MST 알고리즘을 통해 형성된 가중치 그래프의 간선의 개수
    # n - 1개의 간선이 생성될 때까지 반복문을 통해 간선을 추가 (n = 노드의 개수)
    edgeAccepted = 0
    while (edgeAccepted < vsize - 1) :
        """
        정렬된 리스트에서 최소 가중치 간선을 꺼낸다.
        해당 간선에서 양쪽 노드의 부모 노드를 find()함수를 이용하여 구한다.
        두 노드의 부모노드가 동일하지 않다 -> 사이클이 생기지 않는다 -> union() 함수를 이용하여 두 노드 간 간선 추가
        """
        e = eList.pop()
        uset = find(e[0])
        vset = find(e[1])

        if uset != vset :
            print("간선 추가 : (%s, %s, %d)" % (vertex[e[0]], vertex[e[1]], e[2]))
            MST_Wight += e[2]
            union(uset, vset)
            edgeAccepted += 1
            
vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [[None, 5, None, None, None, 2, None],
          [5, None, None, None, 10, None, 3],
          [None, None, None, 1, 6, 7, None],
          [None, None, 1, None, 3, None, 11],
          [None, 10, 6, 3, None, 3, 15],
          [2, None, 7, None, 3, None, None],
          [None, 3, None, 11, 15, None, None]]

MSTKruskal(vertex, weight)
print("가중치 : %d" % MST_Wight)
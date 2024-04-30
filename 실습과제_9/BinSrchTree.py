# 이진탐색트리를 위한 노드 클래스
class BSTNode :
    # 각 노드의 탐색 키와 기에 대한 값을 관리한다.
    # 왼쪽 자식 노드와 오른쪽 자식 노드의 링크도 관리한다.
    def __init__(self, key, value) :
        self.key = key
        self.value = value
        self.left = None
        self.right = None

# 이진탐색트리의 탐색 연산(순환 구조)
def SearchBST(node, key) :
    # node가 Node까지 탐색
    # 노드의 값과 탐색하는 값이 같으면 해당 노드로 반환
    # 큰 경우 오른쪽 노드, 작은 경우 왼쪽 노드로 탐색
    if node == None :
        return None
    elif key == node.key:
        return node
    elif key < node.key:
        return SearchBST(node.left, key)
    else:
        return SearchBST(node.right, key)

# 이진탐색트리의 값을 이용한 탐색 연산
def SearchBSTValue(node, value) :
    # 노드의 값이 None이면 해당 값이 없음
    # 노드의 값과 같은 경우 탐색 성공
    if node == None : return None
    elif value == node.value :
        return node
    
    # 왼쪽 서브트리부터 탐색 시작
    res = SearchBSTValue(node.left, value) 
    # 왼쪽 서브트리에서 탐색한 결과가 None 아니면 탐색 성공
    if res is not None :
        return res
    # None인 경우 왼쪽 서브트리에 없음 -> 오른쪽 서브트리에서 탐색
    else :
        return SearchBSTValue(node.right, value)
    
# 최대 키를 가지는 노드 탐색 함수
def SerachMaxBST(node) :
    # 최대 키를 가지고 있는 노드는 오른쪽 서브트리에 있다.
    # n과 n의 오른쪽 자식이 None이 될 때까지 오른쪽 서브트리를 탐색한다. -> 가자 오른쪽 노드로 이동
    while node != None and node.right != None :
        node = node.right

    return node

# 최대 키를 가지는 노드 탐색 함수 - 순환
def SerachMaxBST_ver1(node) :
    # 노드의 오른쪽 자식이 None인 경우 해당 노드가 최대값
    if node.right is None:
        return node

    # 그렇지 않는 경우에는 오른쪽 노드로 계속 함수를 호출
    else : return SerachMaxBST_ver1(node.right)

# 최소 키를 가지는 노드 탐색 함수
def SerachMinBST(node) :
    # 최소 키를 가지고 있는 노드는 왼쪽 서브트리에 있다.
    # n과 n의 왼쪽 자식이 None이 될 때까지 왼쪽 서브트리를 탐색한다. -> 가장 왼쪽 노드로 이동
    while node != None and node.left != None :
        node = node.left
    return node

# 최소 키를 가지는 노드 탐색 함수 - 순환
def SerachMinBST_ver1(node) :
    # 노드의 왼쪽 자식이 None인 경우 해당 노드가 최솟값
    if node.left is None:
        return node

    # 그렇지 않는 경우에는 왼쪽 노드로 계속 함수를 호출
    else : return SerachMinBST_ver1(node.left)

# 이진탐색트리에 노드를 삽입하는 함수
def InsertBST(root, node) :
    # 공백노드에 도달하게 되면 해당 위치에 node 삽입
    if root == None :
        return node
    
    # 이진탐색트리에 중복으로 키 값을 허용하지 않음
    # 키 값이 동일한 노드가 존재할 경우 삽입이 이뤄지지 않고 그대로 root 반환
    if node.key == root.key :
        return root
    
    # 키값이 root의 키 값보다 작은 경우 왼쪽 노드로 삽입 함수를 순환 호출
    if node.key < root.key :
        root.left = InsertBST(root.left, node)
    
    # 키값이 root의 키 값보다 큰 경우 오른쪽 노드로 삽입 함수를 순환 호출   
    else :
        root.right = InsertBST(root.right, node)
    
    # 삽입이 끝난 root 반환
    return root

# 이진탐색트리에 노드를 삽입하는 함수 - 반복
def InsertBST_ver1(root, node) :
    # 공백노드에 도달하게 되면 해당 위치에 node 삽입
    if root is None:
        return node

    # 반복문으로 움직이는 동안 현재 노드를 가르키는 노드 선언
    Current = root
    while True:
        # 키 값이 동일한 노드가 존재할 경우 root 반환
        if node.key == Current.key:
            return root

        # 키값이 current의 키 값보다 작은 경우 왼쪽 노드로 이동
        if node.key < Current.key:
            # 만약 노드의 왼쪽 서브트리가 None인 경우 해당 위치에 삽입
            if Current.left is None:
                Current.left = node
                return root
            else:
                Current = Current.left

        # 키값이 current의 키 값보다 큰 경우 오른쪽 노드로 이동
        else:
            # 만약 노드의 오른쪽 서브트리가 None인 경우 해당 위치에 삽입
            if Current.right is None:
                Current.right = node
                return root
            else:
                Current = Current.right

# 이진탐색트리에 노드를 삭제하는 함수
def DeleteBST(root, key) :
    if root == None :
        return root
    
    # key가 루트보다 작거나 클 경우 
    # 해당 자식이 루트인 서브트리에 순환 호출하여 삭제를 진행
    if key < root.key :
        root.left = DeleteBST(root.left, key)   
    elif key > root.key :
        root.right = DeleteBST(root.right, key)
        
    # key가 루트와 같은 경우
    # 삭제를 진행
    else :
        # 단말 노드 또는 오른쪽 자식만 있는 경우
        if root.left == None :
            return root.right
        
        # 왼쪽 자식만 있는 경우
        if root.right == None :
            return root.left
        
        # 왼쪽, 오른쪽 모두 있는 경우
        # 루트의 오른쪽 서브트리에서 최솟값(후계자)를 찾음
        # 후계자의 값을 루트에 복사하고 후계자를 삭제
        succ = SerachMinBST(root.right)
        root.key = succ.key
        root.value = succ.value
        root.right = DeleteBST(root.right, succ.key)
        
    return root
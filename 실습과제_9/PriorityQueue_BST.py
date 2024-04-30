from BinSrchTree import *

# 중위순회 함수
def Inorder(node) :
    # 왼쪽 -> 루트 -> 오른쪽
    if node is not None :
        Inorder(node.left)
        print(node.key, end=' ')
        Inorder(node.right)

# 이진탐색트리를 이용한 우선순위 큐
class PriorityQueue_BST :
    
    # 우선순위 큐의 생성자
    # 시작 루트를 가르키는 root만 관리
    def __init__(self) :
        self.root = None

    # 우선순위 큐의 공백상태를 확인하는 함수
    def isEmpty(self) : return self.root == None

    # 우선순위 큐에 삽입하는 함수
    # 값와 키값이 동일한 노드를 생성하여 이진탐색트리에 삽입
    def enqueue(self, value):
        node = BSTNode(value, value)
        self.root = InsertBST(self.root, node)
    
    # 우선순위 큐에서 삭제하는 함수
    # 최대 키 노드를 찾아 삭제
    def dequeue(self):
        self.root = DeleteBST(self.root, SerachMaxBST(self.root).key)
    
    # 우선순위 큐에서 최대값을 반환하는 함수
    # 최대 키 노드를 찾아 반환
    def peek(self):
        return SerachMaxBST(self.root).value
    
    # 우선순위 큐를 출력하는 함수
    def Display(self, msg = 'BTSMap :') :
        print(msg, end='')
        Inorder(self.root)
        print()
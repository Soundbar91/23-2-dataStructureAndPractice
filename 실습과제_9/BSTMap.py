from BinSrchTree import *

# 중위순회 함수
def Inorder(node) :
    # 왼쪽 -> 루트 -> 오른쪽
    if node is not None :
        Inorder(node.left)
        print(node.key, end=' ')
        Inorder(node.right)

# 이진탐색트리를 이용한 맵 클래스
class BSTMap() :
    
    # 맵의 생성을 담당하는 생성자
    # 루트 노드를 가르킬 변수 root만 관리
    def __init__(self) :
        self.root = None
        
    # 공백상태를 검사하는 함수
    def isEmpty(self) :
        return self.root == None
    
    # 최대 노드를 탐색하는 함수
    def FindMax(self) :
        return SerachMaxBST(self.root)
    
    # 최대 노드를 탐색하는 함수 - 순환
    def FindMax_ver1(self) :
        return SerachMaxBST_ver1(self.root)
    
    # 최소 노드를 탐색하는 함수
    def FindMin(self) :
        return SerachMinBST(self.root)
    
    # 최소 노드를 탐색하는 함수 - 순환
    def FindMin_ver1(self) :
        return SerachMinBST_ver1(self.root)
    
    # 노드를 탐색하는 함수
    def Search(self, key) :
        return SearchBST(self.root, key)
    
    # 값을 이용하여 노드를 탐색하는 함수
    def SearchValue(self, value) :
        return SearchBSTValue(self.root, value)
    
    # 새로운 노드를 삽입하는 함수
    def Insert(self, key, value = None) :
        # 매개변수로 받은 키, 값으로 삽입할 새로운 노드 생성
        # 삽입 함수를 호출하여 노드가 삽입된 결과를 root에 저장
        n = BSTNode(key, value)
        self.root = InsertBST(self.root, n)
    
    # 새로운 노드를 삽입하는 함수 - 반복
    def Insert_ver1(self, key, value = None) :
        # 매개변수로 받은 키, 값으로 삽입할 새로운 노드 생성
        # 삽입 함수를 호출하여 노드가 삽입된 결과를 root에 저장
        n = BSTNode(key, value)
        self.root = InsertBST_ver1(self.root, n)  
        
    # 노드를 삭제하는 함수
    def Delete(self, key) :
        self.root = DeleteBST(self.root, key)
        
    # 맵을 화면에 출력하는 함수
    def Display(self, msg = 'BTSMap :') :
        print(msg, end='')
        Inorder(self.root)
        print()
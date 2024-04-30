# 이진트리를 위한 노드 클래스
class TNode :
    # 노드의 데이터, 왼쪽 자식의 링크, 오른쪽 자식의 링크를 관리
    def __init__ (self, data, left, right) :
        self.data = data
        self.left = left
        self.right = right
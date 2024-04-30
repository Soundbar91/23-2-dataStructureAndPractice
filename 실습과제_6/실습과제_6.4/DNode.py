# 전단과 후단 노드의 정보를 가지고 있는 노드
# prev는 전단 노드, next는 후단 노드
class DNode :
    def __init__ (self, elem, prev = None, next = None) :
        self.data = elem
        self.prev = prev
        self.next = next
# 클래스로 구현한 단순연결노드
class Node :
    # 단순연결노드의 생성자
    # elem : 자료, link : 링크(디폴트 값으로 None)
    def __init__(self, elem, link = None) :
        self.data = elem
        self.link = link
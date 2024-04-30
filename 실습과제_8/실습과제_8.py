from TNode import TNode     
from CircularQueue import CircularQueue

# 연습문제 8.19
# 이진트리의 높이를 구하는 함수
def calc_height(n) :
    # 참조하는 노드가 None인 경우 0 반환
    if n is None : return 0
    
    # 재귀를 통해 왼쪽 서브트리와 오른쪽 서브트리의 높이를 계산
    # 이후, 제일 큰 높이값에 1를 더한 값을 반환
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    
    if (hLeft > hRight) : return hLeft + 1
    else: return hRight + 1

# 완전이진트리인지를 검사하는 함수
def is_complete_binary_tree(root) :
    # 원형 큐를 이용해서 이진트리를 순회한다
    queue = CircularQueue(50)
    queue.enqueue(root)
    
    # 이진트리의 높이를 저장하는 변수
    # None 이후에 노드가 있는지 확인하기 위한 bool 변수
    cnt = calc_height(root)
    state = False
    
    # 1 ~ cnt - 1 레벨까지의 노드를 순회해서 검사
    # 완전이진트리의 경우 마지막 레벨 전(cnt - 1)까지는 모든 노드가 있어야함
    for i in range((2 ** (cnt - 1)) - 1) :
        n = queue.dequeue()
        if n == None :
            return False
        else :
            queue.enqueue(n.left)
            queue.enqueue(n.right)
    
    # cnt 레벨의 노드가 있는 원형 큐 검사
    while not queue.isEmpty() :
        n = queue.dequeue()
        
        # n의 값이 None이고 state가 False -> 처음으로 None 값이 나왔다 / state를 True로 변경
        # n의 값이 None이 아니고 state가 True -> None이 나왔었고 이후에 노드의 값이 있다 -> 마지막 레벨의 노드에서 중간에 빈 곳이 있다.
        if n == None and not state : state = True
        elif n != None and state : return False
    
    return True

two = TNode('2', None, None)
nine = TNode('9', None, None)
six = TNode('6', None, None)
seven = TNode('7', None, nine)
three = TNode('3', six, seven)
one = TNode('1', two, three)

print("완전 이진 트리의 여부 : ", is_complete_binary_tree(one)) 

c = TNode('C', None, None)
d = TNode('D', None, None)
b = TNode('B', c, d)
f = TNode('F', None, None)
e = TNode('C', None, f)
root = TNode('A', b, e)

print("완전 이진 트리의 여부 : ", is_complete_binary_tree(root)) 

######################################################################################

# 연습문제 8.20
# 임의의 node의 레벨을 구하는 함수
def level(root, node) :
    # 원형 큐를 이용해서 이진트리를 순회한다
    queue = CircularQueue(50)
    queue.enqueue(root)
    # 이진트리의 높이를 저장하는 변수
    cnt = calc_height(root)
    
    # 원형 큐를 이용해서 1 ~ cnt까지 이진트리를 순회
    for i in range(1, cnt + 1) :
        # 각 레벨에 있는 노드 검사
        for j in range((2 ** i) - 1) :
            # n이 None인 경우 다음 노드 검사
            # n과 node가 같은 경우 해당 레벨 반환
            # 그 외의 경우에는 n의 왼쪽 링크와 오른쪽 링크를 원형 큐에 저장
            n = queue.dequeue()
            if n == None : continue
            
            if n == node :
                return i
            else :
                queue.enqueue(n.left)
                queue.enqueue(n.right)

    # 이진트리에 해당 노드가 없으므로 0 반환
    return 0

ten = TNode('10', None, None)
print("노드 ten의 레벨 : ",level(one, ten))
print("노드 one의 레벨 : ",level(one, three))

g = TNode('g', None, None)
print("노드 e의 레벨 : ",level(root, e))
print("노드 g의 레벨 : ",level(root, g))

######################################################################################

# 연습문제 8.21
# 이진트리가 균형 잡혀있는지를 검사하는 함수
def is_balanced(root) :
    # 높이를 구하는 함수를 통해 왼쪽 서브트리와 오른쪽 서브트리의 높이를 계산 후 1를 더한다
    hLeft = calc_height(root.left) + 1
    hRight = calc_height(root.right) + 1
    
    # 두 높이의 차의 절댓값이 2보다 작으면 True -> 균형 잡혀 있다
    # 그렇지 않는 경우 False -> 균형이 잡혀 있지 않다
    if abs(hLeft - hRight) < 2 : return True
    else : return False

print("이진트리의 균형 여부 : ",is_balanced(one))
print("이진트리의 균형 여부 : ",is_balanced(root))
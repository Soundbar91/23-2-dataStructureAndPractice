from Map import map

# 위치를 보정하는 함수
# 매개변수로 받은 위치가 미로에서 벗어났는지 검사
# 이후, 이동할 수 있는 곳인지 검사하여 움직일 수 있으면 True, 그렇지 않으면 False를 반환
def isValidPos(x, y) :
    if 0 <= x < len(map[0]) and 0 <= y < len(map) :
        if map[y][x] == '0' or map[y][x] == 'x' : return True
    return False
from BSTMap import *

data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]
value= ["삼오", "일팔", "영칠", "이육", "일이", "영삼", "육팔", "이이", "삼영", "구구"]

map = BSTMap()
map.Display("[삽입 전] : ")
for i in range(len(data)) :
    map.Insert_ver1(data[i],value[i])
    map.Display("[삽입  - 반복 %2d] : "%data[i])

print('[최대 키 - 순환] : ', map.FindMax_ver1().key)
print('[최소 키 - 순환] : ', map.FindMin_ver1().key)
print('[탐색 26] : ', '성공' if map.Search(26) != None else '실패')
print('[탐색 25] : ', '성공' if map.Search(25) != None else '실패')
print('[탐색 일팔]:', '성공' if map.SearchValue("일팔") != None else '실패')
print('[탐색 일칠]:', '성공' if map.SearchValue("일칠") != None else '실패')
    
map.Delete(3)
map.Display("[삭제  3] : ")
map.Delete(68)
map.Display("[삭제 68] : ")
map.Delete(18) 
map.Display("[삭제 18] : ")
map.Delete(35) 
map.Display("[삭제 35] : ")

data1 = ["A", "F", "C", "E", "G", "B", "D", "H", "J", "I"]
value1 = ["에이", "에프", "씨", "이", "쥐", "비", "디", "에이치", "제이", "아이"]

map1 = BSTMap()
map1.Display("[삽입 전] : ")
for i in range(len(data1)) :
    map1.Insert_ver1(data1[i],value1[i])
    map1.Display("[삽입  - 반복 %c] : "%data1[i])

print('[최대 키 - 순환] : ', map.FindMax_ver1().key)
print('[최소 키 - 순환] : ', map.FindMin_ver1().key)
print('[탐색 A] : ', '성공' if map1.Search("A") != None else '실패')
print('[탐색 Z] : ', '성공' if map1.Search("Z") != None else '실패')
print('[탐색 에이치]:', '성공' if map1.SearchValue("에이치") != None else '실패')
print('[탐색 더블유]:', '성공' if map1.SearchValue("더블유") != None else '실패')
    
map1.Delete("I")
map1.Display("[삭제 I] : ")
map1.Delete("B")
map1.Display("[삭제 B] : ")
map1.Delete("G") 
map1.Display("[삭제 G] : ")
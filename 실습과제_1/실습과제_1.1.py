def contains(Bag, e):
    return e in Bag

def insert(Bag , e):
    Bag.append(e)

def remove(Bag, e):
    Bag.remove(e)

def count(Bag):
    return len(Bag)

def numOf(Bag, item):
    count = 0

    for i in range(len(Bag)) :
        if Bag[i] == item :
            count = count + 1
    return count

myBag = []
insert(myBag, '휴대폰')
insert(myBag, '지갑')
insert(myBag, '손수건')
insert(myBag, '빗')
insert(myBag, '자료구조')
insert(myBag, '야구공')
print('가방속의 물건 : ', myBag)
print('가방속에 노트북의 유무 : ', contains(myBag, '노트북'))

insert(myBag, '빗')
insert(myBag, '노트북')
remove(myBag, '손수건')
print('가방속의 물건 : ', myBag)
print('가방속 물건의 개수 : ', count(myBag))
print('노트북의 개수 : ', numOf(myBag, '노트북'))

pencil_case = []
insert(pencil_case, '연필')
insert(pencil_case, '지우개')
insert(pencil_case, '볼펜')
print('필통 속 물건 : ', pencil_case)
print('필통속에 수정테이프의 유무 : ', contains(pencil_case, '수정테이프'))
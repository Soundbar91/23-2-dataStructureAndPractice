# 총 세금을 저장할 변수를 선언한다.
Tax_Total = 0
# 소득 기준을 리스트로 선언한다.
Tax_Standard = [15000, 8800, 4600, 1200, 0]
# 근로소득세율을 리스트로 선언한다.
Tax_Rate = [0.38, 0.35, 0.24, 0.15, 0.06]

# 사용자로부터 연봉을 입력받는다.
Cost = eval(input("연봉을 입력하세요 ==> ")) 
# 세후 소득을 계산하기 위해 사용자로부터 입력받은 연봉을 Cost_After 변수에 저장한다.
Cost_After = Cost

# 반복문을 이용하여 총 세금을 계산한다.
for i in range(len(Tax_Rate)) :

    # 연봉과 세금 기준을 비교하여 해당 소득 분위에서 세금을 계산한다.
    if Cost > Tax_Standard[i] :
        Tax_Total += (Cost - Tax_Standard[i]) * Tax_Rate[i]
        Cost = Tax_Standard[i]

# 계산된 세금을 화면에 출력한다
print(" 전체 세금 = ", Tax_Total)
# 세후 소득을 화면에 출력한다
print(" 순수 소득 = ", Cost_After - Tax_Total)

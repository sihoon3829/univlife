# 자판기는 반복하여 동작
# 오렌지주스 100, 커피 200, 콜라 300 판매
# 구매자에게 동전 액수와 주문번호 1,2,3 을 받음
# 입력 받은 액수보다 메뉴가 비싸면 잔액이 부족하다고 출력
# 메뉴가 잘못 입력되면 없는 메뉴 다시입력해주세요 라고 출력
# 자판기는 주문과 동시에 잔액을 알려주고 반환

orange = 100
coffee = 200
cola = 300

money = int(input("금액을 입력해주세요: "))

i = 1
while i <= 9:
    menu = int(input("메뉴 1:오렌지주스(100원) 2:커피(200원) 3:콜라(300원): "))

    if menu == 1:
        if money >= orange:
            print("오렌지주스를 고르셨네요")
            money -= orange
        else:
            print("잔액이 부족합니다.")
    elif menu == 2:
        if money >= coffee:
            print("커피를 고르셨네요")
            money -= coffee
        else:
            print("잔액이 부족합니다.")
    elif menu == 3:
        if money >= cola:
            print("콜라를 고르셨네요")
            money -= cola
        else:
            print("잔액이 부족합니다.")
    else:
        print("없는 메뉴입니다. 다시 입력해주세요")
        continue

    print("현재 잔액:", money, "원")
    i += 1

print("거스름돈을 반환합니다:", money, "원")


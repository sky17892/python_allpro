numList = []
dataCount = 0

class SearchPhone:

    def inputAddr(self):
        global dataCount

        idid = input("아이디 입력 : ")
        nameval = input("이름 입력 : ")
        addr123 = input("주소 입력 : ")
        hpphone = input("번호 입력 : ")

        numList.append({
            "id": idid,
            "name": nameval,
            "addr": addr123,
            "hp": hpphone
        })

        dataCount += 1
        print("저장 완료!")

    def searchPhone(self):
        search = int(input("1. 아이디검색\n2. 이름검색\n3. 주소검색\n4. 번호검색\n선택: "))

        key = None
        value = None

        if search == 1:
            key = "id"
            value = input("아이디 검색 : ")
        elif search == 2:
            key = "name"
            value = input("이름 검색 : ")
        elif search == 3:
            key = "addr"
            value = input("주소 검색 : ")
        elif search == 4:
            key = "hp"
            value = input("번호 검색 : ")
        else:
            print("숫자 잘못 입력함!")
            return

        found = False
        for data in numList:
            if data[key] == value:
                print("\n아이디:", data["id"])
                print("이름:", data["name"])
                print("주소:", data["addr"])
                print("번호:", data["hp"])
                found = True

        if not found:
            print("검색 결과 없음")

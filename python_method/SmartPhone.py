numList = []
numList123 = []
numList12345 = []
dataCount = 0

class SearchPhone:

    def InputAddr(self):
        global dataCount

        idid = input("아이디 입력 : ")
        nameval = input("이름 입력 : ")
        hpphone = input("번호 입력 : ")
        email123 = input("이메일 입력 : ")
        addr123 = input("주소 입력 : ")
        groupaaa = input("그룹 입력 : ")
        groupbbb = input("그룹2 입력 : ")
        birth = input("생일 입력 : ")
        grade = input("직급 입력 : ")


        numList.append({
            "idid": idid,
            "nameval": nameval,
            "hpphone": hpphone,
            "email123": email123,
            "addr123": addr123,
            "groupaaa": groupaaa,
            "groupbbb": groupbbb,
            "birth": birth,
            "grade": grade,
        })        

        dataCount += 1
        print("모든 연락처 저장 완료!")
    
    def CompanyAddr(self):
        global dataCount

        id = input("아이디 입력 : ")
        groupa = input("회사 입력 : ")
        groupb = input("부서 입력 : ")
        grade = input("직급 입력 : ")

        numList123.append({
            "id": id,
            "groupa": groupa,
            "groupb": groupb,
            "grade": grade
        })

        dataCount += 1
        print("저장 완료!")

    def CustomerAddr(self):
        global dataCount

        id123 = input("아이디 입력 : ")
        groupaaa = input("거래처 이름 입력 : ")
        groupbbb = input("품목이름 입력 : ")
        gradeabc = input("직급 입력 : ")

        numList12345.append({
            "id123": id123,
            "groupaaa": groupaaa,
            "groupbbb": groupbbb,
            "gradeabc": gradeabc
        })

        dataCount += 1
        print("저장 완료!")

    def SearchPhone(self):
        search = int(input("1. 아이디검색\n2. 회사검색\n3. 부서검색\n4. 직급검색\n선택: "))

        key = None
        value = None

        if search == 1:
            key = "id"
            value = input("아이디 검색 : ")
        elif search == 2:
            key = "groupa"
            value = input("회사 검색 : ")
        elif search == 3:
            key = "groupb"
            value = input("부서 검색 : ")
        elif search == 4:
            key = "grade"
            value = input("직급 검색 : ")
        else:
            print("숫자 잘못 입력함!")
            return

        found = False
        for data123 in numList123:
            if data123[key] == value:
                print("\n아이디:", data123["id"])
                print("회사:", data123["groupa"])
                print("부서:", data123["groupb"])
                print("직급:", data123["grade"])
                found = True

        if not found:
            print("검색 결과 없음")

    def SearchPhone2(self):
        search = int(input("1. 아이디검색\n2. 거래처 이름검색\n3. 품목이름검색\n4. 직급검색\n선택: "))

        key = None
        value = None

        if search == 1:
            key = "id123"
            value = input("아이디 검색 : ")
        elif search == 2:
            key = "groupaaa"
            value = input("거래처 이름 검색 : ")
        elif search == 3:
            key = "groupbbb"
            value = input("품목이름 검색 : ")
        elif search == 4:
            key = "gradeabc"
            value = input("직급 검색 : ")
        else:
            print("숫자 잘못 입력함!")
            return

        found = False
        for data12345 in numList12345:
            if data12345[key] == value:
                print("\n아이디:", data12345["id123"])
                print("거래처 이름:", data12345["groupaaa"])
                print("품목이름:", data12345["groupbbb"])
                print("직급:", data12345["gradeabc"])
                found = True

        if not found:
            print("검색 결과 없음")

    def allPhone(self):
        search = int(input("1. 아이디검색 선택\n: "))

        key = None
        value = None
       
        
        if search == 1:
            key = "idid"
            value = input("아이디 검색 : ")   
        elif search == 2:
            key = "addr123"
            value = input("그룹 검색 : ")
        elif search == 3:
            key = "groupaaa"
            value = input("그룹2 검색 : ")
        elif search == 4:
            key = "groupbbb"     
        else:
            print("숫자 잘못 입력함!")
            return

        for addr in numList:
            if addr[key] == value:
                print("\n아이디:", addr["idid"])
                print("이름:", addr["nameval"])
                print("번호:", addr["hpphone"])
                print("이메일:", addr["email123"])
                print("주소:", addr["addr123"])
                print("그룹:", addr["groupaaa"]) 
                print("그룹2:", addr["groupbbb"]) 
                print("생일:", addr["birth"]) 
                print("직급:", addr["grade"])                            
                found = True

        if not found:
            print("검색 결과 없음")

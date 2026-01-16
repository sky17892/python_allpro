numList = []
numList123 = []
numList12345 = []
dataCount = 0

class SearchPhone:

    def inputAddr(self):
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
            "id": idid,
            "name": nameval,
            "hp": hpphone,
            "email": email123,
            "addr": addr123,
            "groupa": groupaaa,
            "groupb": groupbbb,
            "birth": birth,
            "grade": grade,
        })        

        dataCount += 1
        print("모든 연락처 저장 완료!")
    
    def companyAddr(self):
        global dataCount

        ididid = input("아이디 입력 : ")
        groupagroupa = input("회사 입력 : ")
        groupbgroupb = input("부서 입력 : ")
        gradegrade = input("직급 입력 : ")

        numList123.append({
            "ididid": ididid,
            "groupagroupa": groupagroupa,
            "groupbgroupb": groupbgroupb,
            "gradegrade": gradegrade
        })

        dataCount += 1
        print("저장 완료!")

    def costomerAddr(self):
        global dataCount

        ididididid = input("아이디 입력 : ")
        groupagroupaaa = input("거래처 이름 입력 : ")
        groupbgroupbbb = input("품목이름 입력 : ")
        gradegradeabc = input("직급 입력 : ")

        numList12345.append({
            "ididididid": ididididid,
            "groupagroupaaa": groupagroupaaa,
            "groupbgroupbbb": groupbgroupbbb,
            "gradegradeabc": gradegradeabc
        })

        dataCount += 1
        print("저장 완료!")

    def searchPhone(self):
        search = int(input("1. 아이디검색\n2. 회사검색\n3. 부서검색\n4. 직급검색\n선택: "))

        key = None
        value = None

        if search == 1:
            key = "ididid"
            value = input("아이디 검색 : ")
        elif search == 2:
            key = "groupagroupa"
            value = input("회사 검색 : ")
        elif search == 3:
            key = "groupbgroupb"
            value = input("부서 검색 : ")
        elif search == 4:
            key = "gradegrade"
            value = input("직급 검색 : ")
        else:
            print("숫자 잘못 입력함!")
            return

        found = False
        for data123 in numList123:
            if data123[key] == value:
                print("\n아이디:", data123["ididid"])
                print("회사:", data123["groupagroupa"])
                print("부서:", data123["groupbgroupb"])
                print("직급:", data123["gradegrade"])
                found = True

        if not found:
            print("검색 결과 없음")

    def searchPhone2(self):
        search = int(input("1. 아이디검색\n2. 거래처 이름검색\n3. 품목이름검색\n4. 직급검색\n선택: "))

        key = None
        value = None

        if search == 1:
            key = "ididididid"
            value = input("아이디 검색 : ")
        elif search == 2:
            key = "groupagroupaaa"
            value = input("거래처 이름 검색 : ")
        elif search == 3:
            key = "groupbgroupbbb"
            value = input("품목이름 검색 : ")
        elif search == 4:
            key = "gradegradeabc"
            value = input("직급 검색 : ")
        else:
            print("숫자 잘못 입력함!")
            return

        found = False
        for data12345 in numList12345:
            if data12345[key] == value:
                print("\n아이디:", data12345["ididididid"])
                print("거래처 이름:", data12345["groupagroupaaa"])
                print("품목이름:", data12345["groupbgroupbbb"])
                print("직급:", data12345["gradegradeabc"])
                found = True

        if not found:
            print("검색 결과 없음")

    #def allPhone(self):
    #    search = int(input("1. 아이디검색 선택: "))

    #    key = None
    #    value = None
       
        
        #if search == 1:
        #    key = "ididididid"
        #    value = input("아이디 검색 : ")
        #elif search == 2:
        #    key = "groupagroupaaa"
        #    value = input("거래처 이름 검색 : ")
        #elif search == 3:
        #    key = "groupbgroupbbb"
        #    value = input("품목이름 검색 : ")
        #elif search == 4:
        #    key = "gradegradeabc"
        #    value = input("직급 검색 : ")
        #else:
        #    print("숫자 잘못 입력함!")
        #    return
    #    if search == 1:
    #        key = "idid"
    #        value = input("아이디 검색 : ")

    #    for data in numList:
    #        if data[key] == value:
    #            print("\n아이디:", data["id"])
    #            print("이름:", data["name"])
    #            print("번호:", data["hp"])
    #            print("이메일:", data["email"]) 
    #            print("그룹:", data["groupa"]) 
    #            print("그룹2:", data["groupb"]) 
    #            print("생일:", data["birth"]) 
    #            print("직급:", data["grade"]) 
                            
    #            found = True

    #    if not found:
    #        print("검색 결과 없음")

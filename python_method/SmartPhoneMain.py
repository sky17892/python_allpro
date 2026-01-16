from SmartPhone import SearchPhone

class Ssss:

    def __init__(self):
        self.book = SearchPhone()

    def print_menu(self):
        print("\n====================") 
        print("1. 전화번호 전체등록") 
        print("2. 전화번호 등록(회사)")
        print("3. 전화번호 등록(거래처)")
        print("4. 전화번호 검색(회사)")
        print("5. 전화번호 검색(거래처)")
        print("6. 전화번호 모든 검색")
        print("7. 종료")

    def start(self):
        while True:
            self.print_menu()
            cho = input("원하는 작업을 고르세요: ")

            if cho == '1':
                self.book.InputAddr()

            elif cho == '2':
                self.book.CompanyAddr()

            elif cho == '3':
                self.book.CustomerAddr()

            elif cho == '4':
                self.book.SearchPhone()
            
            elif cho == '5':
                self.book.SearchPhone2()

            elif cho == '6':
                self.book.allPhone()

            elif cho == '7':
                print("프로그램 종료")
                break

            else:
                print("잘못된 입력입니다. 다시 선택하세욤!")

if __name__ == "__main__":
    Ssss().start()

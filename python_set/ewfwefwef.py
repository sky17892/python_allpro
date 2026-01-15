from wegwegegwegwegwegweg import SearchPhone

class Ssss:

    def __init__(self):
        self.book = SearchPhone()

    def print_menu(self):
        print("\n====================")
        print("1. 전화번호 등록")
        print("2. 전화번호 검색")
        print("3. 종료")

    def start(self):
        while True:
            self.print_menu()
            cho = input("원하는 작업을 고르세요! ")

            if cho == '1':
                self.book.inputAddr()

            elif cho == '2':
                self.book.searchPhone()

            elif cho == '3':
                print("프로그램 종료")
                break

            else:
                print("잘못된 입력입니다. 다시 선택하세욤!")

if __name__ == "__main__":
    Ssss().start()

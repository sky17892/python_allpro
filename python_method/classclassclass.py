from datetime import datetime
from typing import Optional

from dataclasses import dataclass

@dataclass
class Addr:
    id: int
    name: str
    hp: str
    email: str
    addr: str
    groupaaa: str
    groupbbb: str
    birth: str
    grade: str


    def print_input(self):
        print(f'아이다: {self.id}')
        print(f'이름: {self.name}')
        print(f'핸드폰: {self.hp}')
        print(f'이메일: {self.email}')
        print(f'주소: {self.addr}')
        print(f'그룹: {self.groupaaa}')
        print(f'그룹2: {self.groupbbb}')
        print(f'생일: {self.birth}')
        print(f'직급: {self.grade}')

addr = Addr("1", "엄태웅", "010-2323-3434", "sky12342@gmail.com", "대전광역시", "kg", "유지보수개발부", "19770505", "대리")
print(addr)



from datetime import datetime
from typing import Optional

from dataclasses import dataclass

@dataclass
class Addr:
    id: int
    name: str
    addr: str
    hp: str

    def print_input(self):
        print(f'아이다: {self.id}')
        print(f'이름: {self.name}')
        print(f'주소: {self.addr}')
        print(f'핸드폰: {self.hp}')

addr = Addr("1", "엄태웅", "부산광역시", "010-2323-3434")
print(addr)



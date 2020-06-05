from dataclasses import dataclass
from typing import List


@dataclass
class TInfo:
    phone: str = " "
    name: str = " "


@dataclass
class HashItem:
    info: TInfo
    empty: bool = True
    visit: bool = False


class MyHash:
    hash_table: List[HashItem]
    info: TInfo

    def __init__(self, size_table):
        self.size_table = size_table
        self.info = TInfo()
        self.hash_table = [HashItem(info=self.info) for _ in range(self.size_table)]
        self.size = 0
        self.step = 21

    def __hash_function(self, s):
        result = 0
        for i in range(len(s)):
            result += int(s[i]) * i
            result //= self.size_table
        return result

    def add_hash(self, name: str, phone: str):
        adr = -1
        if self.size < self.size_table:
            adr = self.__hash_function(phone)
            while not self.hash_table[adr].empty:
                adr = (adr + self.step) // self.size_table
            self.hash_table[adr].empty = False
            self.hash_table[adr].visit = True
            contact = TInfo(phone=phone, name=name)
            self.hash_table[adr].info = contact
            self.size += 1
        return adr

    def __clear_visit(self):
        for i in self.hash_table:
            i.visit = False

    def find_hash(self, phone: str):
        result = -1
        ok: bool
        count = 1
        self.__clear_visit()
        i = self.__hash_function(phone)
        ok = self.hash_table[i].info.phone == phone
        while not ok and not self.hash_table[i].visit:
            count += 1
            self.hash_table[i].visit = True
            i = (i + self.step) // self.size_table
            ok = self.hash_table[i].info.phone == phone
        if ok:
            result = i + 1
        return result

    def del_hash(self, phone: str):
        result = False
        i = 0
        if self.size != 0:
            i = self.__hash_function(phone)
            if self.hash_table[i].info.phone == phone:
                self.hash_table[i].empty = True
                self.hash_table[i].info.name = " "
                self.hash_table[i].info.phone = " "
                result = True
                self.size -= 1
            else:
                i = self.find_hash(phone)
                if i == -1:
                    self.hash_table[i].empty = True
                    self.hash_table[i].info.name = " "
                    self.hash_table[i].info.phone = " "
                    result = True
                    self.size -= 1
        return result

    def __str__(self):
        out = ""
        head = "{:<6}{:<20}{:<20}".format("N", "NAME", "PHONE")
        out += head
        out += "\n"
        for i in range(self.size_table):
            name: str = self.hash_table[i].info.name
            phone: str = self.hash_table[i].info.phone
            string = "{:<6}{:<20}{:<20}".format(i + 1, name, phone)
            out += string
            out += "\n"
        return out
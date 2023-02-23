# encoding:utf-8
# @Author :ZQY


# 自己做，easy
from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.account = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if 1 <= account1 <= len(self.account) and \
                1 <= account2 <= len(self.account) and \
                self.account[account1 - 1] >= money:
            self.account[account1-1] -= money
            self.account[account2-1] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if 1 <= account <= len(self.account):
            self.account[account-1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if 1 <= account <= len(self.account) and \
                self.account[account-1] >= money:
            self.account[account-1] -= money
            return True
        return False

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)

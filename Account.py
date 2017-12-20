from Block import *
from datetime import datetime
from collections import OrderedDict

class AccountBill(Block):
    def __init__(self, content, amount):
        t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = "{}|{}|{}".format(t, content, amount)
        return super(AccountBill, self).__init__(data)

    def get_amount(self):
        amount = 0
        if self.data:
            amount = int(self.data.split('|')[2])
        return amount

    def get_content(self):
        content = ''
        if self.data:
            content = self.data.split('|')[1]
        return content

    def __repr__(self):
        return 'Bill: {}>'.format(self.data)

class AccountBook(BlockChain):
    def __init__(self):
        self.head = None
        self.blocks = OrderedDict()

    def add_block(self, new_bill):
        new_bill.mine()
        super(AccountBook, self).add_block(new_bill)

    def balance(self):
        balance = 0
        if self.blocks:
            for k, v in self.blocks.items():
                balance += v['block'].get_amount()
        return balance

    def __repr__(self):
        num_existing_blocks = len(self.blocks)
        return 'AccountBook< {} Bills, Head: {} >'.format(num_existing_blocks, self.head, identifier if self.head else None)

from Account import *

book = AccountBook()
b1 = AccountBill('工资', 10000)
book.add_block(b1)

b2 = AccountBill('房租', -2500)
book.add_block(b2)

b3 = AccountBill('衣服', -1500)
book.add_block(b3)

b4 = AccountBill('吃饭', -1000)
book.add_block(b4)

b5 = AccountBill('股票收入', 200)
book.add_block(b5)

b6 = AccountBill('看电影', -200)
book.add_block(b6)

b7 = AccountBill('购物', -1000)
book.add_block(b7)

b8 = AccountBill('水电费等', -100)
book.add_block(b8)

balance = book.balance()
print(balance)

for k,v in book.blocks.items():
    print(v['block'].data)

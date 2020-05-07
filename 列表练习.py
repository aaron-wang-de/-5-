# Author:Aaron
# -*- coding = utf-8 -*-
# @Time: 5/7/20 5:11 AM
# @Author: aaron
# @Site: 
# @File: 列表练习.py
# @Software: PyCharm

"""
现有商品如下：
products = [["iphone", 6888], ["MacPro", 14800], ["小米6", 2499], ["Coffee", 31], ["Book", 60], ["Nike", 699]]
1. 打印出如下格式
---- 商品列表 ----
0 iphone 6888
1 MacPro 14800
2 小米6   2499
3 Coffee 31
4 Book   60
5 Nike   699

2. 根据上面的products列表写一个循环，不断询问用户想买什么，用户选择一个商品编号，就把对应的商品添加到购物车里，最终用户输入q退出时，打印购买的商品列表
"""




















products = [["iphone", 6888], ["MacPro", 14800], ["小米6", 2499], ["Coffee", 31], ["Book", 60], ["Nike", 699]]
print(products)
print("-"*8, "商品列表", "-"*8)
for i, product in enumerate(products):
    print("%d\t%s\t%d"%(i, product[0], product[1]))

cart = []
while True:
    item = input("请输入想要的商品名：")
    if item == "q":
        if len(cart)>0:
            print("您的购物清单如下")
            payment = 0
            cart_items = set(cart)
            for c in cart_items:
                pieces = cart.count(c)
                for product in products:
                    if c == product[0]:
                        price = product[1]
                print("%d个%s\t单价为%d\t总价为%d" % (pieces, c, price, price * pieces))
                payment = payment+ price*pieces
            print("您一共需要支付 %d元"%payment)
        else:
            print("请添加商品到购物车")
        break
    else:
        for product in products:
            if item in product[0]:
                cart.append(item)
            else:
                continue







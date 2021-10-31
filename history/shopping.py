money = int(input("钱数:"))
# 每个商品的信息用字典保存{"名称":"落籍鼠标","价格":60,"库存"：50}
products = [{"名称": "落籍鼠标", "价格": 60, "库存": 50}, {"名称": "落籍键盘", "价格": 160, "库存": 0},
            {"名称": "落籍鼠标垫", "价格": 10, "库存": 500}]
for s, i in enumerate(products):
    print(s, i["名称"], i["价格"], "元", i["库存"], "个")

seq = int(input("请输入要购买的商品编号"))
num = int(input("请输入要购买的商品数量"))
if num > products[seq]["库存"]:
    print("库存不足")
else:
    if products[seq]["价格"] * num > money:
        print("钱包不足")

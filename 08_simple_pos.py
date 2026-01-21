# โปรแกรม POS อย่างง่าย (Dictionary)

products = {
    "apple": 10,
    "banana": 5,
    "orange": 8,
    "milk": 20,
    "bread": 15
}

try:
    name = input("ชื่อสินค้า: ")
    print("ราคา =", products[name])
except KeyError:
    print("ไม่มีสินค้านี้")

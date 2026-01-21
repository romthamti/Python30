# คำนวณพื้นที่วงกลมหลายขนาด (while loop)

import math

while True:
    r = input("ป้อนรัศมี (หรือพิมพ์ exit): ")
    if r == "exit":
        break

    r = float(r)
    area = math.pi * r**2
    print("พื้นที่ =", area)

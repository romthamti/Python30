# คำนวณเงินเดือน + OT

salary = float(input("เงินเดือน: "))
ot = int(input("ชั่วโมง OT: "))

if ot > 20:
    salary += 500

print("เงินเดือนสุทธิ =", salary)

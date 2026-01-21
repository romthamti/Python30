# คำนวณดอกเบี้ยทบต้น

money = float(input("เงินต้น: "))
rate = float(input("อัตราดอกเบี้ย (%): ")) / 100
years = int(input("จำนวนปี: "))

for _ in range(years):
    money += money * rate

print("เงินสะสม =", money)

# คำนวณภาษีเงินได้

income = float(input("รายได้ต่อปี: "))

if income <= 150000:
    tax = 0
elif income <= 300000:
    tax = income * 0.05
else:
    tax = income * 0.10

print("ภาษี =", tax)

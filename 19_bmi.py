w = float(input("น้ำหนัก(กก.): "))
h = float(input("ส่วนสูง(ม.): "))

bmi = w / (h*h)
print("BMI =", bmi)

if bmi < 18.5:
    print("ผอม")
elif bmi < 25:
    print("ปกติ")
else:
    print("อ้วน")

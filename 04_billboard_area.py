# คำนวณพื้นที่ป้ายโฆษณาสามเหลี่ยม

base = float(input("ฐาน: "))
height = float(input("สูง: "))

area = 0.5 * base * height
print("พื้นที่ =", area)

if area > 50:
    print("ต้องเสียภาษีป้าย")

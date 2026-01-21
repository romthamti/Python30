# คำนวณพื้นที่สำนักงาน (Rectangle)
# ใช้ try-except ป้องกันการกรอกข้อมูลที่ไม่ใช่ตัวเลข

try:
    width = float(input("ป้อนความกว้าง: "))
    length = float(input("ป้อนความยาว: "))
    area = width * length
    print("พื้นที่สำนักงาน =", area)
except ValueError:
    print("กรุณากรอกตัวเลขเท่านั้น")

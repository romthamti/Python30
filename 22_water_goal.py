weight = float(input("ระบุน้ำหนักตัว: "))

water_ml = weight*33
water_liter = water_ml / 1000

print("ควรดื่มน้ำประมาณ {:.0f} มล. หรือ {:.2f} ลิตร/วัน".format(
    water_ml, water_liter
))

goal = float(input("ระบุจำนวนที่ดื่มไปแล้ววันนี้(มล): "))

if goal < water_ml:
    print("ดื้มน้ำยังไม่พอ")
elif goal <= water_ml +500:
    print("ยอดเยี่ยม")
else:
    print("ดื้มน้ำเยอะเกินไป")
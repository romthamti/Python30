# ระบบตรวจสอบที่ดิน 3 แปลง (List + For Loop)

lands = []

for i in range(3):
    w = float(input(f"ความกว้างแปลงที่ {i+1}: "))
    l = float(input(f"ความยาวแปลงที่ {i+1}: "))
    lands.append(w * l)

print("พื้นที่รวมทั้งหมด =", sum(lands))

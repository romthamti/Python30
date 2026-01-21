# สรุปยอดขายรายสัปดาห์

sales = []

for i in range(7):
    sales.append(float(input(f"ยอดขายวันที่ {i+1}: ")))

print("รวม =", sum(sales))
print("สูงสุด =", max(sales))

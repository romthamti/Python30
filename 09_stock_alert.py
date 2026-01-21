# ตรวจสอบสินค้าใกล้หมด (Array)

stocks = [3, 10, 2, 8, 4]

for i, s in enumerate(stocks):
    if s < 5:
        print(f"สินค้า {i} ใกล้หมด")

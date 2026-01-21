# คำนวณอายุหนี้
from datetime import date

due = date.fromisoformat(input("วันครบกำหนด (YYYY-MM-DD): "))
today = date.today()

print("ค้างชำระ", (today - due).days, "วัน")

from datetime import date, timedelta

today = date.today()
next_day = today + timedelta(days=180)
print("ตรวจครั้งถัดไป:", next_day)

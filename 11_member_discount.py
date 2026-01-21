# ระบบสมาชิก (match-case) Python 3.10+

member = input("ระดับสมาชิก (Gold/Silver/Bronze): ")

match member:
    case "Gold":
        print("ลด 20%")
    case "Silver":
        print("ลด 10%")
    case "Bronze":
        print("ลด 5%")
    case _:
        print("ไม่พบสมาชิก")

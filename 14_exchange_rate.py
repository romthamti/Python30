# เครื่องแลกเปลี่ยนเงินตรา (Tuple)

rates = (34.5, 37.2, 1.0)  # USD, EUR, THB
choice = int(input("เลือก 0=USD 1=EUR 2=THB: "))
money = float(input("จำนวนเงิน: "))

print("ได้ =", money * rates[choice])

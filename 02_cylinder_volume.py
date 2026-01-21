# คำนวณปริมาตรถังทรงกระบอก
import math

radius = float(input("รัศมีถัง: "))
height = float(input("ความสูงถัง: "))

volume = math.pi * radius**2 * height
print("ปริมาตรถัง = {:.2f}".format(volume))

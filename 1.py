#cau 1
name = input("Enter your name: ")
print(f"Hello, {name}!")

#cau 2
import math
bankinh = float(input("nhap duong kinh hinh tron: "))
chuvi = 2 * math.pi * bankinh
print("chu vi hinh tron la :", chuvi)

#cau 3
dai = float(input("nhap chieu dai: "))
rong = float(input("nhap chieu rong: "))

cv = 2 * (dai + rong)
dt = dai * rong

print("chu vi:", cv)
print("dien tich:", dt)

#cau 4
a = int(input("nhap so 1: "))
b = int(input("nhap so 2: "))
c = int(input("nhap so 3: "))

tong = a + b + c
tich = a * b * c
tb = tong / 3

print("tong:", tong)
print("tich:", tich)
print("trung binh cua 3 so:", tb)

#cau 5
talents = float(input("nhap talents: "))
pounds = float(input("nhap  pounds: "))
lots = float(input("nhap lots: "))
grams = (
    talents * 20 * 32 * 13.3 +
    pounds * 32 * 13.3 +
    lots * 13.3
)
kilograms = int(grams // 1000)
gram_con_lai = grams % 1000
print("The weight in modern units:")
print(f"{kilograms} kilograms and {gram_con_lai:.2f} grams")

#cau 6
import random
code_3 = [random.randint(0, 9) for _ in range(3)]
code_4 = [random.randint(1, 6) for _ in range(4)]
print("3-digit code:", code_3)
print("4-digit code:", code_4)

age = 10
Ad = "Rəşid"
tamAd = "Vəlizadə Ülvi"
print(tamAd, Ad, age, sep="\n")
a = float(input())
if a % 2 == 0:
    print("Cütdür")
elif a%2 != 0:
    print("Təkdir")

a = 2
b = 16
print(a**b, b**8)
import math
y = math.pi

print(y)
a = int(input())
b = int(input())

if a > 0:
    if a>b:
        print("a b den boyukdur")
    elif a == b:
        print("a b e beraberdir")
    else:
        print("a b den kiçikdir")
else:
    print("Salam olsun Ulviye")

a = 5
b = 2

if 3>4:
    print("5 4 den boyukdur")
if 6>2:
        print("6 2 den b")    


n = int(input())
s = 0
for i in range(1, n+1):
    s = s + i **2
print(s)
n = int(input())
i = 1 
s=0
while i <= n:
    s = s + i ** 2
    i = i+1
print(s)
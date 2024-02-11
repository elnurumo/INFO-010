# # 72 ci sual Minimum ədədin tapılması
# # Dövr açıq tipli suallar
# n = int(input())
# mini = 0  
# for i in range(1, n+1):
#     a = int(input())
#     if mini == 0:
#         mini = a
#         if mini > a:
#             mini = a
#     elif mini > a :
#         mini = a
# print(mini)

# # 73  cü sual max ədədin tapılması

# n = int(input())
# maxi = 0 
# for i in range(1, n+1):
#     a = int(input())
#     if maxi == 0:
#         maxi = a
#         if maxi < a:
#             maxi = a
#     elif maxi < a :
#         maxi = a
# print(maxi)

# a = [3,4,2,1,6,9,7,8,12,10,5,14]
# say = 0
# s = 0
# for i in range(0,len(a)):
#     if i % 2 == 0 and a[i]%2 != 0:
#         s = s+a[i]
#         say = say+1
#     if i%2 != 0 and a[i]%2 == 0:
#         s = s+a[i] 
#         say = say+1
# print(s,say)


# # 1 CI USUL
# s = 0
# k = 0
# # print(k,s)

# # # 2 CI USUL

# # s=k=0
# # print(k,s)

# n = int(input())
# s = 0
# a = 3
# k = 1
# while a<=n:
#     s = s + k*a
#     a = a + 2
#     k = -k
# print(s)

# 93 ci test
# n= int(input())
# m = str(n)
# # print(type(m))
# min = m[0]
# # print(min)
# for i in range (0, len(m)):
#     if int(min) >= int(m[i]) and int(m[i])%2 != 0:
#         min = int(m[i])
# if int(min)%2 != 0:
#     print(min)
# else:
#     print("Ədəddə tək rəqəm yoxdur")

# 95
# n = int(input())
# s = ''
# while n>=8:
#     q = n%8
#     q = str(q)
#     s = q + s
#     n = n // 8
# n = str(n)
# s = n + s
# print(s)

# 96

# m = int(input())
# for i in range(100, 1000):
#     a = i//100
#     b = i//10%10
#     c = i%10
#     if a!=1 and b!=1 and c!=1 and a*b*c == m:
#         print(i)

# 94 cü test
# def hex_to_decimal(hexadecimal):
#     return int(hexadecimal, base=16)

# n = input("Giriş (16-lıq say sistemində): ")
# decimal_output = hex_to_decimal(n)
# print("Çıxış (10-luq say sistemində):", decimal_output)

# Sətirlər və onlar üzərində
# 9-cu sual
# a = [1993,27,9,2,0,2,0,5,6,11]
# b = a
# a.append(44)
# b.remove(6)
# del a[0]
# a.insert(6,10)
# del b[7]
# print(a,b)

# 10-cu sual
# def f(n):
#     s = ''
#     while n>0:
#         k=n%8
#         s= str(k)+s
#         n=n//8
#     return s
# n=int(input())
# s = f(n)
# print(n,s)

# 11-ci sual


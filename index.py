# 72 ci sual Minimum ədədin tapılması
# Dövr açıq tipli suallar
n = int(input())
mini = 0  
for i in range(1, n+1):
    a = int(input())
    if mini == 0:
        mini = a
        if mini > a:
            mini = a
    elif mini > a :
        mini = a
print(mini)

# 73  cü sual max ədədin tapılması

n = int(input())
maxi = 0 
for i in range(1, n+1):
    a = int(input())
    if maxi == 0:
        maxi = a
        if maxi < a:
            maxi = a
    elif maxi < a :
        maxi = a
print(maxi)
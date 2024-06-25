print("Введите пятизначное число:")
x = int(input())
ed = x % 10
des = x // 10 % 10
sot = x // 100 % 10
t = x // 1000 % 10
dt = x // 10000

print("Решение:", des ** ed * sot / (dt - t))
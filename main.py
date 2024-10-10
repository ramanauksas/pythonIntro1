# Uzduotis 1
print(8*4+2)
print(8*(4+2))
print(48/4)
print(3+6*2)

# Uzduotis 2
x = 2
y = 3
z = x + y
print(x, y, z)

# Uzduotis 3
x = 10
y = 2
print (f"{x}+{y}={x+y}")
print (f"{x}-{y}={x-y}")
print (f"{x}*{y}={x*y}")
print (f"{x}/{y}={x/y}")

# Uzduotis 4
x = 7
print(f"x: {x} -> {x+5}")

y = 2
print(f"y: {y} -> {y*2}")

# Uzduotis 1.
x = 2
y = 3
z = 4
print(f"Pirmas ir antras skaiciai lygus: {x==y}")
print(f"Antras ir trecias skaiciai lygus: {y==z}")
print(f"x>y : {x>y}")
print(f"y>2*z: {x>2*z}")
print(f"x%2==0 {x%2==0}")
print(f"y%2!=0 {y%2!=0}")
print(f"z>0 {z>0}")
print(f"x<0 {x<0}")
print(f"y%4==0 {y%4==0}")
print(f"z%4==0 {y%8==0}")

# Uzduotis 2.
age = 23
if age>18:
    print("Jus galite balsuoti")

# Uzduotis 3.
x = 2
y = 3
z = 5
mean = (x + y + z) / 3
if mean > 0:
    print("vidurkis teigiamas")


# Uzduotis 4.
x = 10
if x % 5 == 0:
    print(x*1, x*2, x*3, x*4, x*5)
if x % 2 == 0:
    print(x**2/2)
if x % 7 != 0:
    y = 3
    print(x+y, x-y, x*y, x/y)


# Uzduotis 5.
x = 2
y = 3
z = 5
if x>y:
    print("x>y")
elif y>z:
    print("y>z")
else:
    print("z>x")

# Uzduotis 6.
x = 2
y = 3
z = 5
if x==y:
    print("x=y")
elif y==z:
    print("y=z")
elif x==0:
    print("x=0")
elif y<0:
    print("y<0")
elif z>0:
    print("z>0")

# Uzduotis 7.
x = 7
if x==10:
    print("puiku")
elif x>=9:
    print("labai gerai")
elif x>7:
    print("gerai")
elif x>5:
    print("patenkinamai")
else:
    print("egzaminas neislaikytas")


# Uzduotis 7:
x = 10
if x%2==0:
    print("skaicius lyginis")
else:
    print("skaicius nelyginis")

# Uzduotis 8:
if x%7==0:
    print("skaicius dalijasi is 7")
else:
    print("skaicius nesidalija is 7")

# Uzduotis 9:
x = "kelias/iki/failo/main.pt"
if x.endswith(".py"):
    print("failas yra .py tipo")
else:
    print("failas nera .py tipo")


# Uzduotis 10
x = 15

if x%2==0:
    print("skaicius yra lyginis")
elif x%5==0:
    print("skaicius dalijasi is 5")
elif x%3==0:
    print("skaicius dalijasi is 3")
else:
    print("klaida")

# Uzduotis 11
x = 12
y = 14
z = 14
if x == y:
    print("pirmi skaiciai lygus")
elif x == z:
    print("primas ir trecias skaiciai lygus")
elif z < x:
    print("trecias skaicius didesnis uz pirma")
elif y==2*z:
    print("antras skaicius dvigubai didesnis uz trecia")
elif x%3==0:
    print("pirmas skaicius dalijasi is 3")
else:
    print("klaida")



# Uzduotis 12
x = 10
y = 12
z = 15

if x >= y and x>= z:
    print("didziausias skaicius yra ", x)
elif y>=z:
    print("didziausias skaicius yra", y)
else:
    print("didziausias skaicius yra", z)


# Uzduotis 13
x = 10
y = 12
z = 15

if x <= y and x<= z:
    print("maziausias skaicius yra ", x)
elif y<=z:
    print("maziausias skaicius yra", y)
else:
    print("maziausias skaicius yra", z)

# # Uzduotis 14
# num1 = input("Iveskite pirma egzamino ivertinima")
# num1 = int(num1)
# num2 = input("Iveskite antra egzamino ivertinima")
# num2 = int(num2)
# num3 = input("Iveskite trecia egzamino ivertinima")
# num3 = int(num3)
#
# avg = (num1 + num2 + num3) / 3
# if 8 <= avg and avg <=10:
#     print("vidurkis yra intervale [8;10]")
# elif avg >= 5:
#     print("vidurkis yra intervale [5, 8)")
# else:
#     print("vidurkis yra maziau nei 5")

#  Uzduotis 15
x = 10
y = 12
if x>y or x==0:
    print("Pirma salyga patenkinta")
if y>x or y==5:
    print("Antra salyga patenkinta")
if x>y and x==2:
    print("Trecia salyga patenkinta")
if y>x and x<100:
    print("Ketvirta salyga patenkinta")


# # Uzduotis 1.
# vardas = input("Iveskite savo varda")
# amzius = input("Iveskite savo amziu")
# kodel = input("Kodel pasirinkote programavima")
#
# print(f"{vardas} (amzius {amzius} m.) pasirinko programavima, nes {kodel}")

# # Uzduotis 2
# s = input("Iveskite simboli")
# print(s, s, s, s, s)
# print(s, s, s, s, s)
# print(s, s, s, s, s)
# print(s, s, s, s, s)
# print(s, s, s, s, s)

# #Uzduotis 3
# s = input("Iveskite simboli")
# print(s)
# print(s, s)
# print(s, s, s)
# print(s, s, s, s)


# # Uzduotis 4
# vardas = input("Iveskite varda")
# amzius = input("Iveskite amziu")
# amzius = int(amzius)
# ugis = input("Iveskite ugi, metrais")
# ugis = float(ugis)
#
# print(vardas, type(vardas))
# print(amzius, type(amzius))
# print(ugis, type(ugis))

# # Uzduotis 5
# p1 = input("Iveskite pazymi")
# p2 = input("Iveskite pazymi")
# p3 = input("Iveskite pazymi")
# p4 = input("Iveskite pazymi")
# p5 = input("Iveskite pazymi")
#
# print("Jusu pazymiu vidurkis yra: ",  (int(p1)+int(p2)+int(p3)+int(p4)+int(p5))/5)


# # uzduotis 6
# length = input("Iveskite metrus")
# length = float(length)
# print(f"ilgis centimetrais: {length * 100} \n ilgis milimetrais: {length * 1000} \n ilgis kilometrais: {length / 1000}")


# # uzduotis 7
# num1 = input("Iveskite pirma skaiciu")
# num1 = float(num1)
# num2 = input("Iveskite antra skaiciu")
# num2 = float(num2)
# print(f"Suma: {num1+num2} \n Skirtumas: {num1-num2} \n Sandauga: {num1*num2} \n Dalmuo: {num1/num2}")

# # uzduotis 8
# num1 = input("Iveskite pirma skaiciu")
# num1 = float(num1)
# num2 = input("Iveskite antra skaiciu")
# num2 = float(num2)
# print(f"Liekana: {num1%num2}")

# # uzduotis 9
# num1 = input("Iveskite pirma skaiciu")
# num1 = float(num1)
# num2 = input("Iveskite antra skaiciu")
# num2 = float(num2)
# print("num1**num2 = ", num1**num2 )

# 7 skyriaus uzduotis
work_hours = 8
loafs_per_hour_per_worker = 10
num_workers = 20
loaf_cost = 2
loaf_price = 3
num_orders = 300




# 1
output_per_day = work_hours * num_workers * loafs_per_hour_per_worker
print("Kepykla per diena iskepa: ", output_per_day)

# git config --global user.email "tomas_ramanauskas@yahoo.com"
# git config --global user.name "ramanauksas"

print("nauja versija")



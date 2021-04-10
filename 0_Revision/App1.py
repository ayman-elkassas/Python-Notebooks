# import calendar
# print(calendar.calendar(2016,w=1,m=2))
# for i in range(10,1,-1):
#     print(i)
for i in range(3):
    print("fill data of student :",i+1)
    subtotal=0
    for j in range(4):
        deg=int(input("plz input degree "))
        subtotal=subtotal+deg
    print("student {} sub total is {}".format(i+1,subtotal))


a=int(input("enter a year"))
if a%4==0 and a%100!=0:
    print("leap year")
if a%400==0:
    print(" century leap year")
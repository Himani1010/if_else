age=int(input("enter a number "))
sex=input("enter a male and female sex ")
if sex=='female' and age>=20 and age<=60:
    print("urban areas only")
if sex=='male' and age>=20 and age<=40:
    print("work in aanywhere")
if sex=='male' and age>=40 and age<=60:
    print("urban areas only")
else:
    print("Error")
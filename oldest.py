a=int(input("enter a year"))
b=int(input("enter a year"))
c=int(input("enter a year"))
if a>b and a>c:
    print(a,"oldest hai")
if b>a and b>c:
    print(b,"oldest hai")
if c>a and c>b:
    print(c,"oldest hai")
if a<b and a<c:
    print(a,"youngest")
if b<a and b<c:
    print(b,"youngest")
if c<a and c<b:
    print(c,"youngest")
s=input("enter a password:")
if len(s)>=6 and len(s)<=12:
    if "@" or "#" in s:
        if "0" or "" or  in s:
             if "A" or "Z" in s:
                 if "a" or "z" in s:
                     print("strong password")
                 else:
                     print("weak password")
             else:
                 print("week password")
        else:
            print("wrong password")
    else:
        print("wrong")
else:
     print("your lenth is not perfect")
     
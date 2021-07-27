expected_date=int(input("enter the date"))
expected_month=int(input("enter the month"))
expected_year=int(input("enter the year"))
return_date=int(input("enter the date"))
return_month=int(input("enter the month"))
return_year=int(input("enter the year"))
if return_year==expected_year:
    if return_month==expected_month:
        if return_date<=expected_date:
            print("no fine")
        elif return_date>expected_date:
            print(15*(return_date-expected_date))
    elif return_month>expected_month:
        print(500*30*(return_month-expected_month))
else:
    print("10000")



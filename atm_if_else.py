print("welcome")
print("insert atm card")
language=input("write english ya hindi:")
if language=="english":
    transaction_type=input("enter a transaction_type:")
    if transaction_type=="csah_withdrawal":
        account_type=input("enter a account_type:")
        if bank_type=="saving":
            print("saving")
            amount=int(input("enter a amount:"))
            if amount>=500 or amount<=20000:
                pin=int(input("enter a number:"))
                if pin==1010:
                    print("your transaction is being process please wait:")
                    print("please collect your card:")
                    display=input("do you display your balance:")
                    if display=="yes":
                        total_amount=50000
                        print(total_amount-amount)
                        print("last transaction is cancle")
                    else:
                        print("no")  
                else:
                    print("wrong pin")
            else:
                print("last cancle try again")
        else:
            print("current")
    elif transaction_type=="blance inq":
        available_amount=50000
        account_type=input("enter a account_type:")
        if account_type=="saving":
            print("your amount is", available_amount)
        else:
            print("ERROR")
    elif transaction_type=="pin_change":
        print("pin_change")
        old_pin=1010
        account_type=input("enter a account_type:")
        if bank_type=="saving":
            pin=int(input("enter old_pin:"))
            if pin==old_pin:
                new_pin=int(input("enter a new_pin:"))
                if new_pin>=0 or new_pin<=9 and len(new_pin)>=4 or len(new-pin)<=6:
                    print("your new pin is saved please don't share with others")
                else:
                    print("print is not valid")
            else:
                print("old pin is invalid please try again")
        else:
            print("error")
else:
    print("another language")
        
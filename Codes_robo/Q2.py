def credit_card(Num):
    Num=Num[len(Num)-4:]
    return Num
Num=input("Enter the credit card number")
print(credit_card(Num))
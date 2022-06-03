str=input("Enter the string")
sum_of_integers=0;
for i in range(len(str)):
    if ord(str[i])>=ord("0") and ord(str[i])<=ord("9"):
                sum_of_integers=sum_of_integers+int(str[i])
    else :
        continue
print(sum_of_integers)
def str(s):
    n=len(s)
    new_string=" "
    for i in range(n):
        new_string  =new_string + (s[i]*2)
    return new_string

s1=input("enter the string=")
print(str(s1))
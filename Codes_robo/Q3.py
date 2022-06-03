def function(x,y,operator):
    if operator=="+":
        return x+y
    elif operator=="-":
        return x-y
    elif operator=="/":
        return x/y
    elif operator==".":
        return x*y
x=int(input("Enter the first number="))
y=int(input("Enter the second number="))
operator=input("Enter which operation you want to do=")
print(function(x,y,operator))
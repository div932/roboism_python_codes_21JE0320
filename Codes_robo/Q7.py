def modulo(str):
    freq = 0
    max = 0
    for i in str:
        c = str.count(i)
        if c>freq:
            freq=c
            max = i
    print(max)
str=[1,5,28,39,3,4,7,1,2,2,2,2,2]
modulo(str)
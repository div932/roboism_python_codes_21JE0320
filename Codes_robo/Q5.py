import random
def duplicate(list):
    for i in list:
        if((list.count(list[i]))>1):
            return (list[i])
randomlist=[]
for x in range(1,99):
      n=random.randint(1,99)
      randomlist.append(n)
print("the element which is duplicate is",duplicate(randomlist))
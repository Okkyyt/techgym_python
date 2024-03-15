import random

def makeNum():
    num_list = []
    for i in range(18):
        num_list.append(str(i+1))
    return num_list

def num():
    num = makeNum()
    result = []
    for i in range(4):
        a = random.choice(num)
        result.append(a)
        num.remove(a)
    
    print(result)

num()
print(1.2*3)

import random

def make():
    a = random.randint(1,19)
    return a

def check(result,a):
    for i in result:
        if i == str(a):
            return  False
    return True

def num():
    result =[]
    while len(result)<4:
        a = make()
        if check(result,a) == True:
            result.append(str(a))

    return result
    
print(num())
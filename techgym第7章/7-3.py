import random

level = 1
col=[num for num in range(3,10) for i in range(2)]
raw=[num for num in range(3,10) for i in range(2)]
del col[0]
del raw[13]
print(col)
print(raw)
data=[['見','貝'],['土','士'],['眠','眼']]
number_data=['A','B','C','D','E','F','G','H','I']
dictionary={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8}

def start_message():
    print('違う漢字の番号(例:A1)を入力してください')

def section_message():
    print('レベル:{}'.format(level))

def mistake_massege():
    print('デバッグ:mistake_number={}'.format(mistake_number))
    return mistake_number

def abc():
   col_data=''
   x=0
   for a in range(col[level-1]):
      col_data+=' '+number_data[x]
      x+=1
   print('／ |{}'.format(col_data))

def underber():
   ber=''
   for a in range(col[level-1]):
      ber+='ー'
   print('ーー'+ber)

def view_question():
    a=random.randint(0,2)
    print(data[a])
    abc()
    underber()
    new_list=data[a]
    number=1
    miss_space=0
    line_number=1
    while number<=raw[level-1]:
        count=1
        word=''
        line=str(line_number)+' ❘ '
        while count<=col[level-1]:
            if miss_space == mistake_number:
             word+=new_list[1]
            else:
             word+=new_list[0]
            count+=1
            miss_space+=1
        print(line+word)
        number+=1
        line_number+=1

def change_input_number(input_str):
   input_count=dictionary[input_str[0]]+(int(input_str[1])-1)*col[level-1]
   print('デバッグ:input_number={}'.format(input_count))
   return input_count

def is_correct_number(input_number,mistake_number):
   if input_number == mistake_number:
      return True
   else:
      return False
   
def view_result(is_correct):
   if is_correct == True:
      print('正解！')
   else:
      print('不正解')

def change_string(number):
    top = number_data[number%col[level-1]]
    import math
    print('正解は{}{}'.format(top,math.floor(number/col[level-1])+1))

def level_up():
    global level
    level += 1
    if  level < 13:
       play()
   
def play():
    global mistake_number
    mistake_number=random.randint(0,col[level-1]*raw[level-1])

    section_message()
    mistake_number=mistake_massege()
    view_question()
    choice = input('(例:A1)')
    print('デバッグ:choice = {}'.format(choice))
    input_str=list(choice)
    input_number=change_input_number(input_str)
    is_correct=is_correct_number(input_number,mistake_number)
    view_result(is_correct)
    number=mistake_number
    if is_correct == False:
        change_string(number)
    if is_correct == True:
       level_up()

start_message()
play()
import random

level=1
col=5
row=4
data=[['見','貝'],['土','士'],['眠','眼']]
mistake_number=random.randint(0,col*row-1)
dictionary={'A':0,'B':1,'C':2}

def start_message():
    print('違う漢字の番号(例:A1)を入力してください')

def section_message():
    print('レベル:'+str(level))

def mistake_massege():
    print('デバッグ:mistake_number='+str(mistake_number))
    return mistake_number

def abc():
   print('／ | A B C')

def underber():
   print('ーーーーー')

def view_question():
    a=random.randint(0,2)
    print(data[a])
    abc()
    underber()
    new_list=data[a]
    number=1
    miss_space=0
    line_number=1
    while number<=row:
        count=1
        word=''
        line=str(line_number)+' ❘ '
        while count<=col:
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
   input_count=dictionary[input_str[0]]+(int(input_str[1])-1)*3
   print('デバッグ:input_number='+str(input_count))
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
    if number%col ==0:
      top='A'
    elif number%col ==1:
      top='B'
    else:
      top='C'
    
    import math
    print('正解は'+top+str(math.floor(number/col)+1))
   
def play():
    section_message()
    mistake_number=mistake_massege()
    view_question()
    choice = input('(例:A1)')
    print('デバッグ:choice = ' + choice)
    input_str=list(choice)
    input_number=change_input_number(input_str)
    is_correct=is_correct_number(input_number,mistake_number)
    view_result(is_correct)
    number=mistake_number
    if is_correct == False:
        change_string(number)


start_message()
play()
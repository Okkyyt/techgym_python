import random

dictionary={'A':0,'B':1,'C':2}
mistake_number=random.randint(0,8)
data=[['見','貝'],['土','士'],['眠','眼']]
level=1


def start_message():
    print('違う漢字の番号(例:A1)を入力してください')

def section_message():
    print('レベル:'+str(level))

def mistake_massege():
    print('デバッグ:mistake_number='+str(mistake_number))

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
    while number<=3:
        count=1
        word=''
        line=str(line_number)+' ❘ '
        while count<=3:
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
   

def play():
    section_message()
    mistake_massege()
    view_question()
    choice = input('(例:A1)')
    print('デバッグ:choice = ' + choice)
    input_str=list(choice)
    change_input_number(input_str)

start_message()
play()
import random

data=[['見','貝'],['土','士'],['眠','眼']]
level=1

def start_message():
    print('違う漢字の番号(例:A1)を入力してください')

def section_message():
    print('レベル:'+str(level))

def view_question():
    a=random.randint(0,2)
    print(data[a])
    new_list=data[a]
    number=1
    while number<=3:
        count=1
        word=''
        while count<=3:
            word+=new_list[0]
            count+=1
        print(word)
        number+=1

def play():
    section_message()
    view_question()
    choice = input('(例:A1)')
    print('デバッグ:choice = ' + choice)

start_message()
play()
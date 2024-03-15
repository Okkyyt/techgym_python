import random

def start_massage():
    print('じゃんけんスタート')

def get_my_hand():
    print('自分の手を入力してください')
    my_hand = int(input('0:グー, 1:チョキ, 2:パー'))
    return my_hand

def get_you_hand():
    you_hand = random.randint(0, 2)
    return you_hand

def view_result(hand_diff):
    if    hand_diff == 0:
      print('あいこ')
    elif   hand_diff == -1 or hand_diff == 2:
      print('勝ち')
    else:
      print('負け')
    



start_massage()
my_hand=get_my_hand()
you_hand=get_you_hand()
hand_diff = my_hand-you_hand
view_result(hand_diff)
    


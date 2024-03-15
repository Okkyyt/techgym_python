import requests
import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np
import random

card_images = []

def load_image():
  image_name = 'cards.jpg'
  vsplit_number = 4
  hsplit_number = 13
  
  if not os.path.isfile(image_name):
    response = requests.get('https://raw.githubusercontent.com/techgymjp/techgym_python/master/cards.jpg', allow_redirects=False)
    with open(image_name, 'wb') as image:
      image.write(response.content)
   
  img = cv.imread('./'+image_name)
  img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
 
  h, w = img.shape[:2]
  crop_img = img[:h // vsplit_number * vsplit_number, :w // hsplit_number * hsplit_number]
  
  card_images.clear()
  for h_image in np.vsplit(crop_img, vsplit_number):
    for v_image in np.hsplit(h_image, hsplit_number):
      card_images.append(v_image)

class Card:
  def __init__(self,mark,display_name,number,image,flag):
    self.mark = mark
    self.display_name = display_name
    self.number = number
    self.image = image
    self.flag = flag

class Player:
   def __init__(self,name,cards,total_number):
      self.name = name
      self.cards = cards
      self.total_number = total_number

class Human(Player):
    def __init__(self,name,cards,total_number,coin,bet):
        self.coin = coin
        self.bet = bet
        super().__init__(name,cards,total_number)
    
    def show_coin(self):
        print(f"現在の持ちコインは{self.coin}です")

    def set_bet_coin(self):
       self.bet = 100
       self.coin -= self.bet
       
    def add_coin(self):
       self.coin += (self.bet)*2

class Computer(Player):
   def __init__(self,name,cards,total_number):
      super().__init__(name,cards,total_number)

def create_cards():
    global cards
    cards = []
    marks = ['ハート','スペード','ダイヤ','クローバー']
    display_name = ['A']
    for i in range(2,11):
        display_name.append(i)
    display_name += ['J','Q','K']

    card_count = 0
    for i  in marks:
        for j , num in enumerate(display_name):
            if j == 0:
                j = 10
            elif j >= 9:
                j = 9
            cards.append(Card(i,num,j+1,card_images[card_count],0))
            card_count += 1

def deal_card(player):
    random_card = cards[random.randint(0,51)]
    while random_card.flag == 1:
      random_card = cards[random.randint(0,51)]
    player.cards.append(random_card)
    player.total_number += random_card.number
    random_card.flag = 1
    calc_ace(player)

def choice():
    while True:
        choice_number = input("ヒット[1] or スタンド[2]")
        if choice_number.isdigit():
            if int(choice_number) == 1 or int(choice_number) == 2:
                return int(choice_number)
            
def play_once():
    check = choice()
    if check == 1:
      hit()
      return True
    return False

def hit():
   deal_card(Human)
   

def is_blackjack(total_number):
    if total_number >= 21:
      return True
    return False

def win():
   print("あなたの勝ち")

def lose():
   print("コンピューターの勝ち")

def is_burst(player):
   if  player.total_number >= 22:
      return True
   else:
      return False

def show_cards(playerCards):
  for i,card in enumerate(playerCards):
    plt.subplot(1,6,i+1)
    plt.axis("off")
    plt.imshow(playerCards[i].image)
    print(f"{Human.cards[i].mark}{Human.cards[i].display_name}")
  plt.show()


def stand():
   deal_card(Computer)


def judge():
   
   if is_burst(Human)and is_burst(Computer)==False:
      return "lose"
   elif is_burst(Human)==False and is_burst(Computer):
      return "win"
   elif is_burst(Human) and is_burst(Computer):
      return "draw"

   if Human.total_number > Computer.total_number:
      return "win"
   elif Computer.total_number > Human.total_number:
      return "lose"
   else:
      return "draw"

def show_result(result):
    for i,card in enumerate(Human.cards):
        plt.subplot(2,8,i+1)
        plt.axis("off")
        plt.imshow(card.image)
        print(f"あなたのカードは{card.mark}{card.display_name}")

    for i, card in enumerate(Computer.cards):
        plt.subplot(2,8,i+9)
        plt.axis("off")
        plt.imshow(card.image)
        print(f"コンピューターのカードは{card.mark}{card.display_name}")

    plt.show()

    if result == "win":
       win()
       Human.add_coin(Human)
    elif result == "lose":
       lose()
    else:
       print("引き分け")

def calc_ace(player):
   for i in player.cards:
      if i.display_name == "A" and i.number == 11 and player.total_number >= 22:
         i.number = 1
         player.total_number -= 10

def initialize():
   Human.cards = []
   Computer.cards = []
   Human.total_number = 0
   Computer.total_number = 0
   

def play():
  load_image()
  create_cards()
  global players
  Human.name = '自分'
  Computer.name = 'コンピューター'
  players = [Human.name,Computer.name]
  Human.cards = []
  Computer.cards = []
  Human.total_number = 0
  Computer.total_number = 0
  Human.coin = 500
  Human.show_coin(Human)
  Human.set_bet_coin(Human)
  deal_card(Human)
  deal_card(Human)
  deal_card(Computer)
  show_cards(Human.cards)
  num_check = is_blackjack(Human.total_number)
  check_hit = True
  while num_check == False and check_hit == True:
    check_hit = play_once()
    if check_hit:
      show_cards(Human.cards)
    num_check = is_blackjack(Human.total_number)
  while Computer.total_number < 17:
     stand()
  result = judge()
  show_result(result)
  Human.show_coin(Human)
  while Human.coin > 0:
     initialize()
     Human.set_bet_coin(Human)
     deal_card(Human)
     deal_card(Human)
     deal_card(Computer)
     show_cards(Human.cards)
     num_check = is_blackjack(Human.total_number)
     check_hit = True
     while num_check == False and check_hit == True:
        check_hit = play_once()
        if check_hit:
         show_cards(Human.cards)
         num_check = is_blackjack(Human.total_number)
     while Computer.total_number < 17:
         stand()
     result = judge()
     show_result(result)
     Human.show_coin(Human)

play()
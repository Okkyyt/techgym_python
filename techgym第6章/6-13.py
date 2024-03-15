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
    response = requests.get('http://3156.bz/techgym/cards.jpg', allow_redirects=False)
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
   def __init__(self,name,cards,total_number):
        super().__init__(name,cards,total_number)

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

def is_blackjack(total_number):
    if total_number >= 21:
      return True
    return False

def hit():
   deal_card(Human)
   
def win(total_number):
   if total_number == 21:
      print("勝ち")

def lose():
   print("負け")

def is_burst(total_number):
   if  total_number >= 22:
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
  win(Human.total_number)
  if is_burst(Human.total_number):
     lose()

play()
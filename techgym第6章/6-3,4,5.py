import requests
import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

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
  def __init__(self,mark,display_name,number,image):
    self.mark = mark
    self.display_name = display_name
    self.number = number
    self.image = image

class Player:
   def __init__(self,name,cards,total_number):
      self.name = name
      self.cards = cards
      self.total_number = total_number

class Human(Player):
   def __init__(self,name,cards,total_number):
      super().__init__(name,cards,total_number)
      name = '自分'

class Computer(Player):
   def __init__(self,name,cards,total_number):
      super().__init__(name,cards,total_number)
      name = 'コンピューター'

def create_cards():
    global cards
    cards = []
    marks = ['ハート','スペード','ダイヤ','クローバー']
    display_name = ['A']
    for i in range(2,11):
        display_name.append(i)
    display_name += ['J','Q','K']

    for i  in marks:
        for j , num in enumerate(display_name):
            if j == 0:
                j = 10
            if j >= 9:
                j = 9
            cards.append(Card(i,num,j+1,card_images[j]))

def play():
  load_image()
  show_test()

def show_test():
  create_cards()
  plt.subplot(1,6,1)
  plt.axis("off")
  plt.imshow(card_images[20])
  plt.subplot(1,6,2)
  plt.axis("off")
  plt.imshow(card_images[33])
  plt.show()

play()
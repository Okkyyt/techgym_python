import random

class Player:
  def __init__(self, name, coin):
    self.name = name
    self.coin = coin


class Human(Player):
  def __init__(self, name, coin):
    super().__init__(name, coin)

def play():
  global players
  player1 = Human('MY',500)
  players = [player1]
  print('デバッグログ：play()')
  

play()
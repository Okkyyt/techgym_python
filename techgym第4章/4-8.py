import random

class Player:
  def __init__(self, name, coin):
    self.name = name
    self.coin = coin

  def info(self):
    print (self.name + ':' + str(self.coin))

  def set_bet_coin(self,bet_coin):
    self.coin -= int(bet_coin)



class Human(Player):
  def __init__(self, name, coin):
    super().__init__(name, coin)

  def bet(self):
    bet_coin = input('何枚BETしますか？:(1~99)')
    while not self.eneable_bet_coin(bet_coin) :
        bet_coin = input('何枚BETしますか？:(1~99)')

    print(str(bet_coin))
  
    super().set_bet_coin(bet_coin)

  def eneable_bet_coin(self,string):
    if string.isdigit() == True:
      if int(string) >= 1 and int(string) <= 99 :
        return True
      else:
        return False
    else:
        return False

def play():
  global players
  player1 = Human('MY',500)
  players = [player1]
  print('デバッグログ：play()')
  Player.info(players[0])
  Human.bet(players[0])
  Player.info(players[0])
play()
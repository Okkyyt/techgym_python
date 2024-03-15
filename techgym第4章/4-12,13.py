import random
players = []

class Player:
  def __init__(self, name, coin):
    self.name = name
    self.coin = coin

  def info(self):
    print (self.name + ':' + str(self.coin))

  def set_bet_coin(self,bet_coin):
    self.coin -= int(bet_coin)
    print(str(self.name) + 'は' + str(bet_coin) + 'コインBETしました。')


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
    
class Computer(Player):
  def __init__(self, name, coin):
    super().__init__(name, coin)

  def bet(self):
    if self.coin < 99:
      bet_coin = random.randint(1,self.coin)
    else:
      bet_coin = random.randint(1,99)
    
    super().set_bet_coin(bet_coin)


def create_players():
  global players
  player1 = Human('MY',500)
  player2 = Computer('C1',500)
  player3 = Computer('C2',500)
  player4 = Computer('C3',500)
  players = [player1,player2,player3,player4]

def show_players():
  for i in players:
    i.info()
  for i in players:
    i.bet()
  for i in players:
    i.info()
     
def play():
  create_players()
  print('デバッグログ：play()')
  show_players()
play()
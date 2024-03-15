import random

class Team:
  def __init__(self, name,attack,defense):
    self.name = name
    self.attack=attack
    self.defense=defense

  def info(self):
     print(self.name+':'+'攻撃力:'+str(self.attack)+'/'+'守備力:'+str(self.defense))

def create_teams():
  global teams
  team1=Team('アタッカーズ',80,20)
  team2=Team('ディフェンダーズ',30,70)
  team3=Team('アベレージズ',50,50)
  teams=[team1,team2,team3]

def show_teams():
  team_number=1
  for i in range(3):
    print(str(team_number))
    Team.info(teams[team_number-1])
    team_number += 1

def play():
  print('デバッグログ：play()')
  create_teams()
  show_teams()
  
play()

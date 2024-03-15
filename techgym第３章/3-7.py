import random
import math

class Team:
  def __init__(self, name,attack,defense):
    self.name = name
    self.attack=attack
    self.defense=defense

  def info(self):
     print(self.name+':'+'攻撃力:'+str(self.attack)+'/'+'守備力:'+str(self.defense))

  def get_hit_rate(self):
    return random.randint(10,self.attack)
  
  def get_out_rate(self):
    return random.randint(10,self.defense)
    

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

def choice_team (player):
    global playing_teams
    if player == 1:
     player_name ='自分'
    else:
        player_name='相手'

    player_ch = int(input(player_name+'のチームを選択してください(1~3)'))-1
    print(player_name+'のチームは「'+(teams[player_ch].name)+'」です')
    playing_teams={1:False,2:False}
    return teams[player_ch]
  
def get_play_inning(inning,myself,enemy):
  if inning == 'front':
    a_score=int(Team.get_hit_rate(myself)) - int(Team.get_out_rate(enemy))
    score=math.floor(a_score/10)
    if score<0:
     return 0
    else:
     return score

  else:
    b_score = int(Team.get_hit_rate(enemy)) - int(Team.get_out_rate(myself))
    score=math.floor(b_score/10)
    if score<0:
     return 0
    else:
     return score
    


def play():
  print('全チームの情報')
  create_teams()
  show_teams()
  myself=choice_team (1)
  enemy=choice_team (2)
  for i in range(9):
    i += 1
    inning = 'front'
    print('デバッグログ：'+str(i)+'回表'+str(get_play_inning(inning,myself,enemy)))
    inning = 'back'
    print('デバッグログ：'+str(i)+'回裏'+str(get_play_inning(inning,myself,enemy)))
  
play()

import random
import math

playing_teams={"myself":False,"enemy":False}

class Team:
  def __init__(self, name,attack,defense):
    self.name = name
    self.attack=attack
    self.defense=defense
    self.total_score = 0

  def info(self):
     print('{}:攻撃力:{}/守備力:{}'.format(self.name,self.attack,self.defense))

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
    print(f'{team_number}')
    Team.info(teams[team_number-1])
    team_number += 1

def choice_team(player):
    global playing_teams
    if player == 'myself':
        player_name = '自分'
    elif player == 'enemy':
        player_name = '相手'

    choice_team_number = int(input(player_name + 'のチームを選択してください(1~3)'))
    playing_teams[player] = teams[choice_team_number - 1]
    print('{}のチームは「{}」です'.format(player_name, playing_teams[player].name))


def get_play_inning(inning):
  if inning == 'front':
    hit_rate = playing_teams["myself"].get_hit_rate()
    out_rate = playing_teams["enemy"].get_out_rate()
  else:
    hit_rate = playing_teams["myself"].get_out_rate()
    out_rate = playing_teams["enemy"].get_hit_rate()

  inning_score = math.floor((hit_rate - out_rate) / 10)
  if inning_score < 0:
    inning_score = 0

  return inning_score
    
def scoreboard():
  score_boards = ['____ |','自分｜','相手｜']
  for i in range(9):

    score_boards[0] += (str(i+1)+'|')

    inning = 'front'
    my_score = get_play_inning(inning)
    score_boards[1] += str(my_score)+'|'
    playing_teams['myself'].total_score += my_score

    if i == 8 and playing_teams['myself'].total_score < playing_teams['enemy'].total_score :
      score_boards[2] += '✖'+'|'
    else:
      inning = 'back'
      enemy_score = get_play_inning(inning)
      score_boards[2] += str(enemy_score)+'|'
      playing_teams['enemy'].total_score += enemy_score
  
  print(score_boards[0] + 'R|')
  print(score_boards[1] + str(playing_teams['myself'].total_score)+'|')
  print(score_boards[2] + str(playing_teams['enemy'].total_score)+'|')



def play():
  print('全チームの情報')
  create_teams()
  show_teams()
  choice_team('myself')
  choice_team('enemy')
  scoreboard()
  
  
play()

import random

players = []
table = []

class Player:
    def __init__(self, name, coin,):
        self.name = name
        self.coin = coin
        self.bets = {}
        for cell in table:
            self.bets.update({cell.name: 0})

    def set_bet_coin(self, bet_coin,bet_cell):
        self.coin -= int(bet_coin)
        print(str(self.name) + 'は' + str(bet_coin) + 'コインを' + bet_cell + 'にBETしました.')
        for i in table:
            self.bets.update({bet_cell:bet_coin})

    def reset_table(self):
        for i in table:
            self.bets.update({i.name:0})

def reset_table():
    for i in players:
        i.reset_table()

class Human(Player):
    def __init__(self, name, coin):
        super().__init__(name, coin)

    def bet(self):

        if self.coin >= 99:
            max_bet_coin = 99
        else:
            max_bet_coin = self.coin
        
        bet_coin = input('何枚BETしますか？:(1~' + str(max_bet_coin) +')')
        while not self.enable_bet_coin(bet_coin,max_bet_coin):
            bet_coin = input('何枚BETしますか？:(1~' + str(max_bet_coin) +')')

        place_name = input('どこにBETしますか？：(R,B,1~8)')
        while  not self.enable_bet_cell(place_name):
            place_name = input('どこにBETしますか？：(R,B<1~8)')

        super().set_bet_coin(bet_coin,place_name)

    def enable_bet_coin(self, string,max_bet_coin ):
        if string.isdigit() == True:
            if 1 <= int(string) <= max_bet_coin:
                return True
            else:
                return False
        else:
            return False

    
    def enable_bet_cell(self,string):
        if string == 'R' or string == 'B':
            return True
        elif string.isdigit() == True:
            if 1 <= int(string) <= 8:
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
            bet_coin = random.randint(1, self.coin)
        else:
            bet_coin = random.randint(1, 99)

        bet_cell = cells[random.randint(0,9)]
        super().set_bet_coin(bet_coin,bet_cell)
    
    def set_cells():
        global cells 
        cells = []
        for i in table:
            cells += i.__dict__['name']

def create_players():
    global players
    player1 = Human('私', 500)
    player2 = Computer('C1', 500)
    player3 = Computer('C2', 500)
    player4 = Computer('C3', 500)
    players = [player1, player2, player3, player4]

def check_hit():
    hit_place = random.randint(2,9)
    cell_number = cells[hit_place]
    cell_color = table[hit_place].color
    print ('選ばれたのは「' + cell_number + ":" + cell_color + '」')
    for i in players:
        print(f'{i.name}:{i.bets}')
        if int(i.bets[cell_number]) > 0:
            print(i.name + 'は当たり' + str(win_player(i,hit_place)) + 'を獲得しました')
        if int(i.bets['R']) > 0 and cell_color == "red":
            print(i.name + 'は当たり' + str(win_player(i,0)) + 'を獲得しました')
        if int(i.bets['B']) > 0 and cell_color == "black":
            print(i.name + 'は当たり' + str(win_player(i,1)) + 'を獲得しました')

def win_player(players,hit_cell_number):
    number = int(players.bets[cells[hit_cell_number]])
    rate = int(table[hit_cell_number].rate)
    players.coin += number*rate
    return number*rate

def bet_players():
    for i in players:
        i.bet()

class Cell:
    def __init__(self, name, rate, color):
        self.name = name
        self.rate = rate
        self.color = color

class ColorBase:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    END = '\033[0m'

def color(color_name, string):
    if color_name == 'red':
        return ColorBase.RED + string + ColorBase.END
    else:
        return string     

def create_table():
    global table
    table.append(Cell('R', 2, 'red'))
    table.append(Cell('B', 2, 'black'))
    table.append(Cell('1', 8, 'red'))
    table.append(Cell('2', 8, 'black'))
    table.append(Cell('3', 8, 'red'))
    table.append(Cell('4', 8, 'black'))
    table.append(Cell('5', 8, 'red'))
    table.append(Cell('6', 8, 'black'))
    table.append(Cell('7', 8, 'red'))
    table.append(Cell('8', 8, 'black'))

def show_table():
    print(green_bar('|') + '＿＿ ' + green_bar('|') + players[0].name + green_bar('|') + players[1].name + green_bar('|') + players[2].name + green_bar('|') + players[3].name + green_bar('|'))
    for cell in table:
        color_name = cell.color
        string = str(cell.name + '(×' + str(cell.rate) + ')')

        bets_count = str(green_bar('|')) + str(color(color_name, string)) + str(green_bar('|'))
        for player in players:
            bets_count += (str(player.bets[cell.name]).zfill(2) + green_bar('|'))
        
        print(bets_count)

def green_bar(string):
    return ColorBase.GREEN + string + ColorBase.END

def show_coin():
    players_coin = ''
    for i in players:
        players_coin += (i.name + ':' + str(i.coin) + '/')
    
    print('[持ちコイン]' + players_coin) 

def is_game_end():
    for i in players:
        if i.coin <= 0:
            return True
        return False
    
def game_end():
    for i in players:
        if i.coin <= 0:
            print(i.name + 'のコインがなくなったためゲームを終了します。')

def initialize():
    create_table()
    create_players()
    Computer.set_cells()
    show_coin()

def play_once():
    bet_players()
    show_table()
    check_hit()
    show_coin()
    reset_table()
 
def play():
    print('デバッグログ：play()')
    initialize()
    play_once()
    while not is_game_end():
        play_once()
    else:
        game_end()
play()
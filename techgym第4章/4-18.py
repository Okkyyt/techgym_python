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

    def info(self):
        print(self.name + ':' + str(self.coin))

    def set_bet_coin(self, bet_coin):
        self.coin -= int(bet_coin)
        print(str(self.name) + 'は' + str(bet_coin) + 'コインBETしました.')


class Human(Player):
    def __init__(self, name, coin):
        super().__init__(name, coin)

    def bet(self):
        bet_coin = input('何枚BETしますか？:(1~99)')
        while not self.enable_bet_coin(bet_coin):
            bet_coin = input('何枚BETしますか？:(1~99)')

        print(str(bet_coin))

        super().set_bet_coin(bet_coin)

    def enable_bet_coin(self, string):
        if string.isdigit() == True:
            if 1 <= int(string) <= 99:
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

        super().set_bet_coin(bet_coin)

def create_players():
    global players
    player1 = Human('私', 500)
    player2 = Computer('C1', 500)
    player3 = Computer('C2', 500)
    player4 = Computer('C3', 500)
    players = [player1, player2, player3, player4]

def show_players():
    for i in players:
        i.info()
    for i in players:
        i.bet()
    for i in players:
        i.info()

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
    table.append(Cell('R', 8, 'red'))
    table.append(Cell('B', 8, 'black'))
    table.append(Cell('1', 2, 'red'))
    table.append(Cell('2', 2, 'black'))
    table.append(Cell('3', 2, 'red'))
    table.append(Cell('4', 2, 'black'))
    table.append(Cell('5', 2, 'red'))
    table.append(Cell('6', 2, 'black'))
    table.append(Cell('7', 2, 'red'))
    table.append(Cell('8', 2, 'black'))

def show_table():
    print(green_bar('|') + '＿＿' + green_bar('|') + players[0].name + green_bar('|') + players[1].name + green_bar('|') + players[2].name + green_bar('|') + players[3].name + green_bar('|'))
    for cell in table:
        color_name = cell.color
        string = str(cell.name + '(×' + str(cell.rate) + ')')

        bets_count = str(green_bar('|')) + str(color(color_name, string)) + str(green_bar('|'))
        for player in players:
            bets_count += (str(player.bets[cell.name]).zfill(2) + green_bar('|'))
        
        print(bets_count)

def green_bar(string):
    return ColorBase.GREEN + string + ColorBase.END

def play():
    create_table()
    create_players()
    print('デバッグログ：play()')
    show_table()
    #show_players()

play()

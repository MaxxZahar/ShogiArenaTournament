import csv
from player import Player
from player import Game
import os


def addResult(winner_index, loser_index, handicap, players):
    winner = players[winner_index]
    loser = players[loser_index]
    if handicap:
        winner.results.append(f'{loser_index + 1}+({handicap}) ')
        if handicap[0] == '+':
            reverse_handicap = '-' + handicap[1:]
            loser.results.append(f'{winner_index + 1}-({reverse_handicap}) ')
        elif handicap[0] == '-':
            reverse_handicap = '+' + handicap[1:]
            loser.results.append(f'{winner_index + 1}-({reverse_handicap}) ')
    else:
        loser.results.append(f'{winner_index + 1}- ')
        winner.results.append(f'{loser_index + 1}+ ')


def addZeros(players):
    max_length = 0
    for player in players:
        if len(player.results) > max_length:
            max_length = len(player.results)
    for player in players:
        diff = max_length - len(player.results)
        if diff:
            for i in range(diff):
                player.results.append('0- ')


location = os.path.split(__file__)[0]
os.chdir(location)
players = []
results = []
with open("../data/players.csv") as players_file:
    reader = csv.reader(players_file, delimiter=';')
    i = 0
    for line in reader:
        if i:
            players.append(Player(int(line[0]), line[1], line[2]))
        i += 1
with open("../data/results.csv") as results_file:
    reader = csv.reader(results_file, delimiter=';')
    i = 0
    for line in reader:
        if i:
            results.append(Game(int(line[0]), int(line[1]), line[2]))
        i += 1
for game in results:
    players[game.winner - 1].points += 1
    players[game.winner - 1].games += 1
    players[game.loser - 1].games += 1
for player in players:
    player.win_rate = player.points / player.games
players.sort(key=lambda player: (player.points, player.win_rate), reverse=True)
for game in results:
    winner = [player for player in players if player.id == game.winner][0]
    winner_index = players.index(winner)
    loser = [player for player in players if player.id == game.loser][0]
    loser_index = players.index(loser)
    winner = players[winner_index]
    loser = players[loser_index]
    if len(winner.results) < len(loser.results):
        diff = len(loser.results) - len(winner.results)
        for i in range(diff):
            winner.results.append('0- ')
    elif len(winner.results) > len(loser.results):
        diff = len(winner.results) - len(loser.results)
        for i in range(diff):
            loser.results.append('0- ')
    addResult(winner_index, loser_index, game.handicap, players)
addZeros(players)
for player in players:
    print(player.results)
table = []
for i, player in enumerate(players):
    results_line = ''.join(player.results)
    table_line = f'{i + 1}. [{player.last_name}] [{player.first_name}] [{results_line}] {player.points}'
    table.append(table_line)
with open("../temp/table.txt", "w") as table_file:
    for line in table:
        table_file.writelines(line + '\n')

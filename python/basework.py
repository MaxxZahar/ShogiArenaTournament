import re
import csv


def extract_players(table):
    players = []
    for line in table:
        player = {}
        player['last_name'] = re.search('\[.*?\]', line).group(0)[1:-1].strip()
        rb_index = line.index(']')
        player['first_name'] = re.search(
            '\[.*?\]', line[rb_index + 1:]).group(0)[1:-1].strip()
        players.append(player)
    return players


def add_players_to_base(table, type=False):
    if type:
        players = extract_players(table)
    else:
        players = table
    with open("../data/data.csv", 'a', newline='') as base:
        writer = csv.DictWriter(
            base, fieldnames=['last_name', 'first_name'], delimiter=';')
        for player in players:
            writer.writerow(player)


def compare_players_with_base(table):
    players = extract_players(table)
    database_players = []
    players_not_exist = []
    with open("../data/data.csv") as base:
        reader = csv.DictReader(
            base, fieldnames=['last_name', 'first_name'], delimiter=';')
        for row in reader:
            database_players.append(row)
        players_not_exist = [
            player for player in players if player not in database_players]
        for player in players_not_exist:
            print(
                f'Unknown player {player["last_name"], player["first_name"]}')
        if not len(players_not_exist):
            print('Players are checked')
        return players_not_exist

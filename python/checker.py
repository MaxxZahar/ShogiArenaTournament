import os
import csv
import re
from alphabet_detector import AlphabetDetector


def check_brackets(line):
    if (line.count('[') == line.count(']') and line.count('[') == 3):
        return True
    return False


def check_all_brackets(table):
    for i, line in enumerate(table):
        if not check_brackets(line):
            raise Exception(f'Some issue with brackets in line {i + 1}')
    else:
        print('Brackets are checked')
        return True


def check_language(line):
    ad = AlphabetDetector()
    if (ad.only_alphabet_chars(line, "LATIN")):
        return True
    return False


def check_all_language(table):
    for i, line in enumerate(table):
        if not check_language(line):
            raise Exception(f'Some issues with language in line {i + 1}')
    else:
        print('Language is checked')
        return True


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


def add_players_to_base(table):
    players = extract_players(table)
    with open("../data/data.csv", 'a', newline='') as base:
        writer = csv.DictWriter(
            base, fieldnames=['last_name', 'first_name'], delimiter=';')
        for player in players:
            writer.writerow(player)


location = os.path.split(__file__)[0]
os.chdir(location)
with open("../data/table.txt") as table:
    table_body = table.readlines()[1:]
    check_all_brackets(table_body)
    check_all_language(table_body)
    # add_players_to_base(table_body)

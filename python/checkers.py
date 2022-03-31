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


def check_points(line):
    rb_index = line.rindex(']')
    try:
        points = float(re.search('\].*', line[rb_index:]).group(0)[1:].strip())
    except:
        raise Exception('Points are not presented right way')
    pluses = line.count('+')
    equals = line.count('=')
    total = pluses + equals / 2
    if (total == points):
        return True
    return False


def check_all_points(table):
    for i, line in enumerate(table):
        if not check_points(line):
            raise Exception(f'Wrong point value in line {i + 1}')
    else:
        print('Points are checked')
        return True


def get_results_string(line):
    lb_index = line.rindex('[')
    string = re.search('\[.*\]', line[lb_index:]
                       ).group(0).strip()[1:-1].strip()
    string = string.replace(" ", "").replace('\t', '')
    return string


def get_results(line):
    string = get_results_string(line)
    separators = {'+', '-', '='}
    current = ''
    results = []
    for s in string:
        if not s in separators:
            current += s
        else:
            result = {}
            result['opponent'] = int(current)
            if s == '+':
                result['score'] = 1
            elif s == '-':
                result['score'] = 0
            else:
                result['score'] = 0.5
            results.append(result)
            current = ''
    return results


def get_all_results(table):
    results = []
    for i, line in enumerate(table):
        result = {}
        result['player'] = i + 1
        result['games'] = get_results(line)
        results.append(result)
    return results


def check_all_legs(table):
    results = get_all_results(table)
    number_of_legs = len(results[0]['games'])
    for i, result in enumerate(results):
        if not len(result['games']) == number_of_legs:
            raise Exception(f'Unequal number of games in line {i + 1}')
    else:
        print('Legs are checked')
        return True


def check_self_playing(table):
    results = get_all_results(table)
    for i, result in enumerate(results):
        for game in result['games']:
            if result['player'] == game['opponent']:
                raise Exception(
                    f'Wrong result: game with himself in line {i + 1}')
    else:
        print('Selfplay is checked')
        return True


def check_results(table):
    results = get_all_results(table)
    for i, result in enumerate(results):
        for j, game in enumerate(result['games']):
            if game['opponent']:
                if game['opponent'] > len(results):
                    raise Exception(
                        f'Wrong result: such opponent does not exist in line {i + 1}')
                if not result['player'] == results[game['opponent'] - 1]['games'][j]['opponent']:
                    raise Exception(
                        f'Wrong result: wrong opponent in line {i + 1} in leg {j + 1}')
                if not game['score'] + results[game['opponent'] - 1]['games'][j]['score'] == 1:
                    raise Exception(
                        f'Wrong result: wrong result in line {i + 1} in leg {j + 1}')
    else:
        print('Results are checked')
        return True

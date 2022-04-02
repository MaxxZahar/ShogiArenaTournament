import os
from checkers import check_all_brackets, check_all_language, check_all_legs, check_all_points, check_self_playing, check_results
from basework import compare_players_with_base, add_players_to_base

location = os.path.split(__file__)[0]
os.chdir(location)
with open("../data/table.txt") as table:
    table_body = table.readlines()[1:]
    check_all_brackets(table_body)
    check_all_language(table_body)
    new_players = compare_players_with_base(table_body)
    check_all_points(table_body)

    check_all_legs(table_body)
    check_self_playing(table_body)
    check_results(table_body)
    add_players_to_base(new_players)

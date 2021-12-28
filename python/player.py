class Player:
    def __init__(self, id, last_name, first_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.points = 0
        self.games = 0
        self.win_rate = 0
        self.results = []

    def __str__(self):
        return f'{self.id}. {self.last_name} {self.first_name} {self.points} {self.win_rate}'


class Game:
    def __init__(self, winner, loser, handicap):
        self.winner = winner
        self.loser = loser
        self.handicap = handicap

    def __str__(self):
        if self.handicap:
            return f'winner: {self.winner}, loser: {self.loser}, handicap: {self.handicap}'
        return f'winner: {self.winner}, loser: {self.loser}'

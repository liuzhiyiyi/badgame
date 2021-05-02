


class Game_data():
    def __init__(self,pm):
        self.pm=pm
        self.reset_data()
        self.game_active=False
        self.score=0
        self.high_score=0
        self.level=0
        self.up_level()

    def reset_data(self):
        self.ships_left=self.pm.ship_limit

    def up_level(self):
            self.level= self.level+1





class Game_data():
    def __init__(self,pm):
        self.pm=pm
        self.reset_data()
        self.game_active=False

    def reset_data(self):
        self.ships_left=self.pm.ship_limit
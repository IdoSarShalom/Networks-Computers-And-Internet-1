# ******************************
# Tomer Griba 325105625
# Ido Sar Shalom 212410146
# ******************************
class player:
    def __init__(self):
        self.money = 0
        self.place = 0
        self.player_help = True

    def get_money(self):
        return self.money

    def get_place(self):
        return self.place

    def get_help(self):
        return self.player_help

    def add_money(self, money):
        self.money = self.money + money

    def set_money(self, money):
        self.money = money

    def add_place(self, place):
        self.place = self.place + place

    def set_place(self, place):
        self.place = place


    #The player used his help --> change the player_help to false
    def use_help(self):
            self.player_help = False


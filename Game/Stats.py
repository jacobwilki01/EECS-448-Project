class World_Stats:
    def __init__(self):
        self.lives = 3
        self.coins = 0
        self.score = 0
        self.level = 0
    def update_lives(self,value):
        self.lives += value
    def update_coins(self,value):
        self.coins += value
    def update_score(self,value):
        self.score += value
    def update_level(self,value):
        self.level += value
    def reset(self):
        self.lives = 3
        self.coins = 0
        self.score = 0
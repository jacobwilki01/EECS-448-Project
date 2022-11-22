class World_Stats:
    def __init__(self):
        try:
            file = open('saves/save.txt','r')
            self.prev_data = []
            for item in file:
                self.prev_data.append(int(item))
            file.close()

            self.lives = self.prev_data[0]
            self.coins = self.prev_data[1]
            self.score = self.prev_data[2]
            self.level = self.prev_data[3]

            self.has_updated = True
        except:
            self.lives = 3
            self.coins = 0
            self.score = 0
            self.level = 0

            self.has_updated = False

    def update_lives(self,value):
        self.lives += value
        self.has_updated = True
    def update_coins(self,value):
        self.coins += value
        self.has_updated = True
    def update_score(self,value):
        self.score += value
        self.has_updated = True
    def update_level(self,value):
        self.level += value
        self.has_updated = True
    def reset(self):
        self.lives = 3
        self.coins = 0
        self.score = 0
        self.level = 0

        self.has_updated = False
    def write_save_file(self):
        if self.has_updated:
            file = open('saves/save.txt','w')
            for item in [self.lives,self.coins,self.score,self.level]:
                file.write(str(item)+'\n')
            file.close()
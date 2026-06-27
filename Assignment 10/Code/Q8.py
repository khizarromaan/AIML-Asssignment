class Player:
    def __init__(self, name, score=0, level=1):
        self.name = name
        self.score = score
        self.level = level
        
    def increase_score(self, points):
        self.score = self.score + points
        
    def level_up(self):
        self.level = self.level + 1
        
    def show_progress(self):
        print("Player:", self.name, "Level:", self.level, "Score:", self.score)

player = Player("Khizar")
player.show_progress()
player.increase_score(100)
player.increase_score(50)
player.level_up()
player.show_progress()
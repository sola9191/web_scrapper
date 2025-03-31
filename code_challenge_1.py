class Player:
    def __init__(self, name, team):
        self.name = name
        self.xp = 1500
        self.team = team
    
    def introduce(self):
        print(f"Hello! I'm {self.name} and I play for {self.team}")

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []
    
    def add_player(self, name):
        new_player = Player(name, self.team_name)
        self.players.append(new_player)
    
    def show_players(self):
        for player in self.players:
            player.introduce()
    
    def remove_player(self, name):
        for player in self.players:
            if name == player.name:
                self.players.remove(player)
    
    def show_xp(self):
        total_xp = 0
        for player in self.players:
            total_xp += player.xp
        print(f"{self.team_name}의 경험치 총량은 {total_xp}입니다.")
            
team_x = Team("Team X")
team_x.add_player("nico")
team_x.add_player("Alex")
team_x.add_player("Bread")
team_x.add_player("Chu")
team_x.show_players()
team_x.remove_player("Bread")
team_x.show_players()
team_x.show_xp()
class Guest:
    
    def __init__(self, name, age, wallet, song):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.favourite_song = song
    
    def has_sufficient_money(self, amount):
        return self.wallet >= amount
    
    def pay_with_wallet(self, amount):
        self.wallet -= amount
    
    def cheer(self, song):
        if song == self.favourite_song:
            return "Woohoo!"
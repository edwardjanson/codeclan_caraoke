class Guest:
    
    def __init__(self, name, age, wallet, song):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.favourite_song = song
    
    def has_sufficient_money(self, amount):
        return self.wallet >= amount
    
    def pay_with_wallet(self, amount):
        if self.has_sufficient_money(amount):
            self.wallet -= amount
        else:
            return "Not enough money."
    
    def cheer(self, song):
        if song == self.favourite_song:
            return "Woohoo!"
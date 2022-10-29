class Room:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.songs = []
        self.guests = []
        self.tab = {}
    
    def add_song(self, song):
        self.songs.append(song)
    
    def has_space(self):
        return self.capacity > len(self.guests)
    
    def increase_tab(self, amount, guest):
        if guest in self.tab:
            self.tab[guest] += amount
        else:
            self.tab[guest] = amount
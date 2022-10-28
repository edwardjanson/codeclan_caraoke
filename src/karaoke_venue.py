from src.room import Room
from src.guest import Guest


class KaraokeVenue:

    def __init__(self, name, till):
        self.name = name
        self.rooms = []
        self.till = till
        self.entry_fee = 10
        self.bar = None
    
    def add_room(self, room):
        self.rooms.append(room)

    def add_bar(self, bar):
        self.bar = bar
    
    def increase_till(self, amount):
        self.till += amount
    
    def get_entry_fee(self, guest, room):
        if room.has_space() and guest.has_sufficient_money(self.entry_fee):
            guest.pay_with_wallet(self.entry_fee)
            self.increase_till(self.entry_fee)
            room.check_in_guest(guest)

    def check_in_guest(self, guest, room):
        if room.has_space():
            room.guests.append(guest)
        else:
            return "Sorry, this room is full."
    
    def check_out_guest(self, guest, room):
        room.guests.remove(guest)
        guest.pay_with_wallet(room.tab[guest.name])
        self.increase_till(room.tab[guest.name])
        room.tab[guest].clear()
    
    def tab_value(self):
        return sum([room.tab for room in self.rooms])

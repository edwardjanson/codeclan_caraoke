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

    def check_in_guest(self, guest, room):
        room.guests.append(guest)
    
    def check_out_guest(self, guest, room):
        if guest in room.tab:
            guest.pay_with_wallet(room.tab[guest])
            self.increase_till(room.tab[guest])
            room.tab.pop(guest)
        room.guests.remove(guest)

    def get_entry_fee(self, guest, room):
        if room.has_space() and guest.has_sufficient_money(self.entry_fee):
            guest.pay_with_wallet(self.entry_fee)
            self.increase_till(self.entry_fee)
            self.check_in_guest(guest, room)
    
    def tab_value(self):
        return sum([sum([value for value in room.tab.values()]) for room in self.rooms])

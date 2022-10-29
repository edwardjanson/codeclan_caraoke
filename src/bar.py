class Bar:
    
    def __init__(self):
        self.drinks_list = []

    def add_drink(self, drink):
        self.drinks_list.append(drink)

    def sell_drink(self, guest, room, drink):
        if guest.has_sufficient_money(drink.price):
            if drink.has_alcohol and guest.age < 18:
                return "Too young."
            
            guest.pay_with_wallet(drink.price)
            room.increase_tab(drink.price, guest)
            return "Cheers."
        return "That's not enough money."


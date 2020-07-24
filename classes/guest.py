class Guest:
    def __init__(self, name, age, money, fav = None):
        self.name = name
        self.age = age
        self.wallet = money
        self.fav_song = fav

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def cheer(self):
        return "Whoo! They have my favourite song!"
class Bartab:
    def __init__(self):
        self.total = 0
        self.receipt = []

    def increase_total(self, amount):
        self.total += amount

    def add_receipt_item(self, guest, reason, amount):
        item = {"Customer":guest.name, "Sale Item":reason, "Value":amount}
        self.receipt.append(item)
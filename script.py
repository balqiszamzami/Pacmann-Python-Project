class Transaction:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def update_item_name(self, old_name, new_name):
        for item in self.items:
            if item[0] == old_name:
                item[0] = new_name
                break

    def update_item_qty(self, name, new_qty):
        for item in self.items:
            if item[0] == name:
                item[1] = new_qty
                break

    def update_item_price(self, name, new_price):
        for item in self.items:
            if item[0] == name:
                item[2] = new_price
                break

    def delete_item(self, name):
        for item in self.items:
            if item[0] == name:
                self.items.remove(item)
                break

    def reset_transaction(self):
        self.items = []

    def check_order(self):
        for item in self.items:
            if None in item:
                print("Terdapat kesalahan input data")
                return
        print("Pemesanan sudah benar")
        self.show_order()

    def show_order(self):
        print("No | Nama Item | Jumlah Item | Harga/Item | Total Harga |")
        print("-" * 56)
        for i, item in enumerate(self.items):
            total_price = item[1] * item[2]
            print(f"{i+1:>2} | {item[0]:<9} | {item[1]:^11} | {item[2]:^11} | {total_price:>11}")
        print("-" * 56)

    def total_price(self):
        total = 0
        for item in self.items:
            total += item[1] * item[2]
        if total >= 500000:
            discount = 0.1
        elif total >= 300000:
            discount = 0.08
        elif total >= 200000:
            discount = 0.05
        else:
            discount = 0
        discounted_price = total * (1 - discount)
        print(f"Total Harga: Rp {total:,}")
        print(f"Harga Setelah Diskon ({discount*100:.0f}%): Rp {discounted_price:,}")
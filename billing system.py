"""
Week 3 - Mini Project: Billing System (OOP-based)
- Product class -> attributes: name, price, quantity
- Bill class -> total calculation + tax
- Display final bill in tabular format
"""


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def subtotal(self):
        return self.price * self.quantity


class Bill:
    TAX_RATE = 0.05  # 5% tax

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_subtotal(self):
        return sum(p.subtotal() for p in self.products)

    def calculate_tax(self):
        return self.calculate_subtotal() * self.TAX_RATE

    def calculate_total(self):
        return self.calculate_subtotal() + self.calculate_tax()

    def display_bill(self):
        print(f"{'Product':<15}{'Price':>10}{'Qty':>8}{'Subtotal':>12}")
        print("-" * 45)
        for p in self.products:
            print(f"{p.name:<15}{p.price:>10.2f}{p.quantity:>8}{p.subtotal():>12.2f}")
        print("-" * 45)
        print(f"{'Subtotal':<33}{self.calculate_subtotal():>12.2f}")
        print(f"{'Tax (5%)':<33}{self.calculate_tax():>12.2f}")
        print(f"{'Total':<33}{self.calculate_total():>12.2f}")


if __name__ == "__main__":
    bill = Bill()
    bill.add_product(Product("Notebook", 50.0, 3))
    bill.add_product(Product("Pen", 10.0, 5))
    bill.add_product(Product("Backpack", 800.0, 1))

    bill.display_bill()

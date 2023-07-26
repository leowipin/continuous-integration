class DiningExperienceManager:
    def __init__(self):
        self.menu = {
            'Chinese': {'chaulafan': 10, 'wantang': 8},
            'Italian': {'pizza': 30, 'fetuccini': 10},
            'Pastries': {'cupcake': 3, 'cheesecake': 4},
            'Chef\'s Specials': {'tomahawk': 25, 'bife': 30}
        }
        self.total_cost = 0
        self.total_quantity = 0

    def display_menu(self):
        for category, items in self.menu.items():
            print(f'{category}:')
            for item, price in items.items():
                print(f'    {item} - ${price}')
        print()

    def select_meals(self, input_function=input):
        self.order = {}
        self.total_quantity = 0

        while True:
            meal = input_function('Enter meal name (or "done" to finish): ')
            if meal == 'done':
                break
            if not any(meal in items for items in self.menu.values()):
                print('Invalid meal selection. Please try again.')
                continue
            while True:
                quantity = input_function('Enter quantity: ')
                if not quantity.isdigit() or int(quantity) < 1:
                    print('Invalid quantity. Please try again.')
                elif self.total_quantity + int(quantity) > 100:
                    print('Maximum order quantity exceeded. Please try again.')
                else:
                    break
            self.order[meal] = int(quantity)
            self.total_quantity += int(quantity)



    def calculate_cost(self):
        for meal, quantity in self.order.items():
            for category, items in self.menu.items():
                if meal in items:
                    price = items[meal]
                    if category == 'Chef\'s Specials':
                        price *= 1.05
                    self.total_cost += price * quantity
        if self.total_quantity > 10:
            self.total_cost *= 0.8
        elif self.total_quantity > 5:
            self.total_cost *= 0.9
        if self.total_cost > 100:
            self.total_cost -= 25
        elif self.total_cost > 50:
            self.total_cost -= 10

    def confirm_order(self, input_function=input):
        print('Your order:')
        for meal, quantity in self.order.items():
            print(f'    {meal} x{quantity}')
        print(f'Total cost: ${self.total_cost:.2f}')
        while True:
            confirm = input_function('Confirm order? (y/n): ')
            if confirm == 'y':
                return True
            elif confirm == 'n':
                return False

    def run(self, input_function=input):
        while True:
            self.display_menu()
            self.select_meals(input_function)
            if not self.order:
                return -1
            self.calculate_cost()
            if not self.confirm_order(input_function):
                return -1
            return int(self.total_cost)
        
def mock_input(inputs):
    def input(prompt):
        return inputs.pop(0)
    return input

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
mach= True
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
while mach:
    ch = input("What would you like? (espresso/latte/cappuccino/), 'report' for info OR 'off' to close:")
    if ch == "report":
        coffee_maker.report()
        money_machine.report()
    elif ch == "off":
        mach = False
    else:
        drink = menu.find_drink(ch)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


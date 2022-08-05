from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()
my_Menu = Menu()
# my_Menu_Item = MenuItem()
# my_coffee_maker = CoffeeMaker()

isOn = True

while isOn:
    get_input = input("What you like to drink?: ")
    if get_input == "menu":
        print(my_Menu.get_items())
        isOn = False
    else:
        print(my_Menu.find_drink(get_input))
        isOn = False

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MyMoneyMachine = MoneyMachine()
MyMenu = Menu()
MyCoffeeMaker = CoffeeMaker()
# my_Menu_Item = MenuItem()
# my_coffee_maker = CoffeeMaker()

isOn = True

while isOn:
    get_input = input("What you like to drink?: ")
    if get_input == "menu":
        print(MyMenu.get_items())
    elif get_input == "report":
        MyCoffeeMaker.report()
        MyMoneyMachine.report()

    elif get_input == "off":
        isOn = False
    else:

        drink = MyMenu.find_drink(get_input)
        if MyCoffeeMaker.is_resource_sufficient(drink) and MyMoneyMachine.make_payment(drink.cost):
            MyCoffeeMaker.make_coffee(drink)

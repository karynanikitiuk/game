import json
from unit import Units
from army import Army
from pprint import pprint

class Menu():
    def __init__(self):
        self.unit_obj = Units()
        self.army_obj = Army()



        self.MENU = [
            ['Create squad', lambda: self.interact([
                ['Create squad', lambda: self.unit_obj.create_unit()],
                ['List squad', lambda: self.print_data('units_list')],
                ['Back', lambda: 'exit']
            ])],
            ['Rules', lambda:  self.interact([
                ['Create rules', lambda: self.unit_obj.create_rules()],
                ['List rules', lambda: self.print_data('rules_list')],
                ['Back', lambda: 'exit']
            ])],
            ['Create user Army', lambda: self.army_obj.create_army()],
            ['Play', lambda: self.army_obj.battle()],
            ['Set default', lambda: self.clear_data()],
            ['Exit', lambda: 'exit'],
        ]

    def add(self, entity_type):
        record = {}
        fields = FIELDS[entity_type]
        for name, validators in fields:
            while True:
                val = input(name + ': ')
                for check in validators:
                    err = check(val)
                    if err is not None:
                        print('Incorrect value:', err)
                        break
                else:
                    record[name] = val
                    break
        list.append(data[entity_type], record)
        print(data)


    def print_menu(self, menu):
        print('-' * 20)
        for i in range(len(menu)):
            print(i + 1, menu[i][0])

    def get_num_option(self, menu, choice):
        i = int(choice) - 1
        if 0 <= i < len(menu):
            return menu[i]


    def get_str_option(self, menu, choice):
        for option in menu:
            if option[0] == choice:
                return option


    def clear_file(self, file):
        with open(file, 'w') as f:
            json.dump([], f)

    def set_default(self):
        self.unit_obj.units_list = []
        self.unit_obj.rules_list = []
        self.army_obj.comp_army = []
        self.army_obj.user_army = []
        self.army_obj.units_list = []
        self.army_obj.rules_list = []

    def clear_data(self):
        self.clear_file('units.json')
        self.clear_file('rules.json')
        self.set_default()
        print('Done!')


    def interact(self, menu):
        while True:
            self.print_menu(menu)
            choice = input('Your choice: ')

            if str.isnumeric(choice):
                option = self.get_num_option(menu, choice)
            else:
                option = self.get_str_option(menu, choice)

            if option is None:
                print('Incorrect choice <%s>' % choice)
                continue

            action = option[1]
            result = action()
            if result == 'exit':
                print()
                break


    def print_data(self, name):
        if name == 'units_list':
            pprint(self.unit_obj.units_list)
        if name == 'rules_list':
            pprint(self.unit_obj.rules_list)

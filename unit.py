
import json
from random import randint
from pprint import pprint


class Units():

    def __init__(self):

        self.rules_list = []
        self.units_list = []
        self.read_data('rules.json')
        self.read_data('units.json')

    def create_unit(self):

        name = str(input("Enter unit name: "))
        health = int(input("Enter unit health: "))
        damage = float(input("Enter unit damage: "))

        new_unit = {"name" : name, "health" : health, "damage" : damage}

        self.save_data(new_unit, 'units.json')



    def create_rules(self):
        attacker = ""
        defender = ""

        pprint(self.units_list)

        if len(self.units_list) > 0:
            while not self.check_unit(attacker):
                attacker = str(input("Enter attacker name: "))

            while not self.check_unit(defender):
                defender = str(input("Enter defender name: "))

            streng = float(input("Enter damage power: "))

            params = {"attacker" : attacker, "defender" : defender, "streng" : streng}

            self.save_data(params, 'rules.json')



    def check_unit(self, unit_name):
        exist = False
        for i in range(len(self.units_list)):
            if self.units_list[i]['name'] == unit_name:
                exist = True
                break

        return exist

    def read_data(self, file):
        with open(file) as f:
            if file == 'units.json':
                self.units_list = json.load(f)

            else:
                self.rules_list = json.load(f)



    def save_data(self, rec, file):
        if file == 'units.json':
            self.units_list.append(rec)

            with open(file, 'w') as f:
                json.dump(self.units_list, f)
        else:
            print("Saving rule")
            self.rules_list.append(rec)

            with open(file, 'w') as f:
                json.dump(self.rules_list, f)


import json
from random import randint as rand
from pprint import pprint


class Army():

    def __init__(self):

        self.units_list = self.read_data_2('units.json')
        self.rules_list = self.read_data_2('rules.json')
        self.user_army = []
        self.comp_army = []
        self.comp_army = self.create_squad()



    def create_army(self):
        self.units_list = self.read_data_2('units.json')
        max_limit = 100

        for unit in self.units_list :
            if (max_limit > 0) :
                message = 'Input count of units for ' + '<' + unit['name'] + '>' + ' squad (limit - '+ str(max_limit) + '): \n'
                squad = {'name': unit['name'], 'count': 0}

                while squad['count'] < 1 or squad['count'] > max_limit :
                    squad['count'] = int(input(message))

                max_limit -= squad['count']
                self.user_army.append(squad)
            else :
                print('Army is full!!')
                break
        pprint(self.user_army)
        return self.user_army


    def create_squad(self):
        max_limit = 100

        for unit in self.units_list :
            if (max_limit > 0) :
                squad = {'name': unit['name'], 'count': rand(1,max_limit)}

                max_limit -= squad['count']
                self.comp_army.append(squad)
            else :
                break

        return self.comp_army

    def fight(self, attacker, defender):
        attacker_streng = 1
        defender_streng = 1

        for rule in self.rules_list:
            if rule['attacker'] == attacker['name'] and rule['defender'] == defender['name']:
                attakcer_streng = rule['streng']

            if rule['attacker'] == defender['name'] and rule['defender'] == attacker['name']:
                defender_streng = rule['streng']


        while attacker['count'] != 0 and defender['count'] != 0:
            for unit in self.units_list:
                if unit['name'] == attacker['name']:
                    att_health = attacker['count'] * unit['health']
                    att_damage = attacker['count'] * unit['damage'] * attacker_streng

                if unit['name'] == defender['name']:
                    def_health = defender['count'] * unit['health']
                    def_damage = defender['count'] * unit['damage'] * defender_streng

            att_health -= def_damage
            def_health -= att_damage

            for unit in self.units_list:
                if unit['name'] == attacker['name']:
                    if att_health > 0:
                        attacker['count'] = int(att_health / unit['health'])
                    else :
                        attacker['count'] = 0
                if unit['name'] == defender['name']:
                    if def_health > 0:
                        defender['count'] = int(def_health / unit['health'])
                    else :
                        defender['count'] = 0


        self.update_army(self.user_army, attacker)
        self.update_army(self.comp_army, defender)


    def update_army(self, army, com):
        for i in army:
            if i['name'] == com['name']:
                i = com

    def battle(self):
        j = 0
        i = 0

        attacker = self.user_army
        defender = self.comp_army

        print('*' * 40)

        pprint(self.user_army)
        pprint(self.comp_army)

        print('*' * 40)

        if attacker == []:
            print('You need create user Army!')
        else:
            while i < len(attacker) and j < len(defender) and attacker[i]['count'] > 0:
                self.fight(attacker[i], defender[j])

                if defender[j]['count'] == 0 :
                    j+=1
                else:
                    i+=1

            self.count_winner(self.user_army, self.comp_army)




    def count_winner(self, attacker, defender):
        attacker_count = 0
        defender_count = 0
        for i in attacker:
            attacker_count += i['count']

        if attacker_count == 0:
            print('Defender win!')

        for i in defender:
            defender_count += i['count']

        if defender_count == 0:
            print('Attaker win!')


    def read_data_2(self, file_name):
        data_list = []

        with open(file_name) as file:
            data_list = json.load(file)

        return data_list




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




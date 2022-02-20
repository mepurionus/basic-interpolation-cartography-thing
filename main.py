def ask_for_num(what):
    return float(input(f"Give the value of {what}: "))

class num:
    def __init__(self, num):
        self.num = num
    def give_num(self):
        return float(self.num)

class printing_stuff:
    def __init__(self, valueone, valuetwo, round):
        self.valueone = valueone
        self.valuetwo = valuetwo
        self.round = round
    def print_stuff(self):
        if self.round == 1:
            print(f"~{self.valueone} m in terrain = {self.valuetwo} mm on map")
        else:
            print(f"{self.valueone} m in terrain = {self.valuetwo} mm on map")

one = num(ask_for_num("first point [m - height]"))
two = num(ask_for_num("second point [m - height]"))
dist = num(ask_for_num("the distance on the map [mm - distance on map]"))

firstnumber = one.give_num()
secondnumber = two.give_num()

if firstnumber < secondnumber:
    firstnumber, secondnumber = secondnumber, firstnumber

difference = firstnumber - secondnumber

supplement = (int((int(firstnumber) - secondnumber)*100))/100
result = (int((dist.give_num() * (supplement)) / difference*1000))/1000

first = printing_stuff(round(difference), dist.give_num(), 1)
second = printing_stuff(supplement, result, 0)

first.print_stuff()
second.print_stuff()
input("Press ENTER to continue...")
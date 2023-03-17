import time
from random import randint
import functools
import operator

def log(fn):
    """log decorator"""

    def inner(*args, **kwargs):
        called_at = time.time()
        to_execute = fn(*args, **kwargs)
        ended_at = time.time()
        exec_time = ended_at - called_at
        sourceFile = open('machine.log', 'a+')
        print('(cmaxime)Running: {0:20} [ exec-time = {1} ]'.format(format_name(fn.__name__), format_time(exec_time)), file = sourceFile)
        sourceFile.close()
        return to_execute
    
    return inner

def format_time(exec_time):
    if (exec_time * 1000 > 1):
        exec_time = round(exec_time, 3)
        text = str(exec_time) + ' s'
    else:
        exec_time = round(exec_time * 1000, 3)
        text = f'{exec_time} ms'
    return text

def format_name(name):
    return functools.reduce(lambda u, v: u + ' ' + v, map(lambda t: t.capitalize(), name.split('_')))


class CoffeeMachine(object):
    water_level = 100
    
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False 

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
import sys 
d = {}

print(sys.getsizeof(d))

# techniques to solve the memory cache clearing is using __slots__ 


class Resistor:

    # slots helps to reduce the memory
    __slots__ = ['resistance_ohms', 'tolerance_percent', 'power_watts']

    def __init__(self, resistance_ohms, tolerance_percent, power_watts):
        self.resistance_ohms = resistance_ohms,
        self.tolerance_percent = tolerance_percent
        self.power_watts = power_watts


r10 = Resistor(10, 5, 0.25)


# print(sys.getsizeof(r10) + sys.getsizeof(r10.__dict__))

#space_calculating - use slots wisely.
 
# catch here is we cant dynamically add any more attributes to the class after invoking __slots__, and some buildin functions wont work eg: __dict__
# which throws AttributeError: 'Resistor' object has no attribute '__dict__'

r10.cost_dollars = 0.02

print(
sys.getsizeof(r10))


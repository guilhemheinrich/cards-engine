import math
import numpy

class Stack:

    def __init__(self, stack_number, entity_number):
        self.stack_number = stack_number
        self.entity_number = entity_number
        self.distributions = []
        self.distributions_weights = []

    def generate(self):
        self.__looper(self.entity_number, self.entity_number + 1, 0, [])
        self.distributions_weights = []
        for distribution in self.distributions:
            self.distributions_weights.append(self.__weight(distribution))

    def __looper(self, _range, previous, stack, buffer):
        if (stack == self.stack_number - 1):
            last_value  = _range
            _buffer = buffer.copy()
            _buffer.append(last_value)
            if (last_value > previous) or last_value == -1:
                return
            self.distributions.append(_buffer)
        else:
            for _ite in range(_range + 1):
                if (_ite > previous):
                    continue
                next_range = _range - _ite
                _buffer = buffer.copy()
                _buffer.append(_ite)
                self.__looper(next_range, _ite, stack + 1, _buffer)

    def weight(self, index):
        return self.distributions_weights[index]

    def __weight(self, distribution):
        n_array = numpy.array(distribution)
        unique, counts = numpy.unique(n_array, return_counts=True)
        total = 0
        cardinal = 1
        for item in counts:
            cardinal = cardinal * math.comb(5 - total, item)
            total += item
        return cardinal


    @property
    def total_weight(self):
        return sum(self.distributions_weights)
    

stack = Stack(5,14)
print(stack.generate())
print(stack.distributions)
print(stack.weight(2))
print(stack.total_weight)
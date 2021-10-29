class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def __init__(self):
        self.total = 0

    def divisorSum(self, n):
        for i in range(1,n):
            if n % i == 0:
                self.total = self.total+ i
        
        return self.total+n



n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
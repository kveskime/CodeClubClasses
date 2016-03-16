
# Interfaces


class ICalculator:
    @staticmethod
    def add(x, y):
        raise NotImplementedError

    @staticmethod
    def sub(x, y):
        raise NotImplementedError

    @staticmethod
    def mul(x, y):
        raise NotImplementedError

    @staticmethod
    def div(x, y):
        raise NotImplementedError


class IAdvancedCalculator:
    @staticmethod
    def pow(x, p):
        raise NotImplementedError

    @staticmethod
    def sqrt(x):
        raise NotImplementedError

    @staticmethod
    def fact(x):
        raise NotImplementedError


# Implementations

class Calculator(ICalculator):
    """^ Calculator Implements ICalculator Interface (should be made to be able to add, sub, mul and div)"""
    # ToDo Implement ICalculatorHere!


class AdvancedCalculator(Calculator, IAdvancedCalculator):
    """^ AdvancedCalculator inherits Calculator functionality (can add, sub, mul, and div just like a Calculator)
         AdvancedCalculator implements IAdvancedCalculator Interface (should be made able to pow, sqrt and fact)"""
    # ToDo Implement ICalculatorHere

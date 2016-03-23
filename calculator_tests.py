from unittest import TestCase
from calculator import ICalculator, IAdvancedCalculator, Calculator, AdvancedCalculator
# To run in commandline without IDE: python -m unittest


class CalculatorTestCase(TestCase):
    def _test_ICalculator(self, calc: ICalculator):
        """
        calc: ICalculator is a type hint. -> 'Hey, Python, calc should implement ICalculator, k?'

        This also helps IDEs to supply auto completion.
        """
        try:
            self.assertEqual(calc.add(5, 5), 10)
            self.assertEqual(calc.sub(5, 5), 0)
            self.assertEqual(calc.mul(5, 5), 25)
            self.assertEqual(calc.div(5, 5), 1)
        except NotImplementedError:
            print("You haven't implementer ICalculator in Calculator yet?")
            raise NotImplementedError

    def _test_IAdvancedCalculator(self, adv_calc: IAdvancedCalculator):
        try:
            self.assertEqual(adv_calc.pow(2, 2), 4)
            self.assertEqual(adv_calc.fact(2), 2)
            self.assertEqual(adv_calc.sqrt(4), 2)
        except NotImplementedError:
            print("You haven't implementer IAdvancedCalculator in AdvancedCalculator yet?")

    def test_calculator_functionality(self):
        calc = Calculator()
        self._test_ICalculator(calc)

    def test_advanced_calculator(self):
        adv_calc = AdvancedCalculator()
        self._test_ICalculator(adv_calc)
        self._test_IAdvancedCalculator(adv_calc)

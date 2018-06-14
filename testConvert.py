import unittest
from convert import Convert

class TestConvert(unittest.TestCase):

    # degrees_from, units_from, units_to, correct_result
    answers = [(-273.15, 'Kelvin', 'Celsius', -546.3),
        (0, 'Kelvin', 'Celsius', -273.15),
        (32, 'Kelvin', 'Celsius', -241.15),
        (100, 'Kelvin', 'Celsius', -173.15),
        (212, 'Kelvin', 'Celsius', -61.15),
        (-273.15, 'Kelvin', 'Fahrenheit', -951.34),
        (0, 'Kelvin', 'Fahrenheit', -459.67),
        (32, 'Kelvin', 'Fahrenheit', -402.07),
        (100, 'Kelvin', 'Fahrenheit', -279.67),
        (212, 'Kelvin', 'Fahrenheit', -78.07),
        (-273.15, 'Kelvin', 'Rankine', -491.67),
        (0, 'Kelvin', 'Rankine', 0.0),
        (32, 'Kelvin', 'Rankine', 57.6),
        (100, 'Kelvin', 'Rankine', 180.0),
        (212, 'Kelvin', 'Rankine', 381.6),
        (-273.15, 'Celsius', 'Kelvin', 0.0),
        (0, 'Celsius', 'Kelvin', 273.15),
        (32, 'Celsius', 'Kelvin', 305.15),
        (100, 'Celsius', 'Kelvin', 373.15),
        (212, 'Celsius', 'Kelvin', 485.15),
        (-273.15, 'Celsius', 'Fahrenheit', -459.67),
        (0, 'Celsius', 'Fahrenheit', 32.0),
        (32, 'Celsius', 'Fahrenheit', 89.6),
        (100, 'Celsius', 'Fahrenheit', 212.0),
        (212, 'Celsius', 'Fahrenheit', 413.6),
        (-273.15, 'Celsius', 'Rankine', 0.0),
        (0, 'Celsius', 'Rankine', 491.67),
        (32, 'Celsius', 'Rankine', 549.27),
        (100, 'Celsius', 'Rankine', 671.67),
        (212, 'Celsius', 'Rankine', 873.27),
        (-273.15, 'Fahrenheit', 'Kelvin', 103.622222222),
        (0, 'Fahrenheit', 'Kelvin', 255.372222222),
        (32, 'Fahrenheit', 'Kelvin', 273.15),
        (100, 'Fahrenheit', 'Kelvin', 310.927777778),
        (212, 'Fahrenheit', 'Kelvin', 373.15),
        (-273.15, 'Fahrenheit', 'Celsius', -169.527777778),
        (0, 'Fahrenheit', 'Celsius', -17.7777777778),
        (32, 'Fahrenheit', 'Celsius', 0.0),
        (100, 'Fahrenheit', 'Celsius', 37.7777777778),
        (212, 'Fahrenheit', 'Celsius', 100.0),
        (-273.15, 'Fahrenheit', 'Rankine', 186.52),
        (0, 'Fahrenheit', 'Rankine', 459.67),
        (32, 'Fahrenheit', 'Rankine', 491.67),
        (100, 'Fahrenheit', 'Rankine', 559.67),
        (212, 'Fahrenheit', 'Rankine', 671.67),
        (-273.15, 'Rankine', 'Kelvin', -151.75),
        (0, 'Rankine', 'Kelvin', 0.0),
        (32, 'Rankine', 'Kelvin', 17.7777777778),
        (100, 'Rankine', 'Kelvin', 55.5555555556),
        (212, 'Rankine', 'Kelvin', 117.777777778),
        (-273.15, 'Rankine', 'Celsius', -424.9),
        (0, 'Rankine', 'Celsius', -273.15),
        (32, 'Rankine', 'Celsius', -255.372222222),
        (100, 'Rankine', 'Celsius', -217.594444444),
        (212, 'Rankine', 'Celsius', -155.372222222),
        (-273.15, 'Rankine', 'Fahrenheit', -732.82),
        (0, 'Rankine', 'Fahrenheit', -459.67),
        (32, 'Rankine', 'Fahrenheit', -427.67),
        (100, 'Rankine', 'Fahrenheit', -359.67),
        (212, 'Rankine', 'Fahrenheit', -247.67)]

    def test_bad_units(self):
        c = Convert()
        self.assertFalse(c.convert('Foo','Bar',123))
        self.assertFalse(c.convert('Kelvin','Bar',456))
        self.assertFalse(c.convert('Foo','Fahrenheit',789))
        self.assertFalse(c.convert('Foo','Fahrenheit','abc'))
        self.assertFalse(c.convert(None,None,None))
        self.assertFalse(c.convert(False,False,False))

    def test_conversion(self):
        # floating point rounding
        def is_close(a, b, rel_tol=1e-09, abs_tol=0.0):
            return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

        # iterate through the test suite
        c = Convert()
        for test in self.answers:
            deg_from = test[0]
            units_from = test[1]
            units_to = test[2]
            correct_result = test[3]
            self.assertTrue(is_close(c.convert(units_from,units_to,deg_from),correct_result))
            # eliminate false positives where conversion is identity
            if deg_from != correct_result:
                self.assertFalse(is_close(c.convert(units_from,units_to,deg_from),deg_from))
       
if __name__ == '__main__':
    unittest.main()

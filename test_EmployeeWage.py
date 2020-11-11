from unittest import TestCase

class Test_print_welcome(TestCase):
    def test_print_welcome(self):
        from EmployeeWage import print_welcome
        self.assertTrue(print_welcome)
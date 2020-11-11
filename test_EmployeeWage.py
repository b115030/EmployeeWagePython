from unittest import TestCase

class Test_print_welcome(TestCase):
    def test_print_welcome(self):
        from EmployeeWage import print_welcome
        self.assertTrue(print_welcome)

    def test_check_attendance(self):
        from EmployeeWage import check_attendance
        self.assertTrue(check_attendance)
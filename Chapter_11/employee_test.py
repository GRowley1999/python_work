import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the Employee class."""

    def setUp(self):
        """
        Create an employee object for use in all test methods.
        """
        self.employee = Employee('Gregor', 'Rowley', 90000)
    
    def test_give_default_raise(self):
        """
        Tests that the default raise value is added to an employee's salary.
        """
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 95000)

    def test_give_custom_raise(self):
        """
        Tests that a custom raise can be applied to an employee's salary.
        """
        self.employee.give_raise(6000)
        self.assertEqual(self.employee.annual_salary, 96000)

unittest.main()
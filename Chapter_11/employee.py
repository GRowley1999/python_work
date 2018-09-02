class Employee():
    """A simple model of an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialise the attributes of the employee class."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary


    def give_raise(self, raise_amount=5000):
        """Applies a raise to an employee's salary."""
        self.annual_salary += raise_amount
"""A set of classes that represent an administrative user and their privileges."""

from users import Users

class Admin(Users):
    """A simple attempt to model an administrative user."""

    def __init__(self, first_name, last_name, age):
        """Initialize attributes of admin user."""
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()


class Privileges():
    """Models the privileges of an adminstrative user."""

    def __init__(self, privileges=[]):
        """Initializes the privilege attribute."""
        self.privileges = privileges

    def show_privileges(self):
        """Prints the administrators privileges."""
        print("The administrator has the following privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
            else:
                print("- This user has no privileges.")
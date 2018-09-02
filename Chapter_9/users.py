"""A class that can be used to represent a User."""

class Users():
    """A simple attempt to model a user."""

    def __init__(self, first_name, last_name, age):
        """Initialize first_name and last_name attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0
    
    def describe_user(self):
        """Prints a summary of a user's information."""
        full_name = self.first_name + ' '  + self.last_name
        print("Name: " + full_name + ".")
        print("Age: " + str(self.age))
    

    def greet_user(self):
        """Prints a greeting to a user."""
        full_name = self.first_name + ' ' + self.last_name
        print("Hello " + full_name .title() + ".")


    def increment_login_attempts(self):
        """Increments the number of login attempts by one."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the number of login to zero."""
        self.login_attempts = 0
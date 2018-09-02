from random import randint

class Die():
    """A simple attempt to model a die."""

    def __init__(self, sides=6):
        """Initialize sides attribute of die."""
        self.sides = sides

    def roll_die(self):
        """Print a random number between 1 and the number of sides the die has."""
        for value in range(1, 11):
            print(str(randint(1, self.sides)))

die = Die()
die.roll_die()
print("\n")
die = Die(20)
die.roll_die()
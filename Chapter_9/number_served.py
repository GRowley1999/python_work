class Restaurant():
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to represent a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """Give a description of a restaurant."""
        print("The restaurant is named: " + self.restaurant_name.title()  + 
            " and serves " + self.cuisine_type.title() + " cuisine.")
    

    def open_restaurant(self):
        """Print a message indicating that a restaurant is open."""
        print("The restaurant is open.")

    def set_number_served(self, number_of_served):
        """Set the number of customers served."""
        self.number_served = number_of_served


    def increment_number_served(self, number_of_served):
        """Increment the number of customers who have been served."""
        self.number_served += number_of_served


restaurant = Restaurant("Da Vinci's", "Italian")
print(str(restaurant.number_served))
restaurant.number_served = 23
print(str(restaurant.number_served))
restaurant.set_number_served(50)
print(str(restaurant.number_served))
restaurant.increment_number_served(50)
print(str(restaurant.number_served))
def make_shirt(size="large", message="I love Python"):
    """Prints the size of the t-shirt and the message to be printed on it."""
    print("\nSize of t-shirt: " + size.title() + "\nMessage: " + message.title() + 
        ".")

make_shirt("large")
make_shirt("medium")
make_shirt("small", "Hello Python world")
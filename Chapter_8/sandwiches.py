def build_sandwich(*items):
    """Print a summary of the toppings on a sandwich."""
    print("\nThis sandwich is filled with the following items:")
    for item in items:
        print("\t" + item.title())

build_sandwich('ham', 'mango chuteny', 'lettuce leaves', 'cherry tomatoes')
build_sandwich('chicken', 'chives', 'sweet chilli dressing')
build_sandwich('tuna', 'sweetcorn', 'mayo')
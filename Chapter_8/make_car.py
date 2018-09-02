def make_car(manufacturer, model_name, **car_properties):
    """Stores information about a car in a dictionary."""
    car_props = {}
    car_props['manufacturer'] = manufacturer
    car_props['model'] = model_name
    for key, value in car_properties.items():
        car_props[key] = value
    return car_props
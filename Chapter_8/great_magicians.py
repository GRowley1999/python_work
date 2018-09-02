magicians = ['erin', 'freya', 'gregor']

def show_magicians(magicians):
    """Prints the names contained in a list of magicians."""
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    """Adds the phrase 'the great' to the end of a magicians name."""
    for index, magician in enumerate(magicians):
        magicians[index] =  magician + " the Great"
    return magicians

show_magicians(make_great(magicians))
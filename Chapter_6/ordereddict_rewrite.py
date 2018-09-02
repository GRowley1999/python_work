from collections import OrderedDict

glossary = OrderedDict()
 
glossary = {
    'newline character' : 'signifies a new line, is to be taken in printed output.',
    'tab character' : 'signifies that space should be included in printed output.',
    'dicitonary' : 'data structure consisting of associated key-value pairs.',
    'list' : 'data structure which stores n values of a single data type.',
    'string' : 'a series of alphanumeric characters.'
}

for term, definition in glossary.items():
    first_letter = definition[0].upper()
    print(term.title() + " : " + first_letter + definition[1:])
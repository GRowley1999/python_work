favourite_languages = {
    'jen' : ['python', 'ruby'],
    'sarah' : ['c'],
    'edward' : ['ruby', 'go'],
    'phil' : ['python', 'haskell'],
    'gregor' : ['python', 'java', 'haskell'],
}

for name, languages in favourite_languages.items():
    if len(languages) == 1:
        print("\n" + name.title() + "'s favourite language is:")
        for language in languages:
            print("\t" + language.title())
    else:
        print("\n" + name.title() + "'s favourite languages are:")
        for language in languages:
            print("\t" + language.title())
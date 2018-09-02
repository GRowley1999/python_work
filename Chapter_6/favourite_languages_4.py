favourite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):
    print(language.title())
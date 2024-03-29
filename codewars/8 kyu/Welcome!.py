"""
Your start-up's BA has told marketing that your website has a large audience in Scandinavia and surrounding countries.
Marketing thinks it would be great to welcome visitors to the site in their own language. Luckily you already use an API
 that detects the user's location, so this is an easy win.

The Task
Think of a way to store the languages as a database (eg an object).
The languages are listed below so you can copy and paste!

Write a 'welcome' function that takes a parameter 'language' (always a string), and returns a greeting - if you have it
in your database. It should default to English if the language is not in the database, or in the event of an invalid input.
"""

d = {'english': 'Welcome',
'czech': 'Vitejte',
'danish': 'Velkomst',
'dutch': 'Welkom',
'estonian': 'Tere tulemast',
'finnish': 'Tervetuloa',
'flemish': 'Welgekomen',
'french': 'Bienvenue',
'german': 'Willkommen',
'irish': 'Failte',
'italian': 'Benvenuto',
'latvian': 'Gaidits',
'lithuanian': 'Laukiamas',
'polish': 'Witamy',
'spanish': 'Bienvenido',
'swedish': 'Valkommen',
'welsh': 'Croeso'}


def greet(language):
    # my solution
    # return d[language] if language in d else d['english']
    # solution using get() function
    return d.get(language, d['english'])


print(greet(2))
from pprint import pprint
# Input data
"""
+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+"""

TEXTS = ['''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

separator = "-" * len("Enter a number btw. 1 and 3 to select:  ")
users = ["bob", "ann", "mike", "liz"]
passwords = ["123", "pass123", "password123", "pass123"]

reg_users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}


# Entry username and password
username_vstup = input("USERNAME: ")
password_vstup = input("PASSWORD: ")
# Verification of the registered user
if username_vstup in reg_users.keys():
    print(separator)
    verification = reg_users.get(username_vstup)
    if password_vstup == verification:
        print(f"Welcome to the app, {username_vstup}")
        print("We have 3 texts to be analyzed.")
        print(separator)
    else:
        print("unregistred user, terminating the program...")
        quit()
else:
    print(separator)
    print("unregistred user, terminating the program...")
    quit()

# Entry number of the text
text_number = input("Enter a number btw. 1 and 3 to select: ")
print(separator)
if text_number.isnumeric() and int(text_number) in range(1, 4):
    text_index = int(text_number) - 1
    text = TEXTS[text_index]
elif text_number.isnumeric() and int(text_number) not in range(1, 4):
    print("Incorrect number of the text!")
    quit()
else:
    print("The input is not a number")
    quit()

# Text analysis
if int(text_number) in range(1, 4):
    text = TEXTS.copy()
    text_selection = TEXTS.pop(text_index)

# Number of words
    cleaned_words = []
    for word in text_selection.split():
        cleane_word = word.strip(",.:;'")
        cleaned_words.append(cleane_word)
        number_of_words = len(cleaned_words)
    print(f"There are {number_of_words} words in the selected text.")

# Number of capitalised words
    big_letters = []
    for letters in cleaned_words:
        if letters.istitle():
           big_letters.append(letters)
    print(f"There are {len(big_letters)} titlecase words.")
    #    velka_pismena = sum(map(str.istitle, text.split()))

# Number of uppercase words
    upper_words = []
    for words in cleaned_words:
        if words.isupper() and not words.startswith("30N"):
            upper_words.append(words)
    print(f"There are {len(upper_words)} uppercase words.")

# Number of lowercase words
    lower_words = []
    for words in cleaned_words:
        if words.islower():
            lower_words.append(words)
    print(f"There are {len(lower_words)} lowercase words.")

# Number of figures
    summary_figures = []
    for figures in cleaned_words:
        if figures.isnumeric():
            summary_figures.append(figures)
    print(f"There are {len(summary_figures)} numeric strings.")

# The sum of numbers
    summary_numbers = []
    for figures in summary_figures:
        i_numbers = int(figures)
        summary_numbers.append(i_numbers)
    print(f"The sum of all the numbers {sum(summary_numbers)}")
    print(separator,f"LEN|{'OCCURENCES:':^17}|NR.", separator, sep="\n")

# Chart
    length_words = {}
    for word in cleaned_words:
        length = len(word)
        if length not in length_words:
            length_words[length] = 1
        else:
            length_words[length] = length_words[length] + 1
        sor_keys = sorted(length_words.keys())
    for prvek in sor_keys:
        print(f"{prvek: >3}|{'*' * length_words.get(prvek):<17}|{length_words.get(prvek)}")


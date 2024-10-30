"""
projekt_1.py: první projekt od Engeto Online Python Akademie

autor: Karolína Dvořáková Machová
email: karolin.machova@gmail.com
discord: karolinamach
"""

# oddělovač, seznam (dict) registrovaných uživatelů a vložené texty
delim = "-" * 40
registred = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.''',
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


# úvod a vstupní hodnoty od uživatele
print("Input username:")
name = input()
print("Input password:")
password = str(input())                 # Může být jen číselné heslo.
user = (name, password)                 # Musíme obojí převést na tuple, ptž chceme porovnávat s .items(), který na něj převádí hodnoty dictu.

# ověření uživatele
if user not in registred.items():
    print("username:", name)
    print("password:", password)
    print(delim)
    print("Unregistered user or invalid password, terminating the program...")  # Já osobně bych mu dala další pokus
    exit(1)

# vlastní průběh programu
else:
    print("username:", name)
    print("password:", password)
    print(delim)
    print("Welcome to the app,", name)
    print("We have 3 texts to be analyzed.")
    print(delim)
    text_num = input("Enter a number btw. 1 and 3 to select: ")

    if text_num.isalpha():
        print("Input not numeric, terminating the program...")
        exit(2)
    elif int(text_num) not in range(1, 4):                     # Range kvůli potencionálnímu rozšiřování počtu textů.
        print("Invalid number, terminating the program...")
        exit(3)
        print(delim)

## příprava textu
text_num = int(text_num) - 1                         # Převedení zvoleného čísla na hodnotu indexu v listu.
texts_str = TEXTS[text_num].removeprefix("\n").removesuffix(".")

texts_str = texts_str.replace(". ", " " ).replace("\n", " ").replace(",", "").split(" ")

## počet slov v textu
word_count = (len(texts_str))
print("There are", word_count, "words in the selected text.")

## počet slov v textu jsou malými písmeny, jsou velkými písmeny nebo jen začínají velkým písmenem
is_lower = 0
is_upper = 0
is_title = 0
for word in texts_str:
    if word.islower():
        is_lower += 1
    elif word.isupper() and word.isalpha():
        is_upper += 1
    elif word.istitle():
        is_title += 1
    else:
        continue

print("There are", is_title, "titlecase words.")
print("There are", is_upper, "uppercase words.")
print("There are", is_lower, "lowercase words.")

## počet a součet všech čísel v textu
numbers = []                         # Sem se budou přidávat nalezené číselné výskyty.  
words_len = []                          # Bude zaznamenávat list délek slov pro graf.
for word in texts_str:
    word_len = 0                            # Reset délky slova.
    number = str()                           # Musí obsahovat hodnotu pro případ, že se nenajde žádné číslo k přičtení.
    for symbol in word:
        word_len += 1                           # Zaznamenává délku slova.
        if symbol.isalpha():                    # Když bude začínat písmenem, tak zrovna smyčku ukončíme a nepokračujeme v ověřování.
            continue
        elif word.isnumeric() and symbol.isnumeric():
            number += str(symbol)
        else:
            continue                                                      
    else:
        words_len.append(word_len)                      # Přidává délku slova do listu délek.
        number.join(number)                         # Dává další cifru do stringu čísla.
        if number != '' and number != '.':                         
            numbers.append(int(number))                       # Přidává další číslo do listu čísel.
        else:
            continue                       
                 
print("There are", len(numbers), "numeric strings.")
print("The sum of all numbers is", sum(numbers))



## graf
### list délek slov
unique = set(words_len)
words_len = list(words_len)              
counts = list()

### list výskytu jedinečných délek slov
for count in unique:
    count = words_len.count(count)
    counts.append(int(count))
else:
    counts= sorted(list(counts), reverse= True)

### vypsání grafu

graph_delim = "*"
print(delim)
print("LEN|" +  "OCCURENCES".center((counts[0]) + 2) +  "|NR.")             # Samozřemě limitující je délka slova occurences
print(delim)


for lenght in unique:
    count = (words_len.count(lenght))
    if lenght < 10:
        print( "".ljust(2), lenght, "|", graph_delim * count, "|".rjust((counts[0] + 3) - count), count, sep = "")
    elif lenght < 100:
        print("".ljust(1), lenght, "|", graph_delim * count, "|".rjust((counts[0] + 3) - count), count, sep = "")
    else:
        print("Extremely long words or text with a word separator other than space. Unable to create graph.")
        break

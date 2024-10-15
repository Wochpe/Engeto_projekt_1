Texts = [
    "Pokud si chceš vyzkoušet nabité znalosti, 1.2 nyní 12 máš¨' skvělou příležitost. Čeká na tebe první praktický projekt, kde si můžeš svoje dovednosti aplikovat.",
    "Soubor těchto pravidel pro čistý kód můžeš najít v 5 oficiální dokumentaci zde. Nicméně pravidel je tam více, než v tento 2 moment dovedeš uplatnit. Proto si nyní ukážeme ty nejpodstatnější.",
    "Python ti dovolí napsat mezery prakticky kdekoliv, 1 ale to neznamená, že je to 1 správně. Ukážeme ti nyní 1 několik variant."
]
## počet slov v textu
choice = int(input()) - 1
Texts_str = Texts[choice].split(" ")
word_count = (len(Texts_str))
print("There are", word_count, "words in the selected text.")

## počet slov v textu jsou malými písmeny, jsou velkými písmeny nebo jen začínají velkým písmenem
is_lower = 0
is_upper = 0
is_title = 0
for word in Texts_str:
    if word.islower():
        is_lower += 1
    elif word.isupper():
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
for word in Texts_str:
    word_len = 0                            # Reset délky slova.
    number = str()                           # Musí obsahovat hodnotu pro případ, že se nenajde žádné číslo k přičtení. To by pak nešlo převést na float.
    for symbol in word:
        word_len += 1                           # Zaznamenává délku slova.
        if symbol.isalpha():                    # Když bude začínat písmenem, tak ho zrovna vyřadíme a nepokračujeme v ověřování, jinak by byla tečka problém.
            continue
        elif symbol.isnumeric() or symbol == ".":
            number += str(symbol)
        else:
            continue                                                      
    else:
        words_len.append(word_len)                      # Přidává délku slova do listu délek.
        number.join(number)                         # Dává další cifru do stringu čísla.
        if number != '' and number != '.':                         
            numbers.append(float(number))                       # Přidává další číslo do listu čísel. Float kvůli následnému sečtení.
        else:
            continue                       
                 
print("There are", len(numbers), "numeric strings.")
print("The sum of all numbers is", sum(numbers))

# graf
## list délek slov
unique = set(words_len)
words_len = list(words_len)              
counts = list()

## list výskytu jedinečných délek slov
for count in unique:
    count = words_len.count(count)
    counts.append(int(count))
else:
    counts= sorted(list(counts), reverse= True)

## vypsání grafu
graph_delim = "*"
for lenght in unique:
    count = (words_len.count(lenght))
    if lenght < 10:
        print( "".ljust(1), lenght, "|", graph_delim * count, "|".rjust((counts[0] + 3) - count), count, sep = "")
    elif lenght < 100:
        print(lenght, "|", graph_delim * count, "|".rjust((counts[0] + 3) - count), count, sep = "")
    else:
        print("Extremely long words or text with different separator than ' '. Terminating program...")
        break

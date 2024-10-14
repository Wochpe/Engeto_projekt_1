Texty = [
    "Pokud si chceš vyzkoušet nabité znalosti, 1.2 nyní 12 máš¨' skvělou příležitost. Čeká na tebe první praktický projekt, kde si můžeš svoje dovednosti aplikovat.",
    "Soubor těchto pravidel pro čistý kód můžeš najít v 5 oficiální dokumentaci zde. Nicméně pravidel je tam více, než v tento 2 moment dovedeš uplatnit. Proto si nyní ukážeme ty nejpodstatnější.",
    "Python ti dovolí napsat mezery prakticky kdekoliv, 1 ale to neznamená, že je to 1 správně. Ukážeme ti nyní 1 několik variant."
]

vyber = int(input()) - 1
pocet_slov = Texty[vyber].split(" ")
print(len(pocet_slov))

is_upper = 0
is_lower = 0
for slovo in pocet_slov:
    if slovo.istitle():
        is_upper += 1
    else:
        is_lower += 1
hodnota_textu = 0.0
delky_slov = []
for slovo in pocet_slov:
    delka_slova = 0
    cislo = str(0)                  # Musí obsahovat hodnotu pro případ, že se nenajde žádné číslo k přičtení. To by nešlo převést na float pak.
    for znak in slovo:
        delka_slova += 1           
        if znak.isalpha():
            continue                        
        elif znak.isnumeric() or znak == ".":
            cislo += str(znak)
        else:
            continue                               
    else:
        delky_slov.append(delka_slova)
        cislo.join(cislo)
        hodnota_textu += float(cislo)
print(hodnota_textu)
print(is_upper, is_lower)


# graph
## list délek slov
jedinecne = set(delky_slov)               
delky_slov = list(delky_slov)
pocty = list()

## list výskytu jedinečných délek slov
for pocet in jedinecne:
    pocet = delky_slov.count(pocet)
    pocty.append(int(pocet))
else:
    pocty= sorted(list(pocty), reverse= True)

## vypsání grafu
graph_delim = "*"
for delka in jedinecne:
    count = (delky_slov.count(delka))
    if delka < 10:
        print( delka, "|", graph_delim * count, "|".rjust((pocty[0] + 4) - count), count, sep= "")
    elif delka < 100:
        print( delka, "|", graph_delim * count, "|".rjust((pocty[0] + 3) - count), count, sep= "")
    else:
        print("Extremely long words or text with different separator than ' '. Terminating program...")
        break


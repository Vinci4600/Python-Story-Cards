#Main Seite mit Wilkommen
from random import choice
import spuk_im_schloss

print(r'''_____
         |A .  | _____
         | /.\ ||A ^  | _____
         |(_._)|| / \ ||A _  | _____
         |  |  || \ / || ( ) ||A_ _ |
         |____V||  .  ||(_'_)||( v )|
                |____V||  |  || \ / |
                       |____V||  .  |
                              |____V|
''')
print("Wilkommen bei StoryCards" )
storycards = input('Welches Spiel möchten Sie spielen? "1. Spuk im Schloss" oder "2. Das Verschollene Diadem": ')

if storycards == "1":
    print("Willkommen beim Spiel Spuk im Schloss")
    spuk_im_schloss.start()
elif storycards == "2":
    print("Willkommen beim Spiel Das Verschollene Diadem")
else:
    print("Ungültige Eingabe! Bitte wähle 1 oder 2.")


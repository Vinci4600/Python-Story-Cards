#Main Seite mit Wilkommen
from random import choice
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
storycards = input('Welches Spiel möchten Sie spielen? "1. Spuk im Schloss"oder"2. Das Verschollene Diadem"')
if storycards == "1":
    print("Wilkommen beim Spiel Spuck im Schloss ")
else :
    print("Wilkommen im Spiel das Verschollene Diadem ")


import textwrap

print(r'''           /---\
                    /     \
                   |  ## ##|
                /---|   |  |---\
               |    +------+    |
               |    | ???  |    |
               |    +------+    |
                \              /
                 \  /\  /\  /-/
                  \/  \/  \/
                   *
                  / \
                 /___\
                  | |
                 /   \
                /     \
               /       \
              /_________\
              |         |
              |   0 0   |
      *       |   | |   |       *
     / \     /|         |\     / \
    /___\   / |   0 0   | \   /___\
     | |   /  |   | |   |  \   | |
    /   \ /___|____ ____|___\ /   \
   /     \|___|    |    |___|/     \
  /       \   |____|____|   /       \
 /_________\  |    |    |  /_________\
 |         |--|____|____|--|         |
 |   0 0   |  |         |  |   0 0   |
 |   | |   |__|         |__|   | |   |
 |        /   |\___/\___/|   \        |
 |       /    |          |    \       |
 |      /  o  |  ||||||  |  o  \      |
 |     /   |  |  ||||||  |  |   \     |
 |    /    o  |  ||||||  |  o    \    |
 |___/     |  |__||||||__|  |     \___|
           o                o
_______________________________________''')

print("\n" + "=" * 55)
print("              SPUK IM SCHLOSS")
print("=" * 55 + "\n")

# Vorspann
vorspann = '''Wie alles begann …" Eigentlich wollten wir, Justus, Peter und Bob, den Tag am Strand verbringen, aber es kam alles anders. Wir trafen uns in unserem Geheimversteck, der Kaffeekanne. Und dort machte Bob eine Entdeckung: Jemand hatte an der Einstiegsklappe des stillgelegten Wassertanks eine gruselige Botschaft hinterlassen. Auf einem Zettel war mit blutroter Schrift geschrieben: "Hilfe! Ich bin gefangen. Gefangen im alten Schloss. Bitte helft mir!" Klar, dass wir uns sofort auf den Weg machten, 
denn Detektive helfen, wo sie können.
Schließlich sind wir die drei ???.
Wir kannten das alte Schloss. Vor vielen
Jahren war es unweit von Rocky Beach für
Aufnahmen zu einem Gruselfilm gebaut
worden. Auf dem Weg dorthin zogen sich über
unseren Köpfen dunkle Wolken zusammen
und es wurde unangenehm kühl. Düster und
verlassen lag das alte Spukschloss kurz darauf vor uns: Krähen kreisten über den
spitzen Zinnen der schiefen Türme und ihr
Krächzen ließ uns erschaudern. Oder waren
es etwa Schreie? Vorsichtig betraten wir
die wackelige Zugbrücke, die über einen
Burggraben ins Schloss führte. Plötzlich gab
es einen mächtigen Ruck und die Brücke
begann hochzuklappen. Panisch klammerten
wir uns aneinander, doch das half nichts.
Es war unmöglich, sich festzuhalten. Wie auf
einer steilen Rutsche rasten wir in die Tiefe
und landeten unsanft auf hartem Steinboden.
Was war geschehen? Plötzlich hörten wir ein
heiseres Röcheln, das uns das Blut in den
Adern gefrieren ließ. Dazu mischte sich das Rasseln von schweren Ketten. Gab es hier
etwa Geister? Das Röcheln verwandelte sich
in eine Stimme – rau und tief und gruselig:
„Willkommen auf Schloss Gruselberg. Ihr seid
gefangen in meinem Reich der Finsternis.
Die Mauern des Spukschlosses lassen keine
Seele frei. Es gibt nur einen Weg, meiner
magischen Macht zu entkommen: Stellt euch
den 1000 Gefahren, die in meinem Schloss
lauern! Überwindet Fallen und unlösbare
Rätsel! Entkommt meinen Wächtern des
Schreckens! Lange hat es hier noch niemand
ausgehalten, ha, ha, ha, ha!“
Jetzt wussten wir, was geschehen war: Der Hilferuf sollte uns nur in das Spukschloss
locken. Wir selbst waren jetzt die Gefangenen!
Und es gab nur ein Ziel: Wir mussten den
Gefahren trotzen, die hier lauerten, denn
echte Detektive kennen keine Angst!
Wir begannen, uns umzusehen, obwohl Peter
schon am ganzen Leib zitterte. Langsam
konnten wir erkennen, wo wir uns befanden …'''

print(textwrap.fill(
    vorspann,
    width=70,
    initial_indent="    ",
    subsequent_indent="    "
))

print("\n" + "-" * 55)
print("                    BEGINN")
print("-" * 55)
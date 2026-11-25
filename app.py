from flask import Flask, request

app = Flask(__name__)

TEXT_AFISAT = """=== VARIANTA 3 (POZELE 1-2) ===

1. GRILA (1-9):
1.b (erguri)
2.b (talveg)
3.d (pluviodenudare)
4.b (argila)
5.a (abraziune)
6.b (Amazon) / a (Mississippi)
7.c (reactiilor chimice dintre apa si roci)
8.c (180-200 m)
9.a (sedimentare)

2. ASOCIERE COLOANA A - B:
1. roci magmatice -> e (bazalt), f (sienit)
2. roci sedimentare -> b (gresie), d (creta)
3. roci metamorfice -> a (marmura), c (grafit)

3. SCHEMA VULCAN (pct. 3):
a) Reprezinta: vulcan / activitate vulcanica / eruptie vulcanica
b) Parti componente (1-4):
   1. Camera magmatica / vatra vulcanica
   2. Cos vulcanic / canal de alimentare
   3. Crater
   4. Con vulcanic / curgere de lava
c) 2 zone/regiuni afectate: Cercul de Foc al Pacificului, Islanda / Hawaii / Italia

5. VULCANISM / MAGMATISM EFUZIV (pct. 5):
a) Reprezinta: un vulcan / activitate vulcanica
b) Magmatism efuziv: iesirea magmei la suprafata (sub forma de lava) prin crapaturi/fracturi ale scoartei terestre si racirea rapida la suprafata
c) Parti componente (1-4):
   1. Camera magmatica / vatra vulcanica
   2. Cos vulcanic
   3. Con vulcanic
   4. Crater / lava
d) 2 zone/regiuni (atlas pag. 4-5): Cercul de Foc al Pacificului, Islanda / Hawaii / Mediterana

6. TABEL TIPURI DE RELIEF:
- Stanga (Relief eolian):
  * Tip relief: Relief eolian
  * Agent: Vantul
  * Procese: eroziune eoliana (coraziune, deflatie), transport si acumulare eoliana
  * Forme (min. 2): dune de nisip, barkane, yardanguri
  * Raspandire: deserturi (Sahara, Gobi, Arabia)
- Dreapta (Relief carstic):
  * Tip relief: Relief carstic
  * Agent: Apa (ape subterane / carstice / de infiltratie)
  * Procese: dizolvarea (coroziunea), precipitarea, prabusiri/eroziune carstica
  * Forme (min. 2): pesteri, stalactite, stalagmite, doline, avene
  * Raspandire: Pestera Ursu (Romania), regiuni calcaroase (Alpii Dinarici, Carpati)

7. ALUNECARI DE TEREN:
1a) Cauza naturala: precipitatii abundente / topirea brusca a zapezilor / cutremure / pante inclinate si roci argiloase-marnoase
1b) Cauza antropica: defrisari / constructii sau terasamente pe pante / irigatii excesive / suprapasunat
2a) Consecinta mediul natural: degradarea solurilor, distrugerea vegetatiei, modificarea reliefului, bararea cursurilor de apa
2b) Consecinta societatea umana: distrugerea caselor, drumurilor, cailor ferate si terenurilor agricole, pagube economice
3) Masura prevenire/combatere: impaduriri / plantarea vegetatiei pe versanti / drenajul apelor / terasarea pantelor


=== VARIANTA 4 (POZELE 3-4) ===

1. GRILA (1-7):
1.c (200-300 m)
2.d (pluviodenudare)
3.b (rigole)
4.c (reactiilor chimice dintre apa si roci)
5.a (sedimentare)
6.d (Verhoianse, Caucaz)
7.b (asocieri de falii)

2. COMPLETARE SPATII:
- Mantaua incepe sub: scoarta terestra (crusta)
- se extinde pana la adancimea de: 2900 km
- Placa formata doar din crusta oceanica are grosimea de: 5-12 km
- asemanatoare ca structura este placa: oceanica (litosferica oceanica)
- In cadrul crustei oceanice lipseste patura: granito-metamor fica (granitica)
- Corpuri naturale formate in rezultatul combinarii elementelor chimice se

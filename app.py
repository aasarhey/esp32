from flask import Flask, request

app = Flask(__name__)

TEXT_AFISAT = """=== VARIANTA II (PRIMUL TEST) ===

I. CUNOASTERE SI INTELEGERE
1.1: a (30-80 km)
1.2: c (2900 km)
1.3: b (rigole)
1.4: b (siroire)
1.5: c (mine, halde)

2. COMPLETARE TERMENI:
- contact de tip: convergent
- placa (oceanica) coboara sub cea continentala
- impinsa din zona de: rift
- suprafata inclinata: planul Benioff
- asimilata in: astenosfera
- procesul: subductie (subductia plitelor)
- ramurile descendente ale: curenti subcrustali
- provoaca: cutremure de pamant
- hipocentru la 300-700 km: adancime
- alte fenomene: vulcanism, fose oceanice, formarea muntilor cutati

3. ADEVARAT / FALS:
- AF1: F -> biochimice = biofizice / mecanice (sau fizice)
- AF2: A
- AF3: F -> Ravenele = Rigolele
- AF4: F -> Rocile sedimentare = Rocile eluviale / deluviale (sau alterarea)

4. MISCARI TECTONICE:
- Oscilatorii: ridicare/coborare lenta, de amploare mica pe arii vaste; ex: Pen. Scandinavica, Scotia, Uralul de Nord
- Cute (orogenice de cutare): deformarea straturilor, anticlinale/sinclinale; ex: munti cutati (Alpi, Carpati, Himalaya)

5. CLASIFICARE RELIEF:
- Forme planetare: Continentul Africa, Oceanul Arctic
- Forme majore: Podisul Tibet, Groapa Marianelor
- Mezoforme de relief: Cheile Bicazului, Marele Canion Colorado

II. APLICARE SI OPERARE
6. DESFASURAREA CHINEI (40 lat. N, 1 = 85,4 km):
- Longitudini aprox. (harta Asiei p. 46-47): ~73E - ~135E (diferenta ~62 long.)
- Distanta in grade: ~62
- Distanta in km: 62 * 85,4 km ≈ 5294,8 km (variaza usor in functie de citirea exacta de pe harta, ±2 la longitudine)

7. TEMPERATURA IN SCOARTA (2610 m, strat izoterm +24C):
- a. Gradient geotermic: 100 m = ~3C (verifica valoarea din manualul tau)
- b. Crestere temperatura pe 2610 m: (2610 / 100) * 3C = 26,1 * 3C = +78,3C
- c. Temperatura la 2610 m: 24C + 78,3C = +102,3C

8. ANALIZA IMAGINII (COLIZIUNE CONTINENTALA / SUBDUCTIE):
- a. Procesul: coliziune continentala / subductie
- b. Plite litosferice: placa continentala si placa oceanica (litosfera continentala / oceanica)
- c. Regiune exemplu: Himalaya / Anzi / Alpi
- d. 3 fenomene asociate: cutremure de pamant, vulcanism, formarea muntilor (orogeneza)

III. INTEGRARE - CUTREMURE
1a. Cauza naturala: miscarile placilor litosferice / activitatea tectonica
1b. Cauza antropica: exploatari miniere / baraje mari / extractii sau injectii in subsol / teste nucleare


=== VARIANTA 3 (POZELE 1-2) ===

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
- Corpuri naturale formate in rezultatul combinarii elementelor chimice se numesc: roci / minerale
- Miscarile orogenice de cutare au dat nastere unitatilor de relief numite: munti cutati
- Procesul de largire a fundului oceanic se numeste: expansiune oceanica (spreading / riftogeneza)
- caracteristic in prezent oceanului: Atlantic / Pacific

3. ANALIZA SCHEMEI (Fig. 1 - curenti de convectie / astenosfera):
a) Procesul in zona (a): subductie / convergenta placilor litosferice (sau rift/divergenta in functie de sageti)
b) Descriere: coborarea unei placi litosferice sub alta placa in astenosfera, insotita de topire partiala si tensiuni tectonice
c) 3 procese/fenomene asociate: cutremure de pamant, vulcanism, metamorfism / formarea muntilor
d) Forme de relief rezultate: fose oceanice, munti cutati / arcuri insulare vulcanice

4. CLASIFICARE ROCI SEDIMENTARE:
- Tipul: detritice -> 1. nisip, 2. argila
- Tipul: chimice -> 1. sare gema, 2. ghips
- Tipul: organogene -> 1. carbune, 2. calcar

3. TABEL (poza 4 - relief carstic vs relief glaciar):
- Stanga (Relief carstic):
  * Tip relief: Relief carstic
  * Agent: Apa (ape subterane / carstice / de infiltratie)
  * Procese: dizolvarea rocilor solubile/usor solubile, precipitarea
  * Forme (min. 2): pesteri, doline, avene, stalactite, stalagmite
  * Raspandire: In zonele subtropicale, temperate: Romania, Moldova (podis, platou)
- Dreapta (Relief glaciar):
  * Tip relief: Relief glaciar
  * Agent: Gheata / ghetarii
  * Procese: eroziunea glaciara (exaratie, smulgere, abraziune glaciara), transport si acumulare glaciara
  * Forme (min. 2): circuri glaciare, vai glaciare, morene, custuri
  * Raspandire: munti inalti (Alpi, Carpati, Himalaya, Anzi) si regiuni polare

4. MUNTII ANZI:
a) Pozitia geografica: vestul Americii de Sud (de-a lungul tarmului Oceanului Pacific)
b) Directia generala de desfasurare: nord-sud (N-S)
c) Varsta muntilor: tineri (orogeneza alpina / neozoica)
d) Geneza muntilor: miscari orogenice de cutare / subductia placii Nazca sub placa Sud-Americana + vulcanism
e) Coordonatele varfului Aconcagua: ~3239' lat. Sud, ~7001' long. Vest

ALUNECARI DE TEREN (algoritm de jos):
1a) Cauza naturala: precipitatii abundente / topirea brusca a zapezilor / cutremure / pante inclinate si roci argiloase
1b) Cauza antropica: defrisari / constructii sau terasamente pe pante / irigatii excesive / suprapasunat
"""


@app.route('/health', methods=['GET'])
def health_check():
    return "OK", 200


@app.route('/upload', methods=['POST'])
def upload():
    _ = request.data
    return TEXT_AFISAT, 200, {"Content-Type": "text/plain; charset=utf-8"}


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        threaded=True
    )

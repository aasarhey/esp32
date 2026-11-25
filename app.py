from flask import Flask, request

app = Flask(__name__)

TEXT_AFISAT = """TEST LITOSFERA - VAR. II

I. CUNOAȘTERE ȘI ÎNȚELEGERE
1.1: a (30-80 km)
1.2: c (2900 km)
1.3: b (rigole)
1.4: b (șiroire)
1.5: c (mine, halde)

2. COMPLETARE TERMENI:
- contact de tip: convergent
- placa (oceanică) coboară sub cea continentală
- împinsă din zona de: rift
- suprafață înclinată: planul Benioff
- asimilată în: astenosferă
- procesul: subducție (subducția plitelor)
- ramurile descendente ale: curenți subcrustali
- provoacă: cutremure de pământ
- hipocentru la 300-700 km: adâncime
- alte fenomene: vulcanism, fose oceanice, formarea munților cutați

3. ADEVĂRAT / FALS:
- AF1: F -> biochimice = biofizice / mecanice (sau fizice)
- AF2: A
- AF3: F -> Ravenele = Rigolele
- AF4: F -> Rocile sedimentare = Rocile eluviale / deluviale (sau alterarea)

4. MIȘCĂRI TECTONICE:
- Oscilatorii: ridicare/coborâre lentă, de amploare mică pe arii vaste; ex: Pen. Scandinavică, Scoția, Uralul de Nord
- Plictisitoare/Cute (orogenice de cutare): deformarea straturilor, anticlinale/sinclinale; ex: munți cutați (Alpi, Carpați, Himalaya)

5. CLASIFICARE RELIEF:
- Forme planetare: Continentul Africa, Oceanul Arctic
- Forme majore: Podișul Tibet, Groapa Marianelor
- Mezoforme de relief: Cheile Bicazului, Marele Canion Colorado

II. APLICARE ȘI OPERARE
6. DESFĂȘURAREA CHINEI (40° lat. N, 1° = 85,4 km):
- Longitudini aprox. (harta Asiei p. 46-47): ~73°E - ~135°E (diferență ~62° long.)
- Distanța în grade: ~62°
- Distanța în km: 62 * 85,4 km ≈ 5294,8 km (variază ușor în funcție de citirea exactă de pe hartă, ±2° la longitudine)

7. TEMPERATURA ÎN SCOARȚĂ (2610 m, strat izoterm +24°C):
- a. Gradient geotermic: 100 m = ~3°C (valoare medie standard; verifică valoarea din manualul tău)
- b. Creștere temperatură pe 2610 m: (2610 / 100) * 3°C = 26,1 * 3°C = +78,3°C
- c. Temperatura la 2610 m: 24°C + 78,3°C = +102,3°C

8. ANALIZA IMAGINII (COLIZIUNE CONTINENTALĂ / SUBDUCȚIE):
- a. Procesul: coliziune continentală / subducție
- b. Plite litosferice: placă continentală și placă oceanică (litosferă continentală / oceanică)
- c. Regiune exemplu: Himalaya / Anzi / Alpi
- d. 3 fenomene asociate: cutremure de pământ, vulcanism, formarea munților (orogeneză)

III. INTEGRARE - CUTREMURE
1a. Cauză naturală: mișcările plăcilor litosferice / activitatea tectonică
1b. Cauză antropică: exploatări miniere / baraje mari / extracții sau injecții în subsol / teste nucleare
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
    

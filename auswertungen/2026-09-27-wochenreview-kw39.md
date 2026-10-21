# Wochenreview KW39

- **Datum:** 2026-09-27
- **Art:** Wochenreview
- **Zeitraum:** 2026-09-07 bis 2026-09-27 (21-Tage-Fenster); Auswertungswoche KW39 = 21.-27.09., Vergleich KW38 14.-20.09. und KW37 07.-13.09.

> **Kurzfazit:** Die Sicherheitsfrage aus KW37 ist beantwortet: die Muskelmasse steigt (66,04 -> 66,48 -> 66,64 kg), es gibt keinen zweiten fallenden Zeitraum, das Defizit bleibt bei 400 kcal. Dafuer ist die eine Anpassung aus KW37 klar gescheitert: an 4 von 6 vollstaendigen Tagen lag Protein unter der Untergrenze von 151 g (121 / 142,3 / 138,4 / 118 g), Ø 143,5 g statt 175 g - schlechter als in KW37. Dazu Ø 2.037 kcal statt 2.250, also ein tatsaechliches Defizit von 613 kcal (23,1 % des angenommenen TDEE) und drei Tage unter dem Grundumsatz (20., 21., 23.09.). Erstmals existiert ein echter gleitender 7-Tage-Schnitt (21.-27.09.: 83,49 kg), er liegt aber gleichauf mit dem KW38-Blockmittel (83,49 kg) - zwei Wochen flaches Gewicht bei rund 2.200 kcal. Die TDEE-Korrektur ist zum vierten Mal gesperrt (KW38 hat nur 4 trendtaugliche Wiegungen); ab 04.10. ist sie erstmals rechenbar. Training: 80 Arbeitssaetze, hoechstes Volumen der drei Wochen, aber Zug- und Beinseite wieder verfehlt (Lat 8, Ruecken 6, hintere Schulter 4, Beine 3, Unterarme 0) und Bizeps mit 14 Saetzen ueber dem Ziel von 4-10. Seitheben laeuft die sechste Woche mit 5 kg. Die eine Anpassung fuer KW40: ein fest eingeplanter Standard-Shake pro Tag (40 g / 180 kcal) - das hebt Ø Protein auf 183,5 g, den schlechtesten Tag auf 158 g und Ø kcal auf 2.217. Merkzettel: null offene Zeilen. REGELN.md v1.14 -> v1.15. Fuer KW38 war kein Review angelegt, STAND.md stand noch auf dem 13.09.

*Aus Notion übernommen am 2026-10-21. Historisches Dokument — Regeln und Zahlen darin können überholt sein.*

---

## 0. Rahmen und Datenlage

Review laeuft am Sonntag, 27.09.2026, 17:47 UTC (KW39). Datenquelle: Notion, Tabellen Gewicht / Ernaehrung / Training, Zeitraum per WHERE auf 07.09.-27.09. begrenzt (21 Tage). Zeilen mit `Notiz LIKE 'UNGUELTIG%'` ausgeschlossen. Rechnungen mit Python/pandas.

**Zwei Vorbemerkungen, die zur Einordnung gehoeren:**

1. **Fuer KW38 wurde kein Wochenreview angelegt.** Die letzte Seite in „Auswertungen" ist KW37 vom 13.09. `STAND.md` stand entsprechend noch auf dem Stand vom 13.09., waehrend `REGELN.md` laufend bis v1.14 (26.09.) weitergepflegt wurde. Dieses Review deckt deshalb zwei Wochen ab, und alle Woche-zu-Woche-Vergleiche sind hier zum ersten Mal gezogen.
2. **Der laufende Tag (27.09.) zaehlt nicht als Esstag** (REGELN §8). Er ist in den Rohdaten ausgewiesen, aber nicht in den Ø-Werten der Woche.

**Nicht trendtauglich und aus allen Trend- und TDEE-Rechnungen ausgeschlossen:** die Wiegung vom 20.09.2026 (84,05 kg, 09:19, nicht nuechtern, Trinkabend davor) — so bereits in ihrer eigenen `Notiz` vermerkt. Sie traegt kein `UNGUELTIG`, rutscht also durch den SQL-Filter und musste manuell herausgenommen werden.

---

## 1. Ernaehrung — Ø-Werte

| Woche | n Tage | Ø kcal | Ø Protein | Ø KH | Ø Fett | Ø Ballast | Ø Zeilen/Tag |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KW37 (07.-13.09.) | 7 | 2.165 | 142,0 g | 164,4 g | 92,4 g | 20,0 g | 8,9 |
| KW38 (14.-20.09.) | 7 | 2.310 | 142,6 g | 193,3 g | 95,1 g | 22,3 g | 10,0 |
| **KW39 (21.-26.09., vollstaendige Tage)** | **6** | **2.037** | **143,5 g** | **154,5 g** | **90,3 g** | **21,3 g** | **10,2** |

Laufender Tag 27.09. (nicht mitgezaehlt): 2.142 kcal, 119,6 g Protein, 9 Zeilen.

*Anmerkung zur KW37-Zeile: das Review vom 13.09. nannte Ø 2.208 kcal / 150,9 g Protein ueber 6 vollstaendige Tage. Hier stehen 7 Tage inkl. des damals laufenden 13.09. (1.908 kcal, 88,9 g Protein), deshalb der niedrigere Wert. Kein Widerspruch, andere Basis.*

**Rechenweg KW39 (6 Tage):**

```
kcal    (1500 + 2665 + 1771 + 2261 + 2102 + 1925) / 6 = 12224 / 6 = 2037,3
Protein (121,0 + 179,3 + 162,2 + 142,3 + 138,4 + 118,0) / 6 = 861,2 / 6 = 143,53
```

**Anteil `Geschaetzt = __YES__` in KW39: 63,9 %** (39 von 61 Zeilen) — deutlich ueber der 40-%-Schwelle aus REGELN §8.2. **Vorbehalt zur Datenqualitaet gilt.** In KW38 lag der Anteil bei 84,3 %, in KW37 bei 61,3 %; das Niveau von KW37 wurde also gehalten, aber nicht verbessert. Dazu die Verzerrung aus REGELN §4: bei Unsicherheit wird bewusst nach oben gerundet, die kcal-Summen sind also **systematisch nach oben verzerrt** — das echte Defizit ist eher groesser als hier berechnet, nicht kleiner.

**Zwei Tage mit auffaellig wenigen Zeilen** (REGELN §4, Richtwert 10-11): 26.09. mit 6 Zeilen (1.925 kcal, 118 g Protein) und 20.09. mit 7 Zeilen (651 kcal, 19,7 g Protein). Der 20.09. ist mit 651 kcal keine Messung, sondern eine Luecke mit ein paar Zeilen darin — er wird als Untererfassung behandelt und nicht als vollwertiger Esstag gewertet.

---

## 2. Gewicht und Koerperanalyse

### Erstmals ein echter gleitender 7-Tage-Durchschnitt

21.-27.09. sind **sieben lueckenlose Morgenmessungen** — das erste Mal in der ganzen Reihe.

```
(83,95 + 83,75 + 83,55 + 83,40 + 83,85 + 83,35 + 82,60) / 7 = 584,45 / 7 = 83,49 kg
```

Es gibt damit **einen** echten 7-Tage-Schnitt, aber noch keinen zweiten zum Vergleich — also weiterhin keinen gleitenden Trend. Der Woche-zu-Woche-Vergleich bleibt ein **Blockmittel** (REGELN §5).

| Woche | trendtaugl. Wiegungen | Blockmittel Gewicht | Ø Muskelmasse | Ø KFA (Rohwert) | Ø Koerperwasser | Ø Fettmasse |
| --- | --- | --- | --- | --- | --- | --- |
| KW37 | 5 | 84,02 kg | 66,04 kg | 15,76 % | 61,74 % | 13,24 kg |
| KW38 | 4 (20.09. raus) | 83,49 kg | 66,48 kg | 14,72 % | 62,50 % | 12,33 kg |
| KW39 | 7 | 83,49 kg | 66,64 kg | 14,47 % | 62,70 % | 12,07 kg |

**KW38 → KW39: 83,488 → 83,493 kg = +0,005 kg = +0,01 %/Woche.** Das Gewicht steht. Die 0,6-%-Grenze ist nicht gerissen — nicht weil es knapp war, sondern weil sich nichts bewegt hat.

Innerhalb der Woche sieht das anders aus: 83,95 kg (21.09.) auf 82,60 kg (27.09.) sind −1,35 kg in sechs Tagen. **Das ist kein Trend, sondern die Spannweite der Reihe** — der 27.09. ist der niedrigste Einzelwert ueberhaupt und faellt mit dem hoechsten Koerperwasser-Wert der Reihe zusammen (63,3 %). Einzelwerte werden nach REGELN §5 nicht kommentiert.

### Muskelmasse — die entscheidende Frage aus KW37 ist beantwortet

```
KW37 66,040 kg -> KW38 66,475 kg (+0,435) -> KW39 66,643 kg (+0,168)
```

In KW37 war **ein** fallender Zeitraum verzeichnet (66,23 → 66,04 kg), und REGELN §3 sieht vor: fallende Muskelmasse ueber **zwei** Zeitraeume → Defizit sofort auf 300 kcal. **Der zweite Rueckgang ist nicht eingetreten, im Gegenteil.** Der Abbruchgrund ist damit vom Tisch, **das Defizit bleibt bei 400 kcal.**

Einschraenkung, die dazugehoert: der Anstieg faellt mit steigendem Koerperwasser zusammen (61,74 → 62,50 → 62,70 %). Nach REGELN §5 ist das **keine Erfolgsmeldung** — Muskelzuwachs und Wassereinlagerung sind hier nicht zu trennen. Die Aussage ist ausschliesslich negativ formuliert: es gibt **keinen** Hinweis auf Muskelverlust. Innerhalb des Fensters gab es zwei meldepflichtige Einzeltage (18.09. und 26.09.: Muskelmasse faellt, Wasser steigt), beide unter 0,4 kg und damit im BIA-Rauschen.

### KFA-Trend — erstmals zulaessig

Die Bedingung aus REGELN §5 (4 Wochen und 12 Messungen seit Baseline 28.08.) ist seit dem 25.09. erfuellt. Erste zulaessige Aussage:

**Der KFA-Rohwert derselben Waage faellt: 15,76 → 14,72 → 14,47 % (Wochenmittel).** Ueber drei Wochen also −1,29 Punkte.

**Gegenprobe gegen das Gewicht (REGELN §5, Pflicht):**

```
BIA-Fettmasse KW37 -> KW39: 13,24 -> 12,07 kg  = -1,17 kg
Gewicht        KW37 -> KW39: 84,02 -> 83,49 kg = -0,53 kg
implizierte Magermasse:      -0,53 - (-1,17)   = +0,64 kg
```

+0,64 kg Magermasse in zwei Wochen im Defizit ist **nicht plausibel**. Die Differenz ist Hydration, nicht Fortschritt. Der reale Fettverlust der zwei Wochen liegt naeher an **0,5 bis 0,8 kg**. Das passt zur Rechnung von unten: bei 0,3-0,5 kg Fett pro Woche aus dem Defizit waeren ueber zwei Wochen 0,6-1,0 kg zu erwarten.

Zur Absolutzahl aendert sich nichts: es gilt weiter die **Bandbreite 16-19 % KFA** (REGELN §5, Entscheidung vom 24.09.), kein fester Versatz. Der Waagenwert von 13,7 % am 27.09. ist ein Tiefstwert **dieser Waage**, keine Aussage ueber den echten Koerperfettanteil.

### Messbedingungen

Fuenf der sieben KW39-Wiegungen lagen im Fenster 06:30-08:00, zwei darueber (26.09. 09:15, 27.09. 09:57). Beide bleiben nach der am 26.09. praezisierten Regel (REGELN §5) trendtauglich, weil der Ablauf eingehalten war — direkt nach dem Aufstehen, nach dem Wasserlassen, vor dem Trinken, nur spaeter aufgestanden (Wochenende). Der Stuhlgangstatus ist in KW39 an keinem Tag angegeben.

---

## 3. TDEE-Korrektur nach REGELN §8.4 — zum vierten Mal gesperrt

| Bedingung (Fenster 14.-27.09.) | Status |
| --- | --- |
| ≥21 Tage Daten | erfuellt |
| KW39 ≥5 Wiegungen | erfuellt (7) |
| KW39 ≥5 Esstage | erfuellt (6 vollstaendige) |
| KW38 ≥5 Esstage | formal erfuellt (7 Tage mit Eintrag), **inhaltlich fraglich** — der 20.09. ist mit 651 kcal Untererfassung |
| **KW38 ≥5 Wiegungen** | **nicht erfuellt (4)** — 14., 15., 16., 18.09.; der 20.09. ist nicht trendtauglich |

**Gesperrt, weil KW38 nur vier trendtaugliche Wiegungen hat.** Es fehlt genau **eine** Wiegung, und sie fehlt nicht, weil nicht gemessen wurde, sondern weil die Messung vom 20.09. unter verletzten Bedingungen entstand.

**Ab wann es geht:** am **04.10.2026** liegt das 14-Tage-Fenster auf 21.09.-04.10., KW38 ist dann heraus. KW39 erfuellt beide Bedingungen bereits. Haelt KW40 das Niveau (5 Wiegungen, 5 Esstage), ist die Korrektur **zum ersten Mal ueberhaupt rechenbar.**

**Illustrative Rechnung (ausdruecklich nicht uebernommen):**

```
Ø kcal 14 Tage (14.-27.09.)      = 30.534,8 / 14 = 2.181 kcal
Δ Ø-Gewicht (KW38 -> KW39)       = 83,493 - 83,488 = +0,0054 kg
TDEE ~ 2.181 - (0,0054 x 7700)/14 = 2.178 kcal

ohne den untererfassten 20.09. (13 Tage): Ø 2.299 kcal -> TDEE ~ 2.296 kcal
```

**Das ist der Befund, der aufhorchen laesst, und er wird hier nicht weggerechnet:** zwei Wochen praktisch unveraendertes Gewicht bei rund 2.200-2.300 erfassten kcal deuten auf einen TDEE **weit unter den angenommenen 2.650** hin. Drei Anlaeufe ergaben bisher 1.859 (06.09.), 2.767 (13.09.) und jetzt 2.178 kcal — eine Streuung von 900 kcal. **Die Methode ist mit dieser Datenlage nicht stabil**, und genau deshalb bleibt die Sperre richtig. Zwei Erklaerungen konkurrieren und sind aus den Daten nicht zu trennen:

- Der TDEE ist tatsaechlich niedriger als 2.650 (dann waere das Ziel von 2.250 kcal fast kein Defizit).
- Oder die Erfassung ueberschaetzt die Aufnahme — was der Aufrund-Regel aus §4 **widerspricht**, die in die andere Richtung zeigt.

Beides bleibt offen bis zum 04.10. **Es wird jetzt nichts umgestellt.**

---

## 4. Training

### Volumen und Einheiten

| Woche | Kraft-Einheiten | Arbeitssaetze (roh) |
| --- | --- | --- |
| KW37 | 4 (+ Tennis) | 65 |
| KW38 | 5 | 56 |
| KW39 | **6** (+ Laufen 27.09.) | **80** |

Das Gesamtvolumen faellt **nicht** zwei Wochen in Folge (REGELN §6, Meldepflicht) — KW39 ist die volumenstaerkste Woche der Reihe. Die Mittagseinheiten bei der Freundin (REGELN §3, Wochenstruktur seit 22.09.) sind angekommen und tragen sichtbar.

### Soll-Ist gegen die Wochenziele (REGELN §3 / §8.6)

Zaehlweise: direkter Satz 1,0, indirekte Beteiligung 0,5 (Trizeps beim Druecken, Bizeps beim Ziehen) — dieselbe Zuordnung wie im KW37-Review.

| Muskelgruppe | Ziel | Ist KW39 |  |
| --- | --- | --- | --- |
| Seitliche Schulter | 14-18 | **17,5** | erreicht |
| Brust | 10-14 | **14,0** | erreicht (Obergrenze) |
| Trizeps | 10-14 | **11,5** | erreicht |
| Lat | 10-14 | **8,0** | **verfehlt** |
| Bauch | 10-14 | **9,0** | **verfehlt** |
| Bizeps | 4-10 | **14,0** | **ueber dem Ziel** |
| Beine | 6-12 | **3,0** | **deutlich verfehlt** |
| Unterarme | 8-12 | **0** | **nicht begonnen** |
| Hintere Schulter *(vorlaeufig)* | 8-12 | **4,0** | **verfehlt** |
| Ruecken / Rudern *(vorlaeufig)* | 8-12 | **6,0** | **verfehlt** |

Herleitung der Zahlen, die nicht direkt abzaehlbar sind:

```
Seitliche Schulter = Seitheben Kurzhantel 14 + 0,5 x Schulterpresse 7      = 17,5
Bizeps            = Curls SZ 3 + Preacher Curls 4 + 0,5 x Zugsaetze 14    = 14,0
                    (Zug = Lat Pulldown 6 + Klimmzuege 2 + Rudern 6)
Trizeps           = Katana 4 + 2 + 2 + 0,5 x Schulterpresse 7             = 11,5
```

**Das Muster ist dasselbe wie in KW37, nur schaerfer: die Druck- und Spiegelmuskelseite ist voll, die Zug-, Bein- und Unterarmseite leer.** Drei Punkte dazu:

1. **Bizeps liegt mit 14 Saetzen ueber dem Ziel (4-10) und damit hoeher als Lat (8) und Ruecken (6)** — die niedrigste Prioritaet bekommt mehr Volumen als die beiden mittleren. Ursache ist nicht die Curl-Arbeit allein (7 direkte Saetze), sondern die indirekte Anrechnung aus der Zugarbeit.
2. **Brust mit 14 Saetzen an der Obergrenze — aber ohne einen einzigen Drucksatz.** Das gesamte Brustvolumen kommt aus der Butterfly-Maschine (5+5+4). Schraegbankdruecken gefuehrt Loch 1 war zuletzt am 19.09., Bankdruecken frei zuletzt am 09.09. Fuer den Muskelreiz mag das reichen, fuer eine Progression ueber Last nicht — die Brust hat in KW39 keinen einzigen e1RM-Datenpunkt geliefert.
3. **Die Rotation aus REGELN §3 wird nicht gefahren.** Vorgesehen sind Butterfly Mo/Mi/Fr und hintere Schulter Di/Do; tatsaechlich lief Butterfly am Di und Do (22., 24.09.), hintere Schulter nur am Sa (26.09.). Genau das ist das in §3 benannte Risiko dieser Struktur, und es hat sich in KW39 realisiert.

### e1RM je Reihe (Uebung + Gym + Geraet)

| Reihe | Verlauf im Fenster | Befund |
| --- | --- | --- |
| Lat Pulldown Kabelzug neutral schulterbreit (Schwester) | 22.09. 71,5 (50 kg) → 25.09. **79,0 (55 kg)** | **einzige echte Lastprogression der Woche**, +10 % und damit unter der 20-%-Meldeschwelle |
| Butterfly Maschine (Freundin) | 93,0 / 93,0 / 93,0 → 24.09. **95,5** | leicht aufwaerts, Last bei 65 kg (Maschinenmaximum) |
| Squats gefuehrt (Schwester) | 11.09. 19,5 → 25.09. **21,5** | aufwaerts ueber Wiederholungen, Last 15 kg |
| Schraegbankdruecken gefuehrt Loch 1 (Schwester) | 11.09. 40,0 → 16.09. 40,0 → 19.09. **42,0** | aufwaerts, aber **in KW39 nicht trainiert** |
| Schulterpresse gefuehrt (Schwester) | 22.09. 21,0 → 24.09. 21,0 | flach, erst 2 Einheiten — noch keine Meldung nach §6 (3+ noetig) |
| Katana Extension beidhaendig Kabel | 27,5 / 26,5 / 29,5 / 26,5 | **flach ueber 4 Einheiten**, Last unveraendert 20 kg → meldepflichtig |
| Katana einarmig links / rechts | 12,5 → 13,5 → 13,5 / 13,5 → 13,5 → 14,0 | flach, Last unveraendert 10 kg |
| **Seitheben Kurzhantel (Freundin)** | 7,0 / 7,0 → 7,5 / 7,5 / 7,5 | **Last seit 21.08. unveraendert 5 kg** — siehe unten |
| Seitheben Kabelzug (Schwester) | 7,0 / 7,0 / 7,0 → 19.09. 7,5 | Last unveraendert 5 kg, **in KW39 gar nicht trainiert** |
| Reverse Butterfly Kabelzug | 7,0 / 7,5 / 6,5 → 26.09. 7,5 | Rauschen bei sehr kleinen Lasten, keine Aussage |
| Preacher Curls SZ-Stange (Schwester) | 26.09. 11,0 (7,5 kg) | **neue Reihe, erster Punkt** — Uebungserweiterung vom 24.09. umgesetzt |
| Rudern Kabel neutral schulterbreit | 22.09. 71,5 (50 kg); 25.09. ohne Werte | 25.09. drei Saetze ohne Last/Wdh → zaehlt fuers Volumen, kein e1RM |

**Seitheben, sechste Woche in Folge:** Die Progressionsempfehlung aus REGELN §3 (auf 6 oder 7,5 kg erhoehen, Wiederholungen auf 8-12 zuruecknehmen) steht seit dem 13.09. in der Datei und ist **in KW39 erneut nicht umgesetzt** — alle 14 Saetze liefen mit 5 kg. REGELN §3 verlangt, das in jedem Review nachzuhalten; es ist damit der dritte Review in Folge, in dem dieser Punkt unerledigt gemeldet wird. Seitheben ist die hoechste Volumenprioritaet, und das Volumen stimmt — nur die Last nicht.

### Reihen ohne Eintrag seit ueber 14 Tagen (REGELN §6, Meldepflicht)

| Reihe | letzte Einheit | Tage |
| --- | --- | --- |
| **Ab Rollout (Schwester)** | 06.09. | 21 |
| Seitheben Kurzhantel (Schwester) | 06.09. | 21 |
| Schraegbankdruecken gefuehrt Loch 2 | 06.09. | 21 |
| Klimmzuege breit mit Gummiband | 07.09. | 20 |
| Bizeps Curls SZ-Stange (Schwester) | 07.09. | 20 |
| Bankdruecken frei Langhantel (Freundin) | 09.09. | 18 |
| Trizepsdruecken Kabel (Freundin) | 09.09. | 18 |

Drei davon sind inhaltlich relevant: **Ab Rollout** ist die zweite Bauchuebung und fehlt komplett — das Bauchvolumen bestand in KW39 nur aus Reverse Crunch (9 Saetze) und liegt deshalb unter dem Ziel; REGELN §3 sieht ausserdem alle 2-3 Wochen Benchmark-Saetze fuer Ab Rollout vor, die ausstehen. **Schraegbankdruecken Loch 2** wurde nur ein einziges Mal ausgefuehrt (3 Saetze am 06.09.), der in REGELN §3 vereinbarte Vergleich Loch 1 gegen Loch 2 ueber je zwei bis drei Einheiten ist damit nicht begonnen. Bei **Bankdruecken frei** und **Trizepsdruecken Kabel** (beide Gym Freundin) ist die Ursache die neue Mittagsstruktur: dort laufen nur noch Butterfly und Seitheben. Kurz vor der Schwelle stehen Single Arm Lat Pulldown links/rechts und Cable Crunch (je 14.09., 13 Tage) — naechste Woche meldepflichtig.

---

## 5. Sicherheitsgrenzen aus REGELN §3 — einzeln durchgegangen

| Grenze | Status KW39 |
| --- | --- |
| Defizit nie ueber 15 % des TDEE (max. 397 kcal, Ziel ≥2.253) | **Zielwert formal knapp verletzt** (2.250 = 15,09 %, bekannter Randfall, 2,5 kcal). **Tatsaechlich klar verletzt:** Ø 2.037 kcal = Defizit 613 kcal = **23,1 %** des angenommenen TDEE. |
| Kalorien nie unter dem Grundumsatz 1.902 kcal | **Gerissen an drei Tagen:** 20.09. (651), 21.09. (1.500), 23.09. (1.771). Der 20.09. ist Untererfassung; 21. und 23.09. haben 9 bzw. 12 Zeilen und sind damit real. |
| Abnahme nie schneller als 0,6 %/Woche | **gehalten** — Blockmittel +0,01 %/Woche, das Gewicht steht. |
| **Protein nie unter 1,8 g/kg (151 g), kein einzelner Tag darunter** | **Gerissen an 4 von 6 vollstaendigen Tagen:** 21.09. 121,0 / 24.09. 142,3 / 25.09. 138,4 / 26.09. 118,0 g. Ø 143,5 g gegen 151 g Untergrenze und 175 g Ziel. Der laufende 27.09. liegt mit 119,6 g ebenfalls darunter. |
| Ballaststoffe min. 30 g | Ø 21,3 g — verfehlt, wie in jeder Woche bisher. |
| Fett min. 70 g | Ø 90,3 g — erfuellt. |

**Die Protein-Untergrenze ist die Grenze, die zaehlt.** Sie war die eine Anpassung aus dem KW37-Review („Protein zurueck auf 175 g, kein Tag unter 151 g"), sie ist in REGELN §3 und §7.11 hinterlegt, und sie wurde in KW39 an zwei Dritteln der Tage gerissen — **haeufiger als in KW37**, wo es zwei Ausreisser waren. Nach der eigenen Rangfolge (Muskeln vor Tempo) ist das der Punkt mit Vorrang.

Dass die Muskelmasse trotzdem steigt, entlastet das nicht: Ø 143,5 g Protein bei einem tatsaechlichen Defizit von rund 600 kcal ist genau die Konstellation, in der Magermasse verloren geht — die BIA-Reihe ist zu grob, um das zeitnah zu zeigen.

**Kein Abbruchgrund ausgeloest.** Die Muskelmasse faellt nicht ueber zwei Zeitraeume (§3), und der korrigierte KFA liegt mit der Bandbreite 16-19 % nicht unter 16 % (Ausstiegsregel). **Das Defizit bleibt bei 400 kcal / Ziel 2.250 kcal.**

---

## 6. Merkzettel (REGELN §12)

**Null offene Zeilen.** Die Tabelle enthaelt 35 Zeilen, alle mit Status `in REGELN uebernommen`, die juengste vom 24.09. Es war also nichts abzuarbeiten. Das ist der erwartete Zustand seit der Umstellung vom 24.09.: Aenderungen werden im Cowork-Chat direkt in `REGELN.md` eingetragen, der Merkzettel ist nur noch Auffanglager.

Die Aenderungen aus diesem Review sind entsprechend direkt eingetragen: **REGELN.md**** v1.14 → v1.15.**

---

## 7. Die eine Anpassung fuer KW40

> **Ein Standard-Shake pro Tag wird fest eingeplant — 40 g Protein / 180 kcal, zusaetzlich zum bisherigen Essen.**

**Begruendung.** Es ist die einzige Anpassung, die beide gerissenen Grenzen gleichzeitig schliesst, und sie rechnet sich sauber:

```
Ø Protein 143,5 g + 40 g = 183,5 g   (Ziel 175 g, Untergrenze 151 g)
Ø kcal   2.037   + 180   = 2.217     (Ziel 2.250)
schlechtester Tag 118,0 g + 40 = 158,0 g -> ueber der Untergrenze von 151 g
```

Damit landen Protein und Kalorien in einem Schritt dort, wo sie geplant waren — ohne dass eine Zahl in den Zielen geraten oder verschoben werden muss. An Tagen, die ohne Shake bereits 175 g erreichen (in KW39 zwei von sechs), ist er entbehrlich; gebucht wird er wie in REGELN §3 hinterlegt ohne Rueckfrage als 40-g-Mischung.

Gegen die Alternativen: **das Defizit zu verkleinern** waere die falsche Reihenfolge, solange die Muskelmasse steigt und der TDEE selbst ungeklaert ist — das entscheidet sich am 04.10. **Die Seitheben-Last** ist der zweitwichtigste Punkt, aber sie steht seit dem 13.09. in den Regeln und braucht keine neue Wochenanpassung, sondern Umsetzung. **Die Volumenluecken** sind mehrere Punkte und damit per §8.10 keine „eine Anpassung".

### Nebenbedingungen (keine eigenen Anpassungen)

1. **Wiegereihe lueckenlos bis zum 04.10. weiterfuehren.** Fuenf Wiegungen in KW40 machen die TDEE-Korrektur zum ersten Mal rechenbar — nach vier Fehlversuchen ist das der Punkt, an dem die wichtigste offene Zahl des ganzen Projekts entschieden wird.
2. **Seitheben-Last auf 6 oder 7,5 kg**, Wiederholungen auf 8-12 volle Wdh (REGELN §3, seit 13.09. offen).
3. **Zug-, Bein- und Unterarmseite:** Lat 8 → 10-14, Ruecken 6 → 8-12, Beine 3 → 6-12, Unterarme 0 → 8-12, hintere Schulter 4 → 8-12. Praktisch heisst das: der Engpass ist die Abendeinheit bei der Schwester, nicht der Mittag bei der Freundin.
4. **Ab Rollout** wieder aufnehmen (21 Tage ohne Eintrag) — das schliesst gleichzeitig die Bauchluecke.
5. **Mindestens eine Brust-Druckuebung pro Woche**, damit die Brust wieder einen e1RM-Datenpunkt liefert.

---

## 8. Offen, unveraendert

- **Zweite Caliper-Messung** (geuebter, moeglichst dieselbe Person) oder DEXA — davon haengt ab, ob die Bandbreite 16-19 % KFA wieder zu einer Zahl wird und damit die gesamte Zeitplanung bis 14 %.
- **Volumen-Prioritaeten hintere Schulter (8-12) und Ruecken/Rudern (8-12)** sind von mir ergaenzt und **von Simon weiterhin nicht bestaetigt.** Beide wurden in KW39 erneut klar verfehlt.
- **Brust / Nippelwulst** aerztlich abklaeren (unveraendert offen; der Cut wird deswegen nicht verschaerft).
- **Unterer Ruecken:** der ab 24.09. vereinbarte Test (1x/Woche, zwei leichte Saetze, Schmerzdokumentation an Tag 0/1/2) ist in KW39 **nicht in den Daten aufgetaucht** — keine entsprechende Zeile in der Trainingstabelle.
- **Stangengewicht** der freien Langhantel bei der Freundin, **Kabelstation** dort (ein Turm oder zwei), **Beschriftung der Butterfly-Maschine**, **Bandfarbe/kg des Klimmzugbands** — alles weiterhin offen.
- **Erbsenprotein-Fluff:** Naehrwerte beim ersten Verzehr von der Packung erfassen.

---

## Nachtrag vom 28.09.2026 — KW39 mit vollständigem 27.09.

Dieses Review lief am 27.09. abends, als der 27.09. noch nicht abgeschlossen war, und rechnete deshalb mit **sechs** Esstagen. Simon hat am 28.09. zwei Posten nachgemeldet (eine Banane und den Standard-Shake). Damit ist der 27.09. ein vollständiger Esstag und die Wochenzahlen ändern sich:

|  | Review vom 27.09. (6 Tage) | korrigiert (7 Tage) |
| --- | --- | --- |
| Ø kcal | 2.037 | **2.093** |
| Ø Protein | 143,5 g | **146,0 g** |
| Ø KH | 154,5 g | 158,6 g |
| Ø Fett | 90,3 g | 93,0 g |
| Ø Ballast | 21,3 g | 22,0 g |
| Geschätzt-Anteil | 63,9 % | 65,3 % |

**Wichtigste Korrektur:** Der 27.09. schloss mit **160,9 g Protein** ab und liegt damit **über** der Untergrenze von 151 g — nicht darunter, wie im Review auf Basis des Zwischenstands (119,6 g) vermerkt. Die Protein-Untergrenze wurde in KW39 also an **4 von 7** Tagen gerissen (21., 24., 25., 26.09.), nicht an 5 von 7.

Der Grund für den guten 27.09. ist genau die Anpassung, die dieses Review für KW40 beschlossen hat: Simon hat abends den Standard-Shake getrunken, und allein der hob den Tag von 120,9 auf 160,9 g. Die Anpassung ist damit am Tag ihrer Beschlussfassung bereits einmal bestätigt.

Der Befund selbst bleibt unverändert: Ø 146,0 g liegen weiterhin unter der Untergrenze von 151 g und deutlich unter dem Ziel von 175 g. Auch die Gewichts-, Körperanalyse- und Trainingsteile dieses Reviews sind von der Korrektur nicht betroffen.

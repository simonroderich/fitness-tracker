# Wochenreview KW36

- **Datum:** 2026-09-03
- **Art:** Wochenreview
- **Zeitraum:** 2026-08-14 bis 2026-09-03 (21-Tage-Fenster); auswertbare Daten nur 21.08.-29.08.

> **Kurzfazit:** Keine Anpassung. TDEE-Korrektur gesperrt: 6 Tage ohne Ernaehrungseintrag (29.08.-03.09.), nur 1 Esstag im letzten 7-Tage-Fenster statt der geforderten 5. Gewicht und Koerperanalyse laufen weiter (3 Messungen), Muskelmasse 65.8 -> 66.3 kg, KFA 16.3 -> 16.0 % - beides zu frueh fuer eine Aussage (Regel: 4 Wochen / 12 Messungen). Wichtigster Befund: die Waage misst 16.0 % statt der geschaetzten 20 % - das wuerde das Ziel 14 % von ~6 kg auf ~2 kg Fett verkuerzen und die Dauer von 12 auf 4 Wochen. Ohne Ankermessung ist das keine belastbare Grundlage. Eine Anpassung fuer die kommende Woche: lueckenlose Ernaehrungserfassung, sonst faellt die TDEE-Korrektur auch naechste Woche aus.

*Aus Notion übernommen am 2026-10-21. Historisches Dokument — Regeln und Zahlen darin können überholt sein.*

---

## 0. Verdikt vorab

**Simon hat recht: fuer diese Woche gibt es nichts zu rechnen.** Die Ernaehrungsdaten enden am 28.08. Damit ist die TDEE-Korrektur nach REGELN §8.4 formal gesperrt, und eine Kalorienaussage waere Rauschen. Was trotzdem hier steht, sind die drei Dinge, die von der Luecke nicht betroffen sind: die Koerperanalyse-Werte, ein Datenfehler in der Gewicht-Tabelle, und die Zielrechnung, die REGELN §3 nach der ersten echten KFA-Messung ausdruecklich verlangt.

---

## 1. Datenlage im 21-Tage-Fenster (14.08. - 03.09.)

| Tabelle | Zeilen | Abgedeckte Tage | Luecke |
| --- | --- | --- | --- |
| Ernaehrung | 85 | 21.08. - 28.08. (8 Tage) | **29.08. - 02.09. = 5 Tage, dazu heute 03.09. offen** |
| Gewicht | 8 (morgens) + 1 abends | 22.08. - 29.08., 03.09. | **30.08. - 02.09. = 4 Tage** |
| Training | 6 Einheiten | 21., 24., 25., 28.08., 01., 02.09. | keine |

Vor dem 21.08. liegen im Tracker keine Daten - das Fenster ist faktisch 14 Tage lang, nicht 21.

---

## 2. Ernaehrung - Tagessummen (21.08. - 28.08.)

| Datum | kcal | Protein g | KH g | Fett g | Ballast g | Zeilen |
| --- | --- | --- | --- | --- | --- | --- |
| 21.08. | 1572 | 112.5 | 118.0 | 72.4 | 9.9 | 13 |
| 22.08. | 3175 | 189.6 | 235.1 | 159.8 | 21.8 | 10 |
| 23.08. | 2335 | 165.6 | 193.3 | 91.6 | 30.6 | 9 |
| 24.08. | 2150 | 180.0 | 129.0 | 98.0 | 4.0 | 9 |
| 25.08. | 2795 | 158.8 | 194.5 | 149.2 | 19.0 | 15 |
| 26.08. | 2217 | 148.5 | 160.0 | 106.5 | 22.7 | 11 |
| 27.08. | 2575 | 150.0 | 165.5 | 144.1 | 30.0 | 9 |
| 28.08. | 2442 | 184.1 | 188.0 | 105.1 | 37.5 | 10 |

**Rechenweg Durchschnitte** (Python/pandas, `groupby(Datum).sum()`, dann Mittel ueber die Tage):

- Fenster **22.-28.08.** (7 zusammenhaengende Tage, alle erfasst):
  - Ø kcal = 17 689 / 7 = **2527 kcal**
  - Ø Protein = 1176.6 / 7 = **168.1 g**
  - Ø KH = 1265.4 / 7 = **180.8 g**
  - Ø Fett = 854.3 / 7 = **122.0 g**
  - Ø Ballast = 165.6 / 7 = **23.7 g**
- Fenster **21.-28.08.** (8 Tage): Ø kcal **2408**, Ø Protein **161.1 g**

**Bewertung gegen die Zielwerte:**

- kcal 2527 vs. Ziel 2500 - rechnerisch punktgenau, praktisch bedeutungslos (siehe Datenqualitaet).
- Protein 168 g vs. Ziel 175 g. Untergrenze 1,8 g/kg = 152 g bei 84.65 kg: **eingehalten**, Ziel knapp verfehlt.
- Fett 122 g vs. Minimum 70 g - deutlich darueber. Der Ueberschuss steckt fast vollstaendig in Soßen und Dressings: Salatsoße/Dressing 8 Loeffel am 25.08. und 27.08. mit je 450 kcal, Sahnesaucen 26.-28.08. mit 190-335 kcal, Doenersoße 210 kcal.
- Ballaststoffe 23.7 g vs. Ziel 30 g - unter Ziel, aber steigend (letzte drei erfasste Tage 22.7 / 30.0 / 37.5 g, getragen von den geroesteten Edamame).

**Datenqualitaet (REGELN §8.2):** Anteil `Geschaetzt = __YES__` liegt bei **85 %** der Zeilen. Die Schwelle von 40 % ist um mehr als das Doppelte gerissen. Dazu kommt: die Schaetzregel §4.3 rundet bei niedriger Konfidenz bewusst nach oben, und genau die groessten Posten (Soßen, Dressings, Bratfett) haben niedrige Konfidenz. **Die kcal-Summen sind systematisch nach oben verzerrt.** Eine Aussage der Art "du isst zu viel" waere aus diesen Daten nicht begruendbar.

Spannweite 1572 kcal (21.08.) bis 3175 kcal (22.08.). Beide Tage reissen die Ausreisser-Schwelle aus §7.4 (unter 60 % bzw. ueber 160 % des Ziels), beide sind Altchat-Rekonstruktionen und nachtraeglich nicht mehr aufloesbar.

---

## 3. Gewicht - nur Morgenmessungen (REGELN §5)

| Datum | kg | Anmerkung |
| --- | --- | --- |
| 22.08. | 84.30 | vor dem Stuhlgang |
| 23.08. | 83.90 | nach dem Pinkeln, massgeblicher Wert des Tages |
| 24.08. | 84.20 |  |
| 25.08. | 83.50 | Tageszeit unsicher |
| 26.08. | 84.30 |  |
| 28.08. | 84.20 | Baseline 8-Elektroden-Waage |
| 29.08. | 83.55 |  |
| 03.09. | 84.65 | erste Messung nach der Luecke |

Der Wert vom 21.08. (85.4 kg) ist eine Abendmessung und geht nach §5 nicht in den Trend. Der zweite Wert vom 23.08. (84.5 kg, vor dem Klo) ist als ungueltig gekennzeichnet und ausgeschlossen.

**Kein gleitender 7-Tage-Durchschnitt berechenbar** - dafuer braeuchte es sieben aufeinanderfolgende Tage, und zwischen dem 29.08. und dem 03.09. liegen vier Luecken. Ein Blockvergleich waere formal moeglich (22.-25.08. Ø 83.98 kg gegen 26.08.-03.09. Ø 84.18 kg, also +0.2 kg), ist aber mit vier Werten pro Block und ungleichen Abstaenden **Rauschen und wird nicht als Trend gemeldet**.

Der Anstieg 29.08. -> 03.09. (83.55 -> 84.65 kg, +1.1 kg) verteilt sich auf fuenf Tage und faellt mit der Hochzeit samt Alkohol am 29.08. zusammen. Wasser, nicht Fett - keine Bewertung.

### Datenfehler, der repariert werden muss

Die ungueltige Doppelmessung vom 23.08. hat als `Notiz`:

> `aus Altchat - vor dem Klo - UNGUELTIG doppelt gemessen siehe Folgezeile`

Der Standardfilter aus REGELN §2 lautet `WHERE Notiz NOT LIKE 'UNGUELTIG%'` - er prueft den **Zeilenanfang**. Diese Zeile faengt mit "aus Altchat" an und rutscht damit durch den Filter. Ich habe sie in dieser Auswertung von Hand ausgeschlossen; eine automatische Auswertung wuerde sie mitrechnen und das Gewicht des 23.08. verfaelschen. **Die Notiz muss auf `UNGUELTIG - ...` am Zeilenanfang umgeschrieben werden.** Bestehende Zeilen werden nach §2 nicht unaufgefordert angefasst - der Punkt steht als offene Aufgabe in STAND.md.

---

## 4. Koerperanalyse (8-Elektroden-Waage)

| Datum | Gewicht kg | KFA % | Muskelmasse kg | Fettmasse kg | FFM kg | Viszeralfett | Grundumsatz kcal |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 28.08. | 84.20 | 16.3 | 65.8 | 13.7 | 70.5 | 4 | 1892 |
| 29.08. | 83.55 | 16.0 | 65.5 | 13.4 | 70.2 | 4 | 1887 |
| 03.09. | 84.65 | 16.0 | 66.3 | 13.5 | 71.1 | 4 | 1904 |

**Aussage: zu frueh.** REGELN §5 verlangt 4 Wochen und mindestens 12 Messungen, bevor ein KFA-Trend kommentiert wird. Wir haben 6 Tage und 3 Messungen. Die Zahlen stehen hier als Protokoll, nicht als Befund.

Was sich trotzdem sagen laesst, weil es eine **Sicherheitsregel** betrifft: REGELN §3 verlangt eine Defizit-Reduktion, wenn die Muskelmasse ueber zwei Messzeitraeume faellt. Sie faellt nicht (65.8 -> 66.3 kg). **Kein Handlungsbedarf aus dem Muskelschutz.** Die 0.5 kg Zuwachs sind bei parallel gestiegenem Koerperwasser (51.7 -> 52.1 kg) allerdings genauso gut Wasser wie Muskel - keine Erfolgsmeldung.

---

## 5. TDEE-Korrektur nach REGELN §8.4

**Ergebnis: gesperrt, keine Anpassung.**

Die Formel lautet:

```
TDEE_real ≈ Ø kcal (14 Tage) − (Δ Ø-Gewicht_kg × 7700) / 14
```

Bedingungen: mindestens 21 Tage Daten, mindestens 5 Wiegungen **und** 5 erfasste Esstage **pro Woche**.

Pruefung fuer das letzte 7-Tage-Fenster (28.08. - 03.09.):

- Wiegungen: 3 (28.08., 29.08., 03.09.) - erforderlich 5, **verfehlt**
- Erfasste Esstage: **1** (28.08.) - erforderlich 5, **klar verfehlt**
- Zusammenhaengende Datenhistorie: 8 Tage - erforderlich 21, **verfehlt**

Alle drei Bedingungen sind verletzt. Die Formel wird nicht angewandt. Der TDEE bleibt bei der **Formelschaetzung 2800 kcal** (Mifflin-St Jeor 1890 × 1,5), unveraendert und weiterhin ungeprueft.

**Was fehlt, damit sie naechste Woche laufen kann:** mindestens 5 Esstage und 5 Morgenwiegungen zwischen dem 04.09. und dem 10.09.

---

## 6. Training

Sechs Einheiten im Fenster: 21., 24., 25., 28.08. (alle Gym Schwester, Push), 01.09. (Gym Freundin, Brust/Schulter/Bizeps), 02.09. (Gym Schwester, Trizeps/Beine/Ruecken).

**Volumen ist nicht berechenbar.** Von 37 Zeilen tragen nur 12 sowohl Gewicht als auch Wiederholungen. Die Einheiten vom 01.09. und 02.09. enthalten fast ausschliesslich leere Zahlenfelder ("nachtraeglich nicht mehr rekonstruierbar"). `Last gesamt kg` ist nur bei 4 Zeilen gefuellt. Eine Volumenkurve aus diesen Daten waere erfunden.

**e1RM je Reihe (Uebung + Gym + Geraet), soweit rechenbar:**

<table header-row="true">
<tr>
<td>
Reihe
</td>
<td>
21.08.
</td>
<td>
28.08.
</td>
<td>
Bewertung
</td>
</tr>
<tr>
<td>
Bankdruecken gefuehrt · Schwester · Langhantel gefuehrt
</td>
<td>
38.0 (30 kg × 8)
</td>
<td>
38.0 (30 kg × 8, 3 Saetze)
</td>
<td>
**stagniert ueber 2 Einheiten**
</td>
</tr>
<tr>
<td>
Seitheben · Schwester · Kurzhantel
</td>
<td>
6.0 (5 kg × 6)
</td>
<td>
7.0 (5 kg × 13)
</td>
<td>
mehr Wdh bei gleichem Gewicht
</td>
</tr>
<tr>
<td>
Cable Flies · Schwester · Kabelzug
</td>
<td>
  • (keine Wdh)
</td>
<td>
26.5 (20 kg × 10)
</td>
<td>
erste rechenbare Zeile
</td>
</tr>
<tr>
<td>
Bizeps Curls SZ · Schwester · SZ-Stange
</td>
<td>
13.5 (10 kg × 10)
</td>
<td>
-
</td>
<td>
am 01.09. ohne Zahlen
</td>
</tr>
</table>

Die Bankdruecken-Stagnation liegt bei 2 Einheiten - die Meldeschwelle aus §6 ist 3+. **Noch keine Meldung, aber beim naechsten Mal ist sie faellig.** Bei 3×8 mit gleichem Gewicht ueber zwei Wochen waere ein Erhoehungsversuch auf 32.5 kg pro Seite naheliegend.

**Inkonsistenz:** "Schulterpresse gefuehrt" ist am 21. und 25.08. als `Geraet = Langhantel gefuehrt`, am 28.08. als `Geraet = Maschine` erfasst. Nach §6 sind das zwei getrennte Reihen und nicht vergleichbar. Falls es dasselbe Geraet ist, muss die Zuordnung vereinheitlicht werden - sonst ist der Verlauf dieser Uebung dauerhaft zerschnitten.

**Positiv und neu:** Am 02.09. stehen zum ersten Mal ueberhaupt eine Beinuebung (Squats gefuehrt) und eine Ruecken-Zugübung (Rudern Kabel) im Tracker. Der Plan war bisher reines Push. Das ist die groesste Aenderung der Woche - und die einzige, fuer die es keine Zahlen gibt.

---

## 7. Zielrechnung nach der ersten echten KFA-Messung (REGELN §3)

REGELN §3 haelt fest: "Sobald die erste echte KFA-Messung vorliegt, rechnest du das konkret durch." Sie liegt vor. Hier die Rechnung - **mit einem grossen Vorbehalt, der darunter steht.**

Ausgangswerte 03.09.: 84.65 kg, KFA 16.0 %

```
Fettmasse    = 84.65 × 0.160        = 13.54 kg
Magermasse   = 84.65 − 13.54        = 71.11 kg   (Waage: FFM 71.1 - stimmt ueberein)

Ziel 14 % bei unveraenderter Magermasse:
Zielgewicht  = 71.11 / (1 − 0.14)   = 82.68 kg
Zielfett     = 82.68 × 0.14         = 11.58 kg
Abzunehmen   = 84.65 − 82.68        =  1.97 kg

Tempolimit   = 84.65 × 0.006        =  0.51 kg/Woche
Mindestdauer = 1.97 / 0.51          =  3.9 Wochen
```

**Das steht in scharfem Widerspruch zu REGELN §3**, wo auf Basis der Selbstschaetzung von 20 % noch 5-6 kg Fett und 14-16 Wochen stehen. Zur Kontrolle dieselbe Rechnung mit 20 %:

```
Fettmasse    = 84.65 × 0.200        = 16.93 kg
Magermasse   = 67.72 kg
Zielgewicht  = 67.72 / 0.86         = 78.74 kg
Abzunehmen   = 5.91 kg  →  11.6 Wochen
```

**Die Zeitplanung haengt komplett daran, welcher der beiden Werte stimmt - 4 Wochen oder 12.** Und genau das kann die Waage nicht entscheiden. REGELN §5 sagt es deutlich: der Absolutwert einer Hand-zu-Fuss-BIA ist unzuverlaessig, brauchbar ist nur der Trend derselben Waage unter denselben Bedingungen. Hand-zu-Fuss-Geraete geben bei jungen, trainierten Maennern typischerweise zu niedrige KFA-Werte aus.

**Konsequenz: die Zahlen in REGELN §3 werden nicht auf 2 kg / 4 Wochen umgeschrieben.** Der offene Zielkonflikt bleibt unaufgeloest, bis eine unabhaengige Ankermessung vorliegt (DEXA, ersatzweise Caliper oder Navy-Massband als zweite Methode). Der Merkzettel-Punkt "Absolutwert KFA - Ankermessung gewuenscht" ist damit die wichtigste offene Aufgabe im Projekt - er entscheidet ueber einen Faktor 3 in der Zeitplanung.

---

## 8. Die eine Anpassung fuer die kommende Woche (REGELN §8.8)

> **Keine Aenderung an Kalorien, Makros oder TDEE. Stattdessen: lueckenlose Ernaehrungserfassung vom 04.09. bis 10.09. - mindestens 5 Esstage und 5 Morgenwiegungen.**

Begruendung: Es gibt derzeit keine belastbare Groesse, an der man eine Zielwertaenderung festmachen koennte. Der TDEE ist eine ungepruefte Formelschaetzung, die kcal-Summen sind zu 85 % geschaetzt und nach oben verzerrt, der Gewichtsverlauf hat vier Luecken, und der KFA-Absolutwert ist um moeglicherweise 4 Prozentpunkte unsicher. Eine Anpassung auf dieser Basis waere geraten, nicht gerechnet. Die einzige Massnahme, die den naechsten Review handlungsfaehig macht, ist die Datenerfassung selbst.

Zweitwichtigster Punkt, aber ausdruecklich **nicht** die Anpassung dieser Woche: die Ankermessung fuer den KFA.

---

## 9. Verarbeitete Merkzettel-Punkte

Drei offene Zeilen, alle abgearbeitet - Details im Aenderungsprotokoll von REGELN.md (v1.5):

1. **Trainingsspektrum erweitert - Squats und Ruecken neu** (03.09.) → in REGELN uebernommen. §3 sagt nicht mehr "Fokus Brust/Schulter/Arme/Bauch", die Ausstattungstabelle ist um Butterfly (Freundin), gerade Stange / Seil / hueftbreite Stange am Kabelzug und Squats an der gefuehrten Langhantel (Schwester) ergaenzt.
2. **Soja Poppers - Herkunft der Angabe pruefen** (26.08.) → in REGELN uebernommen. Die unbelegte Bestandsangabe wurde aus §3 entfernt und durch den belegten Festwert der geroesteten Edamame (KoRo, 430 kcal / 44 g Protein pro 100 g) ersetzt.
3. **Erbsenprotein-Fluff fuer Muesli** (26.08.) → in REGELN uebernommen, als offener Punkt unter Supplements notiert (milcheiweissfrei, Naehrwerte beim ersten Verzehr erfassen).

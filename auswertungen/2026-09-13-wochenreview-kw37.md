# Wochenreview KW37

- **Datum:** 2026-09-13
- **Art:** Wochenreview
- **Zeitraum:** 2026-09-07 bis 2026-09-13 (Vergleich: KW36 31.08.-06.09., KW35 24.-30.08.)

> **Kurzfazit:** Datenerfassung erstmals auf Soll (6 Esstage, 5 Wiegungen) - die TDEE-Korrektur bleibt trotzdem gesperrt, weil KW36 im 14-Tage-Fenster liegt und dort nur 2 Esstage stehen. Illustrativ ergibt die Formel erstmals einen plausiblen Wert (2.767 kcal, alter Ansatz 2.650). Zwei Warnsignale: Ø Protein 150,9 g liegt unter der eigenen Untergrenze von 151,2 g (1,8 g/kg), und die Muskelmasse faellt erstmals (66,23 -> 66,04 kg) - ein zweiter fallender Zeitraum wuerde das Defizit automatisch auf 300 kcal zurueckfahren. Anpassung fuer KW38: Protein jeden Tag auf 175 g, kein Tag unter 151 g.

*Aus Notion übernommen am 2026-10-21. Historisches Dokument — Regeln und Zahlen darin können überholt sein.*

---

## Datengrundlage

Zeitraum 24.08.-13.09.2026 (21 Tage), Quellen: Notion-Tabellen Gewicht, Ernaehrung, Training. Zeilen mit `Notiz LIKE 'UNGUELTIG%'` ausgeschlossen. Rechnungen mit Python/pandas.

**Vorbehalt zur Datenqualitaet (REGELN §4):** Anteil `Geschaetzt = __YES__` in KW37 liegt bei **55,6 %** (30 von 54 Zeilen) - ueber der 40-%-Schwelle, also gilt der Vorbehalt. Immerhin eine deutliche Verbesserung gegenueber KW36 (88,9 %). Weil bei niedriger Konfidenz bewusst nach oben gerundet wird, sind die kcal-Summen **systematisch nach oben verzerrt**. Ein Ø unter Ziel ist also eher noch niedriger, ein Ø ueber Ziel kein Beweis fuer ein zu kleines Defizit.

Der laufende Tag **13.09. zaehlt nicht als Esstag** (REGELN §8). Er wird separat ausgewiesen, aber nicht in die Wochenmittel gerechnet.

---

## 1. Ernaehrung KW37 (07.-12.09., 6 vollstaendige Tage)

|  | Ø KW37 | Ziel | Abweichung |
| --- | --- | --- | --- |
| kcal | **2.208** | 2.250 | -42 |
| Protein | **150,9 g** | 175 g | **-24,1 g** |
| KH | 166,7 g | ~230 g | -63,3 |
| Fett | 91,2 g | min. 70 g | erfuellt |
| Ballaststoffe | **21,1 g** | min. 30 g | **-8,9 g** |

Mit dem laufenden Tag 13.09. (843 kcal, noch unvollstaendig) waeren es 2.013 kcal / 133,9 g Protein ueber 7 Tage - diese Zahl ist nur der Vollstaendigkeit halber genannt und nicht belastbar.

**Makro-Gegenprobe (REGELN §7.1):** 150,9x4 + 166,7x4 + 91,2x9 = 2.091 kcal gegen 2.208 kcal erfasst = 5,3 % Abweichung. Innerhalb der 10-%-Toleranz, die Zeilen sind in sich stimmig.

**Esstage je Woche:** KW35 = 5, KW36 = 2, KW37 = 6. Die Erfassung hat sich gegenueber KW36 klar erholt - das war die Anpassung des letzten Reviews und sie ist aufgegangen.

**Einschraenkung:** Die beiden Tage mit dem niedrigsten Protein (10.09. mit 131,5 g, 12.09. mit 95,0 g) haben auch die wenigsten Zeilen (je 6 statt sonst 10-11). Es ist deshalb nicht sauber trennbar, ob an diesen Tagen wirklich weniger Protein gegessen oder nur weniger erfasst wurde. Fuer die Bewertung gilt trotzdem, was in der Tabelle steht.

---

## 2. Gewicht

Nur Morgenmessungen, Navy-Dublette vom 05.09. herausgerechnet (gleicher Wert, andere Messmethode).

| Woche | n | Ø Gewicht |
| --- | --- | --- |
| KW35 (24.-30.08.) | 5 | 83,95 kg |
| KW36 (31.08.-06.09.) | 4 | 84,89 kg |
| KW37 (07.-13.09.) | 5 | **84,02 kg** |

**Kein gleitender 7-Tage-Durchschnitt moeglich.** Laengste lueckenlose Wiegereihe: 6 Tage (07.-12.09., der 09.09. fehlt; am 13.09. bisher nicht gewogen). Nach REGELN §5 gibt es damit weiterhin keinen Durchschnitt, sondern nur einen Blockvergleich - und der ist ausdruecklich **kein Trend**.

> **Hinweis auf einen Regelverstoss in den Daten:** Die Notizen vom 11.09. und 12.09. sprechen von einem "7-Tage-Schnitt" (84,44 -> 84,34 -> 84,16 kg). Das ist ein Blockmittel ueber sieben Kalendertage mit Luecken, kein gleitender Durchschnitt. Nach REGELN §5 haette das so nicht formuliert werden duerfen. Die Zeilen bleiben unveraendert, der Begriff wird hier richtiggestellt.

**Sicherheitsgrenze Tempo (REGELN §3):** KW36 -> KW37 sind -0,867 kg = **-1,02 % pro Woche**. Die eigene Obergrenze liegt bei 0,6 %. Nominal ist die Grenze also gerissen.

**Das ist aber mit hoher Wahrscheinlichkeit ein Artefakt, kein echter Abnahmeschub:**

- KW36 besteht nur aus vier Messungen (03.-06.09.), die alle im oberen Bereich lagen (84,65-85,10 kg) - Nachlauf der Luecke 29.08.-02.09. inkl. Hochzeit mit Alkohol am 29.08.
- Der 05.09. (85,10 kg) wurde um 09:53 statt im ueblichen Fenster 06:39-07:52 gemessen und ist laut eigener Notiz nur eingeschraenkt verwendbar.
- Ueber zwei Wochen gerechnet: KW35 83,95 kg -> KW37 84,02 kg = **+0,07 kg**. Das Gewicht ist seit drei Wochen praktisch unveraendert.

**Konsequenz: keine Verlangsamung des Defizits allein wegen dieser Zahl.** Reisst KW38 die 0,6-%-Grenze erneut, ist es kein Artefakt mehr und das Defizit wird reduziert.

**Messzeit-Drift:** 10.09. 06:39, 11.09. 08:05, 12.09. 08:41. Zwei Tage in Folge deutlich ausserhalb des urspruenglichen Fensters. Das verschlechtert genau die Vergleichbarkeit, auf der die TDEE-Korrektur der naechsten Woche beruht.

---

## 3. TDEE-Korrektur nach REGELN §8.4 - dritter Anlauf, weiterhin gesperrt

Bedingungen:

| Bedingung | Status |
| --- | --- |
| mindestens 21 Tage Daten | erfuellt |
| KW37: mindestens 5 Wiegungen | erfuellt (5) |
| KW37: mindestens 5 Esstage | erfuellt (6) |
| KW36: mindestens 5 Wiegungen | **nicht erfuellt (4)** |
| KW36: mindestens 5 Esstage | **nicht erfuellt (2)** |

**Ergebnis: keine Anpassung.** Das 14-Tage-Fenster der Formel (31.08.-13.09.) enthaelt zwingend KW36, und KW36 ist die Luecken-Woche. KW37 selbst erfuellt inzwischen alle Bedingungen.

**Rechnung rein illustrativ, nicht zu uebernehmen:**

```
Ø kcal 14 Tage (31.08.-12.09., 8 erfasste Tage von 13)   = 2.290 kcal
Δ Ø-Gewicht KW36 -> KW37                                 = -0,8675 kg
TDEE_real ~ 2.290 - (-0,8675 x 7700) / 14
          = 2.290 + 477                                  = 2.767 kcal
```

Abweichung zum angesetzten TDEE von 2.650 kcal: **+117 kcal** - das laege ueber der 100-kcal-Schwelle und wuerde bei erfuellten Bedingungen eine Anpassung ausloesen (gedeckelt auf +150 kcal/Woche).

**Das ist der erste Anlauf, der ueberhaupt eine plausible Zahl liefert.** Am 03.09. und 06.09. ergab dieselbe Formel Werte unterhalb des Grundumsatzes (zuletzt 1.859 kcal), also physiologisch unmoegliche Ergebnisse. 2.767 kcal liegt dagegen nahe an der Gegenprobe von unten (BMR + Nahrungsthermogenese + NEAT + Training = 2.720 kcal) und knapp ueber der Formelschaetzung 2.650.

**Trotzdem wird nichts geaendert**, und zwar aus drei Gruenden: die Bedingung ist formal nicht erfuellt; von 13 Tagen im 14-Tage-Fenster sind nur 8 erfasst; und der Gewichtsdelta, der die Rechnung traegt, ist derselbe Block-Artefakt wie in Abschnitt 2 - faellt er kleiner aus, faellt der TDEE-Wert mit.

**Wichtig fuer naechste Woche:** Ab dem Review am 20.09. liegt KW36 ausserhalb des 14-Tage-Fensters. Haelt KW38 das Niveau von KW37 (5 Esstage, 5 Wiegungen), ist die Korrektur zum ersten Mal ueberhaupt rechenbar.

---

## 4. Koerperanalyse - Vorrang der Muskelmasse

| Woche | Ø Muskelmasse | Ø Koerperwasser |
| --- | --- | --- |
| KW36 (03.-06.09.) | 66,225 kg (n=4) | 61,30 % |
| KW37 (07.-12.09.) | **66,040 kg (n=5)** | 61,74 % |

**Δ Muskelmasse = -0,185 kg.** Das ist der **erste fallende Messzeitraum**. Die Abbruchregel greift erst bei **zwei fallenden Zeitraeumen in Folge** - sie ist also noch nicht ausgeloest, das Defizit bleibt bei 400 kcal.

Der Betrag liegt innerhalb des BIA-Rauschens und waere fuer sich genommen bedeutungslos. Zwei Dinge machen ihn trotzdem meldepflichtig:

1. Die Muskelmasse faellt, **waehrend das Koerperwasser steigt** (61,30 -> 61,74 %). Bei einer BIA-Waage laeuft die Muskelschaetzung dem Wasser hinterher - steigendes Wasser haette den Muskelwert eher nach oben druecken muessen. Dass er trotzdem faellt, ist das ungeguenstigere der beiden Vorzeichen.
2. Im selben Zeitraum lag das Protein unter der eigenen Untergrenze (Abschnitt 5). Das ist genau die Kombination, gegen die REGELN §3 die Rangfolge "Muskeln vor Tempo" gesetzt hat.

**KFA-Trend: weiterhin zu frueh.** Seit Baseline 28.08. liegen 11 Messungen mit der 8-Elektroden-Waage vor - noetig sind 12 - und es sind 2,2 von 4 geforderten Wochen vergangen. Eine Aussage zum KFA-Trend gibt es fruehestens am 25.09.

Rohwert 12.09.: 15,3 % -> **korrigiert (+4,5 Punkte Navy-Versatz) rund 19,8 %**. Die Ausstiegsschwelle von 16 % ist damit klar nicht erreicht, das Defizit von 400 kcal bleibt zulaessig. Der nominale Rueckgang von rund 21,0 % (06.09.) auf 19,8 % waere rund 1 kg Fett in einer Woche bei praktisch unveraendertem Gewicht - das ist rechnerisch unmoeglich und damit ueberwiegend Hydration, kein Fettverlust. **Der Zeitplan bis 14 % wird deshalb nicht nach unten korrigiert** und bleibt bei rund 19 Wochen (Mitte bis Ende Januar 2027).

---

## 5. Sicherheitsgrenzen (REGELN §3) - eine Grenze gerissen

| Grenze | Wert | Status |
| --- | --- | --- |
| Kalorien nie unter Grundumsatz 1.902 kcal | Ø 2.208 kcal, Minimum 1.860 kcal (07.09.) | Ø eingehalten, **ein Einzeltag 42 kcal darunter** |
| Defizit max. 15 % des TDEE (max. 397 kcal) | Ziel 2.250 = 400 kcal = 15,09 % | bekannter Randfall, unveraendert |
| Abnahme max. 0,6 %/Woche | nominal -1,02 % | nominal gerissen, als Block-Artefakt eingeordnet (Abschnitt 2) |
| **Protein nie unter 1,8 g/kg** | **Ø 150,87 g gegen Untergrenze 151,2 g** | **UNTERSCHRITTEN** |

```
Untergrenze = 1,8 g/kg x 84,02 kg (Ø Gewicht KW37) = 151,2 g
Ø Protein KW37                                     = 150,87 g
Differenz                                          = -0,4 g/Tag
Tage unter der Grenze: 10.09. (131,5 g), 12.09. (95,0 g)
```

Die Unterschreitung im Wochenmittel ist mit 0,4 g winzig. Entscheidend ist nicht der Mittelwert, sondern der Abstand zum eigentlichen Ziel von 175 g (-24 g/Tag) und der Ausreisser vom 12.09. mit 95 g - das sind 1,13 g/kg und deutlich unter allem, was im Defizit vertretbar ist. **In Verbindung mit der erstmals fallenden Muskelmasse ist das der wichtigste Befund dieser Woche.**

---

## 6. Training

**4 Krafteinheiten in KW37** (07., 09., 11., 13.09.) plus Tennis am 12.09. Soll erreicht, zweite Woche in Folge. 65 Arbeitssaetze. Trainingsvolumen faellt nicht (KW35 3 Einheiten, KW36 4, KW37 4).

### Wochenvolumen gegen die Prioritaeten (direkter Satz 1,0 / indirekte Beteiligung 0,5)

| Muskelgruppe | Saetze | Ziel | Status |
| --- | --- | --- | --- |
| Seitliche Schulter | 14,0 | 14-18 | erreicht (untere Kante) |
| Brust | 14,0 | 10-14 | erreicht (obere Kante) |
| Trizeps | 12,0 | 10-14 | erreicht |
| Bizeps | 7,5 | 4-10 | erreicht |
| Lat | 8,0 | 10-14 | verfehlt (-2) |
| Bauch | 9,0 | 10-14 | verfehlt (-1) |
| Hintere Schulter | 4,0 | 8-12 | verfehlt (-4) |
| Beine | 3,0 | 4-10 | verfehlt (-1) |
| **Ruecken / Rudern** | **1,0** | 8-12 | **verfehlt (-7)** |

Die Push-Prioritaeten sitzen. Die Zug- und Ruecken-Seite ist die Luecke: ein einziger Rudersatz in der ganzen Woche, dazu nur 4 Saetze hintere Schulter. Genau davor warnt der Merkzettel-Eintrag vom 07.09. (Risiko Schulterdysbalance und reiner Spiegelmuskel-Aufbau).

### e1RM je Reihe (Uebung + Gym + Geraet)

- **Seitheben Kurzhantel | Schwester:** 28.08. 7,0 -> 03.09. 7,5 -> 06.09. 7,0. **Flach ueber drei Einheiten**, Last seit 21.08. unveraendert bei 5 kg. Das loest die Meldepflicht aus REGELN §6 aus. Am 09.09. (5 Saetze) und 11.09. (6 Saetze am Kabel) ist das **Volumen** gestiegen, die **Last** nicht.
- **Seitheben Kabelzug | Schwester:** neue, eigene Reihe seit 11.09. (11.09. 7,0 -> 13.09. 7,0, ebenfalls 5 kg). Wird nicht mit der Kurzhantelreihe vermischt.
- **Schraegbankdruecken gefuehrt Loch 1 | Schwester:** 03.09. 40,0 -> 11.09. 40,0 bei 30 kg/Seite. Zwei Einheiten unveraendert - noch keine Meldepflicht, aber zu beobachten.
- **Cable Flies | Schwester:** 26,5 -> 25,5 -> 28,5 -> 28,5. Aufwaerts.
- **Schulterpresse gefuehrt | Schwester:** 03.09. 20,0 -> 06.09. 20,0. Der Wert vom 28.08. (14,5 bei 10 kg) liegt unter dem Arbeitsgewicht von 15 kg und ist als Einstellfehler aus der Reihe genommen. Seit 06.09. sieben Tage nicht mehr trainiert - noch unter der 14-Tage-Schwelle.
- **Bizeps Curls SZ-Stange | Schwester:** 03.09. 14,0 -> 07.09. 13,5. Leicht fallend ueber zwei Einheiten.
- **Butterfly Maschine | Freundin:** Reihe startet am 09.09. neu (94,5 bei 70 kg/Seite). Der Wert vom 01.09. (55 kg, ohne Saetze und Wdh) ist als Vergleichsbasis wertlos - siehe Merkzettel vom 09.09.
- **Neue Reihen ohne Verlauf:** Bankdruecken frei Langhantel | Freundin (09.09., e1RM 40,0), Trizepsdruecken Kabel | Freundin (09.09., 36,0).

### Uebungsnamen weiterhin zersplittert (REGELN §6)

Das Problem aus dem letzten Review besteht fort und hat neue Faelle dazubekommen:

- **Bankdruecken-Reihe:** "Bankdruecken" (24.08.) / "Bankdrücken geführt" (28.08.) / "Schraegbankdruecken gefuehrt Loch 1" (03.09., 11.09.)
- **Seitheben:** "Seitheben" (28.08.) gegen "Seitheben Kurzhantel" (sonst) - reine Schreibvariante
- **Ab-Roller:** "Ab-Roller" (28.08.) gegen "Ab Rollout" (24.08., 25.08., 03.09., 06.09.)
- **Schulterpresse:** "Schulterpresse geführt" (28.08.) gegen "Schulterpresse gefuehrt" (sonst)
- **Trizeps am Seil:** "Trizepsdruecken Seil" (24.08.) / "Trizeps Ueberkopfstrecken Seil" (02.09.) / "Trizeps Ueberkopf Seil" (11.09.)

Diese Zeilen werden **nicht** eigenmaechtig umbenannt (REGELN §2: nur anhaengen). Sie brauchen eine ausdrueckliche Freigabe.

---

## 7. Die eine Anpassung fuer KW38

> **Protein zurueck auf 175 g pro Tag - und kein Tag unter 151 g.**

Begruendung: Es ist die einzige Sicherheitsgrenze, die diese Woche echt und nicht nur artefaktbedingt gerissen wurde (150,87 g gegen 151,2 g Untergrenze, Ziel 175 g). Sie faellt mit dem ersten fallenden Muskelmasse-Zeitraum zusammen. Nach der eigenen Rangfolge (Muskeln vor Tempo, REGELN §3) hat das Vorrang vor allem anderen - auch vor der Seitheben-Last und vor der Ruecken-Luecke, die beide ueber die Regeln nachgezogen werden statt als Wochenanpassung.

Praktisch: An den beiden Problemtagen (10.09. und 12.09., beide mit auswaerts essen) war Protein das, was wegfiel. Ein Shake (40 g Protein, 180 kcal) an solchen Tagen schliesst die Luecke fast vollstaendig und passt ins Kalorienbudget - die Woche lag mit 2.208 kcal ohnehin 42 kcal unter Ziel.

**Nebenbedingungen** (keine eigenen Anpassungen, nur Mitlaufen):

1. Erfassungsniveau von KW37 halten - 5 Esstage und 5 Wiegungen, dann ist die TDEE-Korrektur am 20.09. zum ersten Mal rechenbar.
2. Wiegezeit zurueck ins Fenster 06:30-08:00 (Drift 06:39 -> 08:05 -> 08:41).

---

## 8. Offene Punkte, die eine Freigabe brauchen

1. **Uebungsnamen vereinheitlichen** (Liste in Abschnitt 6). Ohne das gibt es fuer die wichtigste Drueckuebung weiterhin keinen durchgaengigen e1RM-Verlauf.
2. **Caliper-Messung** steht weiter aus. Davon haengt die Neubestimmung des BIA-Versatzes (+4,5 Punkte) und die gesamte Zeitplanung bis 14 % ab.
3. **Brust / Nippelwulst** aerztlich abklaeren - unveraendert offen. Der Cut wird deswegen nicht verschaerft.
4. **Ruecken- und Ruderlast**: 1 Satz Rudern in einer ganzen Woche. Ob die Prioritaeten "Ruecken/Rudern 8-12" und "hintere Schulter 8-12" so gelten sollen, ist noch nicht von Simon bestaetigt (siehe Merkzettel 07.09.).
5. **Bandstaerke des Klimmzug-Gummibands** und **Stangengewicht der Langhantel bei der Freundin** sind unbekannt und begrenzen die Aussagekraft dieser Reihen.

---

*Erstellt am 2026-09-13 als geplantes Wochenreview. Rechenweg mit Python/pandas, Rohdaten aus Notion.*

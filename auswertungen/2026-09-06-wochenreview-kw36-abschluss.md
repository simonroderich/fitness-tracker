# Wochenreview KW36 (Abschluss)

- **Datum:** 2026-09-06
- **Art:** Wochenreview
- **Zeitraum:** 2026-08-16 bis 2026-09-06 (21-Tage-Fenster); auswertbare Esstage nur 21.-28.08., 03.09. und 06.09.

> **Kurzfazit:** Keine inhaltliche Anpassung - die Datenlage laesst keine zu. TDEE-Korrektur nach REGELN 8 zum zweiten Mal gesperrt: nur 10 erfasste Esstage in 17 moeglichen, in der aktuellen Woche 2 statt 5, und nur 4 Wiegungen statt 5. Ein gleitender 7-Tage-Schnitt existiert nicht (laengste lueckenlose Wiegereihe: 5 Tage), also kein Gewichtstrend - nur der Blockvergleich 83,95 -> 84,89 kg, der wegen der Luecke 30.08.-02.09. nichts beweist. Sicherheitsseite unauffaellig: Muskelmasse 65,65 -> 66,22 kg im Mittel, kein Abbruchgrund, Defizit bleibt. Zwei harte Befunde: (1) Die Gewichtszeile 23.08. 84,5 kg traegt UNGUELTIG mitten in der Notiz statt am Anfang und rutscht dadurch durch jeden Filter - bitte in Notion korrigieren. (2) Die Bankdrueck-Reihe ist ueber vier Uebungsnamen zersplittert und damit als e1RM-Verlauf wertlos. Merkzettel: alle 3 offenen Zeilen in REGELN uebernommen (v1.5 -> v1.6), inkl. TDEE 2.650 und Waagen-Versatz +4,5 Punkte, die bisher nur in STAND.md standen. Die eine Anpassung fuer KW37: 5 lueckenlose Esstage, notfalls grob.

*Aus Notion übernommen am 2026-10-21. Historisches Dokument — Regeln und Zahlen darin können überholt sein.*

---

## 0. Rahmen

Review vom **Sonntag, 06.09.2026** (19:48 Uhr). Zweites Review in KW36 — das erste lief am 03.09. (Merkzettel-Nachholung), deshalb der Titelzusatz.

Gelesene Tabellen: Gewicht, Ernährung, Training, Merkzettel, Auswertungen. Zeitraum je Abfrage per `WHERE` auf **2026-08-16 bis 2026-09-06** begrenzt, Zeilen mit `Notiz LIKE 'UNGUELTIG%'` ausgeschlossen. Rechnungen mit Python/pandas.

---

## 1. Datenlage — der eigentliche Befund

|  | Soll (REGELN §8.4) | Ist |
| --- | --- | --- |
| Tage Daten | ≥ 21 | **17** (erster Eintrag 21.08.) |
| Esstage 24.–30.08. | ≥ 5 | 5 ✔ |
| Esstage 31.08.–06.09. | ≥ 5 | **2** ✘ (03.09. und der laufende 06.09.) |
| Wiegungen 24.–30.08. | ≥ 5 | 5 ✔ |
| Wiegungen 31.08.–06.09. | ≥ 5 | **4** ✘ |

**Tage ganz ohne Ernährungseintrag:** 29.08., 30.08., 31.08., 01.09., 02.09., 04.09., 05.09. — sieben Stück. 10 erfasste Esstage von 17 möglichen.

Das ist derselbe Befund wie am 03.09. Die damalige Anpassung („lückenlose Erfassung") hat **nicht** gewirkt: in der Woche danach kamen zwei Esstage dazu, einer davon ist der heutige, noch laufende Tag.

---

## 2. Ernährung

| Woche | Esstage | Ø kcal | Ø Protein | Ø KH | Ø Fett | Ø Ballast |
| --- | --- | --- | --- | --- | --- | --- |
| 24.–30.08. | 5 | 2.436 | 164 g | 168 g | 119 g | 21 g |
| 31.08.–06.09. | 2 | 2.221 | 151 g | 179 g | 95 g | 30 g |

Der zweite Wert steht auf **zwei** Tagen, davon einer unvollständig (06.09., bis 19:48 Uhr erst 1.733 kcal). Ohne den laufenden Tag bleibt **ein einziger** vollständiger Esstag in dieser Woche: 03.09. mit 2.709 kcal. Ein Wochendurchschnitt ist das nicht.

**Datenqualität:** `Geschaetzt = __YES__` bei **95 von 110 Zeilen = 86 %** — weit über der 40-%-Schwelle aus REGELN §8.2. Zusätzlich 25 % der Zeilen mit Konfidenz *niedrig*.

**Verzerrung (REGELN §4):** Bei niedriger Konfidenz wird bewusst nach oben gerundet und Brat-/Streichfett pauschal mitgerechnet. Die kcal-Summen sind daher **systematisch nach oben verzerrt**. Ein Ø über dem Ziel ist kein Beweis für ein zu kleines Defizit.

**Protein:** an den erfassten Tagen im Mittel 164 g bzw. 151 g gegen ein Ziel von 175 g. Die Untergrenze von 1,8 g/kg (= 153 g) wird an einzelnen Tagen unterschritten (26.08. 149 g, 27.08. 150 g). Bei 10 von 17 erfassten Tagen ist das aber eher eine Aussage über die Erfassung als über das Essen.

---

## 3. Gewicht

Nur Morgenmessungen, Navy-Zeile und die Doppelmessung vom 23.08. ausgeschlossen.

```
17.–23.08.:    n=2   Ø 84,100 kg   (22., 23.08.)
24.–30.08.:    n=5   Ø 83,950 kg   (24., 25., 26., 28., 29.08.)
31.08.–06.09.: n=4   Ø 84,888 kg   (03., 04., 05., 06.09.)
Δ = +0,938 kg
```

**Längste lückenlose Wiegereihe: 5 Tage.** Nach REGELN §5 gibt es damit **keinen gleitenden 7-Tage-Durchschnitt und keinen Gewichtstrend**. Der Blockvergleich oben wird hier ausdrücklich *nicht* als Trend verkauft: zwischen den beiden Blöcken liegt die Lücke 30.08.–02.09., im ersten Block fehlen die letzten beiden Tage, und am 29.08. lag eine Hochzeit mit Alkohol.

Was man sagen kann: das Gewicht ist gegenüber Ende August **nicht gefallen**. Bei einem angesetzten Defizit von 400 kcal wäre nach zwei Wochen rund −0,7 kg zu erwarten gewesen. Ob das an der Erfassungslücke, am Wasserhaushalt oder an einem zu hoch geschätzten TDEE liegt, lässt sich mit 10 Esstagen nicht trennen — genau dafür gibt es die Bedingungen in §8.4.

---

## 4. Körperanalyse und Sicherheitsprüfung

| Datum | kg | KFA % | Fett kg | FFM kg | Muskel kg | Wasser % |
| --- | --- | --- | --- | --- | --- | --- |
| 28.08. | 84,20 | 16,3 | 13,7 | 70,5 | 65,8 | 61,4 |
| 29.08. | 83,55 | 16,0 | 13,4 | 70,2 | 65,5 | 61,6 |
| 03.09. | 84,65 | 16,0 | 13,5 | 71,1 | 66,3 | 61,5 |
| 04.09. | 84,95 | 16,0 | 13,6 | 71,4 | 66,6 | 61,6 |
| 05.09. | 85,10 | 17,0 | 14,5 | 70,6 | 65,9 | 60,9 |
| 06.09. | 84,85 | 16,5 | 14,0 | 70,8 | 66,1 | 61,2 |

**6 Messungen, 9 Tage seit Baseline.** REGELN §5 verlangt 4 Wochen **und** ≥ 12 Messungen für eine Aussage zum KFA-Trend → **zu früh**. Der KFA-Ausschlag am 05.09. läuft parallel zum Körperwasser (61,6 → 60,9 %) und bei abweichender Messzeit (09:53 statt 06:49–07:41) — Hydrationsartefakt, kein Fettaufbau.

**Sicherheitsprüfung Muskelmasse (REGELN §3 — der Vorrang der Muskelmasse):**

```
Zeitraum 1 (28./29.08.):  Ø 65,65 kg
Zeitraum 2 (03.–06.09.):  Ø 66,22 kg
Δ = +0,57 kg
```

→ **Kein Abbruchgrund.** Die Muskelmasse fällt nicht über zwei Messzeiträume, das Defizit wird nicht reduziert. Einschränkung: das Körperwasser bewegt sich im selben Fenster mit (61,4 → 61,2 %, dazwischen 61,6) — nach REGELN §5 ist ein Muskelanstieg bei mitlaufendem Wasser **keine Erfolgsmeldung**, sondern nur die Feststellung, dass nichts wegbricht.

**Weitere Grenzen (REGELN §3):**

- Gewichtsabnahme ≤ 0,6 %/Woche (= 0,51 kg): eingehalten, es wurde nichts abgenommen.
- Kalorien nie unter Grundumsatz 1.902 kcal: Ziel 2.250 — eingehalten.
- Protein ≥ 1,8 g/kg (= 153 g): Ziel 175 g = 2,06 g/kg — eingehalten.
- Defizit ≤ 15 % des TDEE: **knapp gerissen.** 2.650 − 2.250 = 400 kcal = **15,09 %**. Die Grenze liegt bei 397,5 kcal, das regelkonforme Minimalziel bei 2.253 kcal. Differenz: 2,5 kcal. Gegenüber der Schätzunsicherheit des TDEE ist das bedeutungslos, aber es ist ein Verstoß gegen die eigene Regel und steht jetzt als bekannter Randfall in REGELN §3. Die dort bisher genannte Obergrenze „max. 420 kcal" stammte noch vom TDEE 2.800 und wurde auf 397 kcal korrigiert.

---

## 5. TDEE-Korrektur — gesperrt

Formel aus REGELN §8.4:

```
TDEE_real ≈ Ø kcal (14 Tage) − (Δ Ø-Gewicht_kg × 7700) / 14
```

Bedingungen: ≥ 21 Tage Daten, ≥ 5 Wiegungen **und** ≥ 5 Esstage **pro Woche**. Erfüllt: 2 von 5. → **Keine Anpassung. Der TDEE bleibt bei 2.650 kcal, das Tagesziel bei 2.250 kcal.**

Rein illustrativ, ausdrücklich **nicht zur Übernahme**:

```
Ø kcal der erfassten Tage seit 24.08. = 2.374
Δ Ø-Gewicht (Block 2 − Block 1)      = +0,938 kg
TDEE_real = 2.374 − (0,938 × 7700)/14 = 2.374 − 516 = 1.859 kcal
```

Dieser Wert liegt **unter dem Grundumsatz** und ist damit physiologisch unmöglich. Er zeigt genau, warum die Bedingungen existieren: die 2.374 kcal stammen aus 7 von 14 Tagen, die fehlenden 7 Tage sind rechnerisch Nulltage, und das +0,938 kg ist zum Teil die Lücke 30.08.–02.09. mit Hochzeit. Aus so etwas darf kein Zielwert werden.

---

## 6. Training

| Woche | Einheiten | erfasste Sätze | Zeilen ohne Satzangabe |
| --- | --- | --- | --- |
| bis 23.08. | 1 (21.08.) | 6 (Sammelzeilen) | 0 |
| 24.–30.08. | 3 (24., 25., 28.08.) | 24 | 0 |
| 31.08.–06.09. | **4** (01., 02., 03., 06.09.) | 29 | 8 |

Das Soll von 4 Einheiten/Woche ist in KW36 erstmals erreicht. Ein Volumenvergleich in kg ist nicht möglich: `Last gesamt kg` ist fast durchgehend leer (geführte Stange, Eigengewicht unbekannt). Die Meldung „Gesamtvolumen fällt zwei Wochen in Folge" kann mangels Volumendaten nicht geprüft werden — die Satzzahl steigt.

**e1RM je Reihe (Übung + Gym + Gerät), bester Satz je Einheit:**

| Reihe | Verlauf | Δ |
| --- | --- | --- |
| Schulterpresse geführt [Schwester / LH geführt] | 28.08. 14,5 → 03.09. 20,0 → 06.09. 20,0 | +5,5 |
| Cable Flies [Schwester / Kabelzug] | 28.08. 26,5 → 03.09. 25,5 → 06.09. 28,5 | +2,0 |
| Seitheben [Schwester / Kurzhantel] | 21.08. 6,0 → 28.08. 7,0 → 03.09. 7,5 → 06.09. 7,0 | +1,0 |
| Bizeps Curls SZ [Schwester / SZ-Stange] | 21.08. 13,5 → 03.09. 14,0 | +0,5 |

Keine Reihe stagniert oder fällt über 3+ Einheiten. **Keine Meldung nach REGELN §6 fällig.**

Zwei Einschränkungen, die man beim Lesen mitnehmen muss:

- Der 06.09.-Wert der **Cable Flies** (28,5) stammt aus einer Variante an der angelehnten Bank. Vergleichbar mit den Vorwochen ist nur Satz 3 im Stehen: e1RM **26,0**. Damit ist die Reihe eher 26,5 → 25,5 → 26,0, also **flach**, nicht steigend.
- Bei der **Schulterpresse** waren am 06.09. drei von vier Sätzen unter dem Arbeitsgewicht (7,5 / 10 / 12,5 statt 15 kg pro Seite) — versehentlich zu leicht eingestellt. Nur der vierte Satz (15 kg, e1RM 20,0) zählt. Ist in der Zeile korrekt vermerkt und jetzt auch als Regel in REGELN §3/§6 verankert.

**Sprünge über 20 % beim Arbeitsgewicht:** dreimal in der Schulterpresse-Reihe (7,5 → 15 → 10 → 15 kg). Das sind keine echten Sprünge, sondern die Einstellfehler oben plus fehlende Wdh-Angaben in den Altchat-Zeilen. Mit der neuen Arbeitsgewichts-Tabelle sollte das künftig sauber trennbar sein.

**Übung seit über 14 Tagen nicht mehr aufgetaucht:** „Bankdruecken gefuehrt schraeg" (zuletzt 21.08., 16 Tage). Das ist mit hoher Wahrscheinlichkeit **kein** Aussetzer, sondern der Namensfehler aus Abschnitt 7.

**Cardio:** erster erfasster Lauf am 06.09., 6:27 min/km im Schnitt, Splits 5:52 / 6:23 / 6:15 / 7:23 — deutlich negative Split-Struktur, das Tempo bricht am Ende ein. Ein Datenpunkt, keine Aussage. Die 356 kcal der App werden korrekt **nicht** vom Tagesbudget abgezogen.

---

## 7. Datenfehler, die eine Korrektur in Notion brauchen

**(1) `UNGUELTIG` an der falschen Stelle — Tabelle Gewicht, 23.08., 84,5 kg.**

Die Notiz lautet „aus Altchat - vor dem Klo - UNGUELTIG doppelt gemessen siehe Folgezeile". Das Schlüsselwort steht **mitten im Text**, nicht am Zeilenanfang. Der Filter `NOT LIKE 'UNGUELTIG%'` greift damit nicht — die Zeile rutscht in jede automatische Auswertung und verfälscht sie (hier: zwei Werte für den 23.08.). In diesem Review wurde sie manuell entfernt. **Bitte in Notion die Notiz so umstellen, dass sie mit `UNGUELTIG` beginnt** (Regel: REGELN §2). Bestehende Zeilen werden ohne ausdrückliche Anweisung nicht angefasst, deshalb bleibt sie vorerst stehen.

**(2) Die Bankdrück-Reihe ist über vier Namen zersplittert.**

| Datum | Übungsname | e1RM |
| --- | --- | --- |
| 21.08. | Bankdruecken gefuehrt schraeg | 38,0 |
| 24.08. | Bankdruecken | — (keine Wdh) |
| 28.08. | Bankdrücken geführt | 38,0 |
| 03.09. | Schraegbankdruecken gefuehrt Loch 1 | 40,0 |
| 06.09. | Schraegbankdruecken gefuehrt Loch 2 | 36,0 |

Alles dieselbe geführte Langhantel im Gym der Schwester, alles 25–30 kg pro Seite. Für die Auswertung sind das fünf getrennte Reihen mit je einer Einheit — **der Verlauf der wichtigsten Druckübung ist damit nicht auswertbar**. Loch 1 und Loch 2 gehören zu Recht getrennt (anderer Winkel), die übrigen drei sind reine Schreibvarianten. Vorschlag: die Zeilen vom 21.08., 24.08. und 28.08. auf **einen** Namen vereinheitlichen — vermutlich `Schraegbankdruecken gefuehrt Loch 1`, falls es damals derselbe Winkel war. Das ist eine Korrektur bestehender Zeilen und braucht deshalb eine ausdrückliche Freigabe.

Die Regel dazu (`Uebung` je Reihe konstant halten) steht ab v1.6 in REGELN §6 und §7.7.

**(3) Kleinigkeit:** In der Tabelle Ernährung steht am 03.09. beim KoRo-Snack noch die offene Rückfrage, welcher der drei Snacks es war (Bohnen-Erbsen-Mix angenommen). Betrifft 639 kcal an einem der wenigen erfassten Tage.

---

## 8. Merkzettel — 3 offene Zeilen, alle abgearbeitet

| Zeile | Entscheidung | Wohin |
| --- | --- | --- |
| Waagen-Versatz +4,5 Punkte (05.09.) | **in REGELN uebernommen** | §5 neuer Abschnitt „Versatz der BIA-Waage"; Zielkonflikt in §3 zugunsten ~21 % aufgelöst |
| Arbeitsgewichte / keine Aufwärmsätze (06.09.) | **in REGELN uebernommen** | §3 neue Tabelle „Arbeitsgewichte je Übung", Konsequenz für e1RM in §6 |
| TDEE 2.650 (06.09.) | **in REGELN uebernommen** | §3 Tageszielwerte und Sicherheitsgrenzen komplett umgestellt |

Wichtig dabei: **REGELN.md**** stand bis heute noch auf TDEE 2.800 / Ziel 2.500.** Die neuen Werte existierten nur in `STAND.md`. Ein Chat, der nur REGELN gelesen hätte, hätte mit dem alten Ziel gerechnet. Das ist jetzt behoben.

**Abweichung dokumentiert:** Der Merkzettel-Eintrag nennt Tagesziel **2.350** (Defizit 300), `STAND.md` vom selben Tag nennt **2.250** (Defizit 400) auf Simons ausdrücklichen Wunsch. Übernommen wurde die jüngere Festlegung (2.250). Die zugehörige Vorrangregel steht jetzt in REGELN §12.

REGELN.md: **v1.5 → v1.6**, Änderungsprotokoll ergänzt.

---

## 9. Die eine Anpassung für KW37

> **Fünf lückenlose Esstage — notfalls grob.**

Es gibt weiterhin keine Zahl, die man ohne Daten seriös verändern könnte. Nach REGELN §8.8 ist die Anpassung deshalb erneut die Erfassung selbst. Weil dieselbe Anpassung letzte Woche wirkungslos blieb, diesmal mit einer konkreten Erleichterung statt derselben Aufforderung:

- **Ziel sind 5 Tage, nicht 7.** Vollständigkeit an fünf Tagen schlägt Halbheit an sieben.
- **Grob zählt.** Ein Tag mit drei Zeilen „Frühstück wie immer, Döner mittags, abends Reis mit Hähnchen" ist auswertbar; ein Tag ohne jeden Eintrag ist es nicht. Bei 86 % geschätzten Zeilen kostet eine weitere grobe Schätzung fast nichts an Genauigkeit — ein fehlender Tag kostet dagegen die ganze TDEE-Korrektur.
- **Täglich wiegen bleibt Nebenbedingung** (aktuell 4 statt 5 pro Woche). Ohne 5 Wiegungen scheitert §8.4 auch bei perfekter Ernährungserfassung.

Erst wenn das steht, ist die datenbasierte TDEE-Korrektur möglich — und erst dann lässt sich die Frage beantworten, ob 2.650 kcal die richtige Annahme ist. Bis dahin gilt der geschätzte Wert.

**Zusätzlich offen (nicht die Anpassung, aber der nächste inhaltliche Schritt):** die Caliper-Messung. Sie ist der dritte Datenpunkt, der den Waagen-Versatz von +4,5 Punkten bestätigt oder kippt — und davon hängt die gesamte Zeitplanung bis 14 % KFA ab.

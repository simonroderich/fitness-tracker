# STAND

*Beim Sessionstart zuerst lesen, danach REGELN.md.*

**Letzte Aktualisierung:** 2026-10-21 (Umzug von Notion ins Repo, REGELN v1.25)

**Diese Datei enthält absichtlich fast keine Messwerte mehr.** Zahlen
veralten, diese Datei wird nicht turnusmäßig überschrieben, und
veraltete Zahlen hier haben schon zu falschen Aussagen im Chat geführt.
Hier stehen nur Dinge, die sich selten ändern: Zugänge, Konventionen,
der Übungskatalog und offene Fragen. **Alle Zahlen kommen aus `daten/`.**

---

## 1. Datenablage

Alle Daten liegen in diesem Repo (`simonroderich/fitness-tracker`), Ordner
**`daten/`**. Seit 21.10.2026 — vorher Notion, Seite „Fitness Tracker". Die
Notion-Seite bleibt als Archiv stehen, wird aber nicht mehr benutzt.

| Datei | Inhalt | Titelspalte | Zeilen beim Umzug |
|---|---|---|---|
| `daten/gewicht.csv` | Wiegungen inkl. Körperanalyse | `Eintrag` | 50 |
| `daten/training.csv` | eine Zeile pro Satz bzw. Übung | `Eintrag` | 471 |
| `daten/ernaehrung.csv` | eine Zeile pro Lebensmittel (ruht seit 13.10.) | `Item` | 400 |
| `daten/festwerte.csv` | Festwerte pro 100 g | `Produkt` | 16 |
| `daten/merkzettel.csv` | Auffanglager, REGELN §12 | `Was` | 38 |
| `daten/auswertungen.csv` | Index der Auswertungen | `Titel` | 5 |
| `auswertungen/*.md` | Volltexte der Auswertungen | — | 5 |

Jede Datei hat als letzte Spalte `notion_id` (ID der alten Notion-Zeile,
bei neuen Zeilen leer). Spalten sonst wie in REGELN §4–§6.

**Ohne Repo-Zugriff mit Push-Recht geht nichts** — dann sofort sagen und
nichts eintragen.

### Technische Fallen

- CSV immer mit dem `csv`-Modul bzw. pandas schreiben, nie per Hand —
  Notizen enthalten Kommas und Anführungszeichen.
- `Geschaetzt` steht als `ja` / `nein`.
- UNGUELTIG-Filter: `df[~df["Notiz"].fillna("").str.startswith("UNGUELTIG")]`.
- Vor jedem Commit `python3 werkzeuge/pruefen.py`, danach pushen. Nicht
  gepusht = nicht gespeichert.
- Die Notion-Fallen von früher (SQL-Kontingent, 100-Zeilen-Limit, eine
  Tabelle pro Abfrage, `parent`-Pflicht) gibt es im Repo nicht mehr.

---

## 2. Was aktuell getrackt wird — und was nicht

| Bereich | Status |
|---|---|
| **Gewicht / BIA** | läuft unverändert, jede Wiegung eintragen |
| **Training** | **vereinfacht seit 21.10.2026** (REGELN v1.24) |
| **Ernährung** | **eingestellt seit 13.10.2026** (REGELN v1.20) |

Zum Training: Simon meldet, was er will, eine Zeile pro Übung mit der Last
genügt. Wiederholungen und Sätze nur, wenn er sie von selbst nennt.
**Nicht nachfragen** — weder nach Wiederholungen, Sätzen, Gym, Loch, Griff
oder Bandstärke, noch nach ausgelassenen Einheiten oder Lücken. Fehlt
etwas, bleibt das Feld leer und die Zeile ist eine Volumenzeile.

**Keine laufende Kraftauswertung mehr:** keine Reihenvergleiche, keine
Höchstwert- oder Rekordmeldungen, keine Volumenbilanz pro Muskelgruppe,
keine Meldung über flache oder fallende Reihen oder über Reihen ohne
Eintrag seit X Tagen. Unaufgefordert gemeldet wird nur noch: wenn Simon
fragt; wenn ein Eintrag in sich falsch oder widersprüchlich wäre (dann ist
**eine** Rückfrage erlaubt, statt zu raten); wenn die Last einer Übung
deutlich unter der letzten Einheit derselben Übung liegt (ein Satz, keine
Analyse); und die §5-Prüfungen zur Körperanalyse samt den vier Ausnahmen
aus v1.18.

Der **Übungskatalog unten und die Nachschlagepflicht aus v1.23 gelten
weiter** — sie kosten Simon keine Arbeit und verhindern genau die Fehler,
wegen derer am 17.10. aufgeräumt werden musste.

Zur Ernährung: keine Zeilen anlegen, außer Simon erzählt von selbst
etwas. **Nicht fragen, was er gegessen hat. Keine Tage nachrechnen.
Nicht nach Protein fragen und nicht dazu mahnen.** Die Protein-Untergrenze
von 151 g und die Grundumsatz-Untergrenze von 1.902 kcal sind ausgesetzt,
ebenso die TDEE-Korrektur und das feste Wochenreview (abgeschafft am
04.10.). **Protein-Minimalerfassung wurde am 13.10. von Simon abgelehnt —
nicht erneut anbieten.**

Die Verlustrate von 0,6 %/Woche wird weiter **berechnet und in der
Gewichts-Notiz dokumentiert**, aber **nicht im Chat gemeldet und nie mit
einem Korrekturvorschlag verbunden** (REGELN v1.18). Unaufgefordert
gemeldet wird nur: Rate über 1,5 %/Woche; das §5-BIA-Muster
(Muskelmasse fällt bei steigendem Körperwasser) an drei Wiegungen in
Folge; ein e1RM-Serienhoch, das über drei Einheiten fällt; oder wenn
Simon fragt.

**Laststeuerung macht Simon selbst** (Ansage 28.09.). Keine
Gewichtsempfehlungen ohne Aufforderung.

---

## 3. Übungskatalog — VOR JEDEM TRAININGSEINTRAG HIER NACHSEHEN

Stand 17.10.2026, 45 Reihen, 442 Zeilen (inzwischen 471 Zeilen; Reihen seit 17.10. siehe `daten/training.csv`). **Eine Reihe ist nach REGELN §6
die Kombination Übung + Gym + Gerät.** Die Spalte „Gewicht kg" ist
immer die Angabe **pro Seite / pro Hantel**, nicht die Gesamtlast.

**Warum diese Liste existiert:** am 17.10. habe ich Seitheben am
Kabelzug als „neue Reihe" eingetragen, obwohl die Reihe seit dem
11.09. mit 20 Zeilen bestand. Ich hatte den Bestand nicht abgefragt.
Simon hat den Fehler gefunden, nicht ich. Dasselbe war vorher bei den
Cable Flies passiert. **Namen nie aus dem Gedächtnis vergeben.**

| Uebung | Geraet | Gym | Gewicht kg | Tage | erster | letzter |
|---|---|---|---|---|---|---|
| Ab Rollout | Koerpergewicht | Freundin/Schwester | - | 10 | 21.08. | 12.10. |
| Bankdruecken frei Langhantel | Langhantel frei | Freundin | 30 | 1 | 09.09. | 09.09. |
| Bizeps Curls SZ-Stange | SZ-Stange | Freundin/Schwester | 10-11,25 | 8 | 21.08. | 15.10. |
| Butterfly Maschine | Maschine | Freundin | 55-65 | 7 | 01.09. | 13.10. |
| Butterfly Maschine Sitz hoch | Maschine | Freundin | 65 | 1 | 09.09. | 09.09. |
| Cable Crunch | Kabelzug | Schwester | 35 | 1 | 14.09. | 14.09. |
| Cable Flies sitzend | Kabelzug | Schwester | 20 | 1 | 28.09. | 28.09. |
| Cable Flies stehend | Kabelzug | Schwester | 20 | 7 | 21.08. | 13.09. |
| Cable Flies stehend vorgebeugt nach unten | Kabelzug | Schwester | 20 | 1 | 17.10. | 17.10. |
| Handgelenk-Curls Kurzhantel links | Kurzhantel | Schwester | 5 | 1 | 13.10. | 13.10. |
| Handgelenk-Curls Kurzhantel rechts | Kurzhantel | Schwester | 5 | 1 | 13.10. | 13.10. |
| Katana Extension Kabelzug beidhaendig | Kabelzug | Schwester | 20 | 6 | 02.09. | 28.09. |
| Katana Extension Kabelzug einarmig links | Kabelzug | Schwester | 10 | 6 | 11.09. | 13.10. |
| Katana Extension Kabelzug einarmig rechts | Kabelzug | Schwester | 10 | 6 | 11.09. | 13.10. |
| Klimmzuege breit mit Gummiband | Koerpergewicht | Schwester | - | 1 | 07.09. | 07.09. |
| Klimmzuege neutral schulterbreit mit Gummiband | Koerpergewicht | Schwester | - | 4 | 13.09. | 02.10. |
| Kreuzheben gefuehrt | Langhantel gefuehrt | Schwester | 10 | 1 | 15.10. | 15.10. |
| Lat Pulldown Kabelzug breiter Griff | Kabelzug | Freundin | 105-110 | 2 | 08.10. | 15.10. |
| Lat Pulldown Kabelzug einarmig Seite unbekannt | Kabelzug | Schwester | - | 1 | 07.09. | 07.09. |
| Lat Pulldown Kabelzug einarmig links | Kabelzug | Schwester | 25 | 1 | 14.09. | 14.09. |
| Lat Pulldown Kabelzug einarmig rechts | Kabelzug | Schwester | 25 | 1 | 14.09. | 14.09. |
| Lat Pulldown Kabelzug neutral schulterbreit | Kabelzug | Schwester | 50-60 | 3 | 22.09. | 15.10. |
| Laufen Hausstrecke | Koerpergewicht | anderes | - | 2 | 06.09. | 27.09. |
| Leg Extensions Maschine | Maschine | Freundin | 35 | 1 | 28.09. | 28.09. |
| Motorschirmfliegen | - | anderes | - | 1 | 06.09. | 06.09. |
| Preacher Curls SZ-Stange | SZ-Stange | Schwester | 7,5 | 2 | 26.09. | 02.10. |
| Reverse Butterfly Kabelzug | Kabelzug | Schwester | 5-6,15 | 5 | 07.09. | 02.10. |
| Reverse Butterfly Maschine | Maschine | Freundin | 35-48 | 3 | 06.10. | 15.10. |
| Reverse Crunch | Koerpergewicht | Freundin/Schwester | - | 12 | 06.09. | 05.10. |
| Reverse Handgelenk-Curls Kurzhantel links | Kurzhantel | Schwester | 5 | 1 | 13.10. | 13.10. |
| Reverse Handgelenk-Curls Kurzhantel rechts | Kurzhantel | Schwester | 5 | 1 | 13.10. | 13.10. |
| Rudern Kabelzug 45 Grad von oben vorne | Kabelzug | Schwester | - | 1 | 07.09. | 07.09. |
| Rudern Kabelzug enger Griff | Kabelzug | Freundin | 105 | 3 | 02.10. | 07.10. |
| Rudern Kabelzug hueftbreite Stange | Kabelzug | Schwester | - | 1 | 02.09. | 02.09. |
| Rudern Kabelzug neutral schulterbreit | Kabelzug | Schwester | 50 | 2 | 22.09. | 25.09. |
| Schraegbankdruecken Kurzhantel | Kurzhantel | Schwester | 39 | 1 | 28.09. | 28.09. |
| Schraegbankdruecken gefuehrt Loch 1 | Langhantel gefuehrt | Schwester | 30 | 10 | 21.08. | 17.10. |
| Schraegbankdruecken gefuehrt Loch 2 | Langhantel gefuehrt | Schwester | 25 | 1 | 06.09. | 06.09. |
| Schulterpresse gefuehrt | Langhantel gefuehrt | Schwester | 7,5-15 | 11 | 21.08. | 17.10. |
| Seitheben Kabelzug | Kabelzug | Schwester | 5-6,25 | 5 | 11.09. | 17.10. |
| Seitheben Kurzhantel | Kurzhantel | Freundin/Schwester | 5-6,25 | 19 | 21.08. | 15.10. |
| Shrugs Langhantel gefuehrt | Langhantel gefuehrt | Schwester | 22,5-30 | 3 | 28.09. | 13.10. |
| Squats gefuehrt | Langhantel gefuehrt | Schwester | 10-15 | 4 | 02.09. | 15.10. |
| Tennis | - | anderes | - | 1 | 12.09. | 12.09. |
| Trizeps Pushdown gerade Stange | Kabelzug | Freundin/Schwester | 25 | 4 | 24.08. | 13.10. |

### Namenskonvention

`<Übung> <Gerät> <Variante/Griff> [Seite]`

- Das Gerätewort im Namen muss zum Select-Feld `Geraet` passen. Erlaubte
  Werte: `Langhantel frei`, `Langhantel gefuehrt`, `Kurzhantel`,
  `SZ-Stange`, `Kabelzug`, `Maschine`, `Koerpergewicht`.
- **Immer „Kabelzug", nie „Kabel".**
- Seite als letztes Wort: `links` / `rechts`.
- Einstellungen hinter die Variante: `Loch 1`.
- Keine Umlaute und kein ß in Übungsnamen (`ue`, `oe`, `ae`, `ss`) —
  die Tabelle ist durchgängig so geführt.
- **Titel (`Eintrag`) = `YYYY-MM-DD <Uebung> Satz N`**, bei Zeilen ohne
  Satznummer ohne den Satz-Teil. Durchgängig so hergestellt am 17.10.

### Datenpflege-Stand 17.10.2026

- 59 Zeilen umbenannt (Kabel → Kabelzug, Wortstellung bei Katana,
  Single Arm → einarmig, Tippfehler „huefbreite").
- `Cable Flies` → `Cable Flies stehend` (15 Zeilen), damit die drei
  Cable-Flies-Varianten unterscheidbar sind.
- `Trizepsdruecken Kabel` → `Trizeps Pushdown gerade Stange` (3 Zeilen,
  09.09. bei der Freundin). Gleiche Bewegung, gleiche Last, Simon hatte
  am 24.09. bestätigt, dass er Pushdowns mit gerader Stange macht. Die
  Trennung nach Gym leistet weiter das Feld `Gym`.
- **183 fehlende Satznummern** aus dem Titel rekonstruiert. Die Spalte
  war ab dem 28.09. praktisch nicht mehr gefüllt worden.
- 286 Titel auf das Schema oben gebracht.
- Sechs Notizen korrigiert, deren Aussage überholt oder falsch war
  (Seitheben Kabelzug 17.10., Cable Flies 17.10., Gym-Ableitung am
  05.10. zweimal, Reverse Butterfly 08.10., Shrugs 13.10., Tennis).

**13 Zeilen haben bewusst keine Satznummer**: Altzeilen vom 01./02.09.,
bei denen nur „3 Sätze" ohne Einzelwerte bekannt war, sowie Tennis,
Laufen und Motorschirmfliegen.

**6 Zeilen tragen `UNGUELTIG`** (Sätze, die nicht stattgefunden haben):
Schulterpresse und Cable Flies je Satz 3 am 03.09., sowie die vier
dritten Sätze der Handgelenk-Curls vom 13.10.

---

## 4. Ziel in einem Satz

Muskeln aufbauen, Fett von ihnen runter — **Muskelmasse hat Vorrang vor
Tempo.** Sixpack wäre schön, notfalls später. Details: REGELN §3.

KFA-Einordnung: es gilt die **Bandbreite 16–19 %** (Entscheidung
24.09.), nicht der Waagenwert. Eine zweite Caliper-Messung oder eine
DEXA würde daraus wieder eine Zahl machen.

---

## 5. Offene Fragen an Simon

**Diese Liste wird seit dem 21.10.2026 nicht mehr abgefragt** (REGELN
v1.24). Sie steht hier als Dokumentation dessen, was in den Daten
unsicher ist — damit keine Auswertung so tut, als wäre es geklärt. Simon
kann jederzeit von selbst darauf zurückkommen.

Erledigt am 21.10.: Die Einheiten vom 19.10. und 20.10. liefen beide bei
der Freundin (Angabe Simon). Damit sind auch Griff und Gerät dieser
Einheiten geklärt.

1. **Gibt es das Ausrollrad in beiden Gyms?** Die Zuordnung „Ab Rollout
   = Schwester" war sieben Einheiten lang die Grundlage für geratene
   Gym-Werte und ist am 07.10. widerlegt worden. Betroffen: die
   Vormittagseinheit vom **05.10.** (Gym geraten) und die Einheit vom
   **12.10.** (Gym bewusst leer gelassen, damit nach §6 nicht
   e1RM-vergleichbar).
2. **Seitheben am 17.10.: wirklich am Kabelzug?** 6,25 und 5 kg sind
   genau seine Kurzhantelgewichte, Kabelstapel haben selten
   1,25-kg-Stufen. Eingetragen ist Kabelzug, weil er das geschrieben hat.
3. **Bizeps Curls am 15.10. bei der Schwester: normal oder Preacher?**
   Als normale Curls eingetragen (11,25 kg passt zur 10-kg-Reihe, die
   Preacher-Reihe läuft mit 7,5 kg).
4. **Butterfly 13.10. mit 60 statt 65 kg** — Absicht? Geklärt ist
   inzwischen nur die Bestückung: seit spätestens 28.10. neue, schmalere
   Platten (Angabe Simon 30.10.), 65 kg pro Seite sind kein Maximum mehr.
5. **Cable Flies 17.10.: bleibt die neue Technik?** Wenn ja, bleibt die
   eigene Reihe. Wenn es ein Versuch war, gehören die drei Zeilen zurück
   zu `Cable Flies stehend`.
6. **Ab der nächsten Kreuzheben-Einheit Wiederholungen mitzählen**, sonst
   bleibt die Reihe dauerhaft nicht auswertbar.
7. Toter Verweis auf „Abschnitt 8.8" in REGELN §5 — gibt es nicht,
   Simon zweimal gefragt, nie beantwortet.
8. Stangengewicht der freien Langhantel bei der Freundin (20 kg
   Olympiastange, 10 kg, anderes?). Ohne das ist die Gesamtlast beim
   freien Bankdrücken nicht ableitbar; dasselbe gilt für alle geführten
   Langhantelübungen.
9. Kabelstation bei der Freundin: zwei getrennte Türme oder einer mit
   zwei Griffen? Simon gibt dort „pro Seite" an. Auffällig: Rudern enger
   Griff und Lat Pulldown breiter Griff laufen beide mit genau 105 kg.
10. Bandstärke des Klimmzug-Gummibands in Farbe oder kg (aktuell nur
    „stark").
11. **Brust / Nippelwulst ärztlich abklären.**

---

## 6. Strukturelle Befunde — dokumentiert, nicht gemeldet

*Seit v1.24 wird keiner dieser Punkte unaufgefordert im Chat
wiederholt. Sie stehen hier, damit die Einschränkungen der Daten bekannt
bleiben, wenn Simon einmal etwas auswerten lässt.*

- **Schulterpresse und Seitheben messen die Position in der Einheit, nicht
  den Fortschritt.** Beide landen regelmäßig hinten im Dreier-Zirkel und
  schwanken deshalb um zwei bis vier Wiederholungen. Solange die Position
  wechselt, ist kein Trend ablesbar. Am 17.10. der sauberste Beleg der
  ganzen Aufzeichnung: längere Pause vor Satz 3 der Schulterpresse → 9
  Wdh gegen 7 im Satz davor.
- **Arbeitshypothese Techniklernphase (15.10.):** die ersten ein bis zwei
  Einheiten einer neuen Übung sind Technik, keine Leistungsbasis; die
  Reihe beginnt praktisch mit der dritten Einheit. Zweimal bestätigt
  (Shrugs, Reverse Butterfly Maschine), beide Male von Simon selbst
  vorhergesagt.
- **22 von 45 Reihen haben genau einen Trainingstag.** Teils gewollt
  (Tests, einmal probiert und verworfen), teils Folge davon, dass ich
  Varianten zu schnell als eigene Reihe angelegt habe. Eine Variante
  gehört zuerst in die Notiz; eine eigene Reihe erst, wenn Simon sie
  wiederholt.
- **Beine bleiben die größte Volumenlücke.** Squats an vier Tagen seit
  dem 21.08., Leg Extensions einmal, Kreuzheben seit dem 15.10. neu.
- **Epley ist über etwa 12 Wiederholungen unbrauchbar.** Bei Sätzen mit
  15 bis 20 Wdh ist ein „neuer e1RM-Höchstwert" ein Formelartefakt und
  muss als solcher benannt werden.

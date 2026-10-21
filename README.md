# Fitness-Tracker

Privates Trainings-, Gewichts- und Ernährungstagebuch, gepflegt mit Claude.

## Aufbau

| Pfad | Inhalt |
|---|---|
| `CLAUDE.md` | Startanweisung für Claude |
| `REGELN.md` | Alle Regeln: Erfassung, Auswertung, Ziele |
| `STAND.md` | Überblick, Übungskatalog, offene Fragen |
| `daten/gewicht.csv` | Wiegungen inkl. Körperanalyse |
| `daten/training.csv` | Trainingssätze |
| `daten/ernaehrung.csv` | Ernährung (ruht seit 13.10.2026) |
| `daten/festwerte.csv` | Nährwerte pro 100 g |
| `daten/merkzettel.csv` | Offene Punkte |
| `daten/auswertungen.csv` | Index der Auswertungen |
| `auswertungen/` | Volltexte der Auswertungen |
| `werkzeuge/pruefen.py` | Prüft die CSVs vor jedem Commit |

## Daten ansehen

- **Am Handy oder im Browser:** auf GitHub eine Datei in `daten/` öffnen —
  CSVs werden als durchsuchbare Tabelle angezeigt.
- **Am PC:** in VS Code (z. B. mit der Erweiterung „Rainbow CSV")
  oder in Excel öffnen.

Bis 21.10.2026 lagen die Daten in Notion (Seite „Fitness Tracker"). Dort
steht noch eine Archivkopie; maßgeblich ist dieses Repo. Die Spalte
`notion_id` verweist auf die alte Notion-Zeile.

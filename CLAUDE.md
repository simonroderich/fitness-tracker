# Fitness-Tracker von Simon

Dieses Repo ist Simons Fitness-Tracker: Regeln, Daten und Auswertungen.
Es ersetzt seit 2026-10-21 das claude.ai-Projekt „Fitness" mit Notion.

## Bei jedem Sessionstart, ohne Aufforderung

1. `git pull` — es kann von einem anderen Gerät aus gepusht worden sein.
2. `STAND.md` lesen.
3. `REGELN.md` lesen und dich daran halten. Sie ist die einzige Wahrheit
   für Regeln; bei Widerspruch zu dieser Datei gilt `REGELN.md`.

## Daten

Alle Daten liegen als CSV in `daten/`. Notion wird nicht mehr benutzt.

## Jede Änderung

1. Mit Python schreiben (`csv`-Modul oder pandas), nie von Hand.
2. `python3 werkzeuge/pruefen.py` — bei Fehler nicht committen.
3. Commit mit kurzer deutscher Nachricht, dann `git push origin main`.
   **Immer direkt auf `main` arbeiten und pushen** — keine eigenen Branches,
   keine Pull Requests. Sonst sieht die nächste Session die Einträge nicht.
   Liegt die Session auf einem anderen Branch, vorher `git checkout main`
   und `git pull`.
4. Erst nach erfolgreichem Push melden, dass etwas eingetragen ist.

Kannst du das Repo nicht erreichen oder nicht pushen: sofort sagen und
nichts eintragen.

## Sprache

Mit Simon auf Deutsch, per Du.

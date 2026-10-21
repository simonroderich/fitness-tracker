"""Prüft alle CSVs in daten/ vor jedem Commit (REGELN §2 und §11).

Aufruf:  python3 werkzeuge/pruefen.py
Exit-Code 0 = alles in Ordnung, 1 = Fehler gefunden (dann nicht committen).
"""
import csv
import re
import sys
from pathlib import Path

DATEN = Path(__file__).resolve().parent.parent / "daten"

SPALTEN = {
    "gewicht.csv": ["Datum", "Eintrag", "Gewicht kg", "Tageszeit", "Messmethode", "KFA Prozent",
                    "Fettmasse kg", "Fettfreie Masse kg", "Muskelmasse kg", "Muskelrate Prozent",
                    "Skelettmuskel kg", "Skelettmuskel Prozent", "Koerperwasser Prozent",
                    "Wassergehalt kg", "Protein Prozent", "Eiweissmenge kg", "Unterhautfett Prozent",
                    "Viszeralfett", "Knochenmasse kg", "WHR", "BMI", "Grundumsatz kcal", "Notiz"],
    "training.csv": ["Datum", "Eintrag", "Einheit", "Uebung", "Satz", "Wdh", "Gewicht kg",
                     "Last gesamt kg", "RPE", "e1RM", "Gym", "Geraet", "Dauer min", "Distanz km",
                     "Hoehenmeter", "Notiz"],
    "ernaehrung.csv": ["Datum", "Item", "Mahlzeit", "Menge g", "kcal", "Protein g", "KH g", "Fett g",
                       "Ballast g", "Geschaetzt", "Konfidenz", "Notiz"],
    "festwerte.csv": ["Produkt", "kcal 100g", "Protein 100g", "KH 100g", "Fett 100g", "Ballast 100g",
                      "Salz 100g", "Standardportion g", "Quelle", "Notiz"],
    "merkzettel.csv": ["Datum", "Was", "Kategorie", "Status", "Details"],
    "auswertungen.csv": ["Datum", "Titel", "Art", "Zeitraum", "Kurzfazit", "Datei"],
}
AUSWAHL = {
    ("gewicht.csv", "Tageszeit"): {"", "morgens", "mittags", "abends"},
    ("gewicht.csv", "Messmethode"): {"", "Waage einfach", "Waage 8 Elektroden", "Navy Massband", "Caliper"},
    ("training.csv", "Gym"): {"", "Freundin", "Schwester", "anderes"},
    ("training.csv", "Geraet"): {"", "Langhantel frei", "Langhantel gefuehrt", "Kurzhantel", "SZ-Stange",
                                 "Kabelzug", "Maschine", "Koerpergewicht"},
    ("ernaehrung.csv", "Mahlzeit"): {"", "fruehstueck", "mittag", "abend", "snack"},
    ("ernaehrung.csv", "Konfidenz"): {"", "hoch", "mittel", "niedrig"},
    ("ernaehrung.csv", "Geschaetzt"): {"", "ja", "nein"},
    ("festwerte.csv", "Quelle"): {"", "Packung", "Herstellerseite", "Simon selbst", "geschaetzt"},
    ("merkzettel.csv", "Status"): {"offen", "in REGELN uebernommen", "verworfen"},
    ("auswertungen.csv", "Art"): {"Wochenreview", "Sonderauswertung"},
}
TEXT = {"Datum", "Eintrag", "Einheit", "Uebung", "Gym", "Geraet", "Notiz", "Item", "Mahlzeit",
        "Geschaetzt", "Konfidenz", "Produkt", "Quelle", "Was", "Kategorie", "Status", "Details",
        "Titel", "Art", "Zeitraum", "Kurzfazit", "Datei", "Tageszeit", "Messmethode"}
DATUM = re.compile(r"^\d{4}-\d{2}-\d{2}$")

fehler = []
for name, soll in SPALTEN.items():
    pfad = DATEN / name
    if not pfad.exists():
        fehler.append(f"{name}: Datei fehlt")
        continue
    with pfad.open(encoding="utf-8", newline="") as f:
        zeilen = list(csv.reader(f))
    kopf = zeilen[0]
    if kopf != soll + ["notion_id"]:
        fehler.append(f"{name}: Kopfzeile weicht ab: {kopf}")
        continue
    for nr, z in enumerate(zeilen[1:], start=2):
        if len(z) != len(kopf):
            fehler.append(f"{name} Zeile {nr}: {len(z)} statt {len(kopf)} Felder")
            continue
        d = dict(zip(kopf, z))
        if "Datum" in d and not DATUM.match(d["Datum"]):
            fehler.append(f"{name} Zeile {nr}: Datum '{d['Datum']}' nicht JJJJ-MM-TT")
        for spalte, wert in d.items():
            if spalte in TEXT or spalte == "notion_id" or wert == "":
                continue
            try:
                float(wert)
            except ValueError:
                fehler.append(f"{name} Zeile {nr}: '{spalte}' = '{wert}' ist keine Zahl (Punkt als Dezimalzeichen)")
        for (datei, spalte), erlaubt in AUSWAHL.items():
            if datei == name and d[spalte] not in erlaubt:
                fehler.append(f"{name} Zeile {nr}: '{spalte}' = '{d[spalte]}' nicht erlaubt")
        notiz = d.get("Notiz", "")
        if "UNGUELTIG" in notiz and not notiz.startswith("UNGUELTIG"):
            # Nur Hinweis: das Wort darf in Erklärtexten vorkommen, eine Markierung muss aber vorne stehen.
            print(f"Hinweis {name} Zeile {nr}: 'UNGUELTIG' steht nicht am Anfang der Notiz - ist das eine Markierung?")
    print(f"{name}: {len(zeilen) - 1} Zeilen")

if fehler:
    print("\nFEHLER - nicht committen:")
    for f in fehler:
        print("  " + f)
    sys.exit(1)
print("\nAlles in Ordnung.")

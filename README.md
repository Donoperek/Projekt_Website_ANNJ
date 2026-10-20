# Schachclub DHBW (fiktives Projekt)

Website für das DHBW-Modul **Webseiten Projekt 2026**. Reines HTML5 und CSS, kein JavaScript, keine externen Skripte, Schriften oder Bilder.

## Start
`index.html` in einem lokalen Server öffnen, zum Beispiel `python3 -m http.server`.

## Struktur
- 8 Seiten: Start, Lernen, Termine, Turniere, Mitmachen, Über uns, Kontakt, Impressum
- `css/style.css`: eine Datei, Farben und Abstände als CSS-Variablen
- `build.py`: optionaler Generator, der die Seiten aus gemeinsamen Bausteinen erzeugt (nicht für den Betrieb nötig)

## Technische Entscheidungen
- Layouts: Hero mit CSS-Brett (Start), Kartenraster (Lernen), Tabellen (Termine, Turniere), Preiskarten und FAQ (Mitmachen), Formular (Kontakt), Textseite (Impressum)
- Responsive von 320 bis 1920 px mit CSS Grid und `auto-fit`
- Barrierefreiheit (WCAG 2.2 A, AA angestrebt): Skip-Link, semantische Tags, `aria-current`, Labels, sichtbarer Fokus, Kontrast, `prefers-reduced-motion`
- Schachbrett und Figuren sind CSS und Unicode-Text, daher keine Lizenzfragen und schnelle Ladezeit
- Das Kontaktformular ist ein Mock (`action="kontakt.html"`)
- Hinweis auf die fiktive Arbeit steht auf jeder Seite oben

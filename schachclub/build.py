# Erzeugt die HTML-Seiten aus gemeinsamen Bausteinen (Ausgabe ist normales, lesbares HTML)
NAV=[("index.html","Start"),("lernen.html","Lernen"),("termine.html","Termine"),("turniere.html","Turniere"),("mitmachen.html","Mitmachen"),("ueber-uns.html","Über uns"),("kontakt.html","Kontakt")]
def page(f,title,body):
    nav="".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h==f else ""}>{t}</a></li>' for h,t in NAV)
    html=f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Schachclub DHBW Heidenheim: Schach spielen, lernen und Turniere für Studierende. Fiktives Projekt.">
<title>{title} – Schachclub DHBW</title>
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<a class="skip" href="#inhalt">Zum Inhalt springen</a>
<div class="notice">Fiktive Arbeit im Rahmen der DHBW Heidenheim (Webseiten Projekt 2026) – kein echter Verein.</div>
<header class="site-header"><div class="wrap">
<a class="brand" href="index.html"><span aria-hidden="true">♞</span> Schachclub DHBW</a>
<nav aria-label="Hauptnavigation"><ul class="nav">{nav}</ul></nav>
<a class="btn" href="mitmachen.html">Jetzt mitspielen</a>
</div></header>
<main id="inhalt">
{body}
</main>
<footer class="site-footer"><div class="wrap">
<ul><li><a href="index.html">Start</a></li><li><a href="kontakt.html">Kontakt</a></li><li><a href="impressum.html">Impressum</a></li></ul>
<p>© 2026 Schachclub DHBW (fiktiv) · Alle Zeichen sind Unicode-Text, keine Fremdbilder.</p>
</div></footer>
</body>
</html>
'''
    open(f,"w",encoding="utf-8").write(html)

cards=lambda items:"".join(f'<article class="card"><div class="icon" aria-hidden="true">{i}</div><h3>{t}</h3><p>{p}</p></article>' for i,t,p in items)

page("index.html","Start",f'''
<section class="hero"><div class="wrap">
<div><p class="eyebrow">Für Studierende der DHBW</p>
<h1>Dein Zug.<br>Dein Club.</h1>
<p class="lead">Ob du gerade die Regeln lernst oder schon Eröffnungen paukst: Beim Schachclub DHBW findest du Gegner auf Augenhöhe, Training und Turniere direkt neben der Vorlesung.</p>
<div class="btn-row"><a class="btn" href="mitmachen.html">Kostenlos reinschnuppern</a><a class="btn btn-ghost" href="termine.html">Termine ansehen</a></div>
<div class="stats"><p><strong>2×</strong>Training pro Woche</p><p><strong>0 €</strong>Probetraining</p><p><strong>Alle</strong>Spielstärken</p></div></div>
<div class="board" role="img" aria-label="Schachbrett mit einem Springer">♞</div>
</div></section>
<section><div class="wrap"><h2>Warum Schach an der DHBW?</h2>
<div class="grid">{cards([("♟","Lernen ohne Druck","Anfänger-Gruppen mit Mentoren zeigen dir Schritt für Schritt, wie das Spiel funktioniert."),("♜","Training für Fortgeschrittene","Eröffnungen, Endspiele und Partieanalyse in kleinen Runden."),("♛","Turniere zwischen Vorlesungen","Blitz, Schnellschach und das Semesterturnier – kurz genug für den Stundenplan."),])}</div></div></section>
''')

page("lernen.html","Lernen",f'''
<section><div class="wrap"><p class="eyebrow">Lernen</p><h1>Vom Bauern zur Dame</h1>
<p class="lead">Unsere Lerneinheiten sind kurz und bauen aufeinander auf. Such dir dein Niveau aus.</p>
<div class="grid">
<article class="card"><span class="badge">Anfänger</span><h3>Regeln &amp; Figuren</h3><p>Wie ziehen die Figuren? Was bedeuten Schach, Matt und Patt? Dazu die ersten Mattbilder.</p><a href="termine.html">Anfänger-Training ansehen</a></article>
<article class="card"><span class="badge">Mittelstufe</span><h3>Eröffnungen &amp; Taktik</h3><p>Gabeln, Fesselungen und die wichtigsten Eröffnungsprinzipien für Weiß und Schwarz.</p><a href="termine.html">Training für Mittelstufe ansehen</a></article>
<article class="card"><span class="badge">Fortgeschritten</span><h3>Endspiele &amp; Analyse</h3><p>Turmendspiele, Bauernstrukturen und die Analyse eigener Partien.</p><a href="turniere.html">Zu den Turnieren</a></article>
</div></div></section>
''')

def row(*c): return "<tr>"+"".join(f"<td>{x}</td>" for x in c)+"</tr>"
page("termine.html","Termine",f'''
<section><div class="wrap"><p class="eyebrow">Termine</p><h1>Wann wir spielen</h1>
<p class="lead">Alle Termine liegen so, dass du sie nach der Vorlesung erreichst. Orte und Zeiten sind Beispieldaten.</p>
<div class="table-scroll"><table><caption>Wochenplan Semester 2026/27</caption>
<thead><tr><th scope="col">Tag</th><th scope="col">Zeit</th><th scope="col">Angebot</th><th scope="col">Ort</th></tr></thead><tbody>
{row("Mittwoch","17:30–19:00","Anfänger-Training","Raum A101 (Beispiel)")}
{row("Mittwoch","19:00–21:00","Freies Spielen","Raum A101 (Beispiel)")}
{row("Freitag","16:00–18:00","Taktik &amp; Eröffnungen","Raum B204 (Beispiel)")}
{row("Samstag (monatlich)","10:00–14:00","Schnellschach-Turnier","Mensa-Foyer (Beispiel)")}
</tbody></table></div>
<p><a class="btn" href="kontakt.html">Frage zu einem Termin stellen</a></p></div></section>
''')

page("turniere.html","Turniere",f'''
<section><div class="wrap"><p class="eyebrow">Turniere</p><h1>Zeig, was du kannst</h1>
<p class="lead">Drei Formate für jede Zeit und jede Spielstärke. Alle Ergebnisse sind Beispieldaten.</p>
<div class="table-scroll"><table><caption>Turnierkalender und Tabelle Semesterturnier (Beispiel)</caption>
<thead><tr><th scope="col">Turnier</th><th scope="col">Bedenkzeit</th><th scope="col">Datum</th></tr></thead><tbody>
{row("Blitz-Abend","3 + 2 Minuten","Nov 2026")}{row("Schnellschach","15 + 10 Minuten","Dez 2026")}{row("Semesterturnier","60 Minuten","Jan 2027")}</tbody></table></div>
<h2 style="margin-top:2.5rem">Stand Semesterturnier</h2>
<div class="table-scroll"><table><thead><tr><th scope="col">Platz</th><th scope="col">Spieler</th><th scope="col">Punkte</th></tr></thead><tbody>
{row("1","Lena K.","4,5")}{row("2","Jonas M.","4,0")}{row("3","Sara P.","3,5")}</tbody></table></div>
<p><a class="btn" href="mitmachen.html">Für Turniere anmelden</a></p></div></section>
''')

def plan(n,price,note,items,pop=False,cta="Auswählen"):
    li="".join(f"<li>{i}</li>" for i in items)
    return f'<article class="card plan{" popular" if pop else ""}">'+('<span class="badge">Beliebt</span>' if pop else '')+f'<h3>{n}</h3><p class="price">{price}</p><p>{note}</p><ul>{li}</ul><a class="btn" href="kontakt.html">{cta}</a></article>'
page("mitmachen.html","Mitmachen",f'''
<section><div class="wrap"><p class="eyebrow">Mitgliedschaft</p><h1>Wähle deinen Platz am Brett.</h1>
<p class="lead">Starte kostenlos und wechsle, wenn du mehr willst. Preise sind fiktiv.</p>
<div class="grid">
{plan("Gast","0 €","für das erste Semester",["Probetraining","Freies Spielen","Anfänger-Gruppe"],cta="Als Gast starten")}
{plan("Mitglied","5 € / Semester","für Studierende",["Alles aus Gast","Alle Trainings","Semesterturnier","Vereinsbretter nutzen"],True,"Mitglied werden")}
{plan("Turnierspieler","15 € / Semester","für Ehrgeizige",["Alles aus Mitglied","Alle Turniere","Partieanalyse","Eigene Spielstärke-Wertung"],cta="Turnierspieler werden")}
</div>
<h2 style="margin-top:3rem">Fragen und Antworten</h2>
<details><summary>Muss ich schon spielen können?</summary><p>Nein. Die Anfänger-Gruppe startet bei null.</p></details>
<details><summary>Kann ich jederzeit aufhören?</summary><p>Ja, die Mitgliedschaft endet zum Semesterende. Du musst nichts kündigen.</p></details>
<details><summary>Brauche ich ein eigenes Schachbrett?</summary><p>Nein. Bretter und Uhren stellt der Club.</p></details>
</div></section>
''')

page("ueber-uns.html","Über uns",f'''
<section><div class="wrap prose"><p class="eyebrow">Über uns</p><h1>Ein Club von Studierenden für Studierende</h1>
<p class="lead">Der Schachclub DHBW ist ein fiktives Projekt aus dem Modul Webseiten Projekt 2026 an der DHBW Heidenheim.</p>
<h2>Unser Ziel</h2><p>Wir wollen, dass jede und jeder an der DHBW einen entspannten Ort zum Schachspielen findet, neben Vorlesung und Praxisphase.</p>
<h2>Unser Team (Beispiel)</h2></div>
<div class="wrap"><div class="grid">{cards([("♔","Vorstand","Organisiert Termine und Turniere."),("♕","Training","Betreut Anfänger- und Fortgeschrittenengruppen."),("♖","Öffentlichkeitsarbeit","Pflegt Website und Aushänge.")])}</div></div></section>
''')

page("kontakt.html","Kontakt",f'''
<section><div class="wrap"><p class="eyebrow">Kontakt</p><h1>Schreib uns.</h1>
<p class="lead">Fragen zu Terminen oder zur Mitgliedschaft? Das Formular ist ein Mock und sendet nichts ab.</p>
<form class="form" action="kontakt.html" method="get">
<div><label for="name">Name</label><input id="name" name="name" autocomplete="name" required></div>
<div><label for="mail">E-Mail</label><input id="mail" name="mail" type="email" autocomplete="email" required></div>
<div><label for="level">Deine Spielstärke</label><select id="level" name="level"><option>Anfänger</option><option>Mittelstufe</option><option>Fortgeschritten</option></select></div>
<div><label for="msg">Nachricht</label><textarea id="msg" name="msg" rows="5" required></textarea></div>
<button class="btn" type="submit">Nachricht senden</button>
</form></div></section>
''')

page("impressum.html","Impressum",f'''
<section><div class="wrap prose"><h1>Impressum</h1>
<p><strong>Hinweis:</strong> Diese Website ist eine fiktive Arbeit im Rahmen der DHBW Heidenheim (Webseiten Projekt 2026). Es gibt keinen echten Verein.</p>
<p>Verantwortlich im Sinne der Projektarbeit: Projektgruppe Schachclub DHBW (Namen werden in der Dokumentation ergänzt).</p>
<p>Alle Inhalte, Preise, Termine und Personen sind erfunden. Es werden keine Bilder, Schriften oder Skripte von Dritten eingebunden.</p>
<p><a href="index.html">Zurück zur Startseite</a></p></div></section>
''')

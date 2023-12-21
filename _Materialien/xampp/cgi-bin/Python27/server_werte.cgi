#!C:\Python27\python.exe

# Modul cgi
import cgi, cgitb

# Ausgabe bei Fehler
cgitb.enable()

# Objekt der Klasse FieldStorage
form = cgi.FieldStorage()

# HTML-Dokument mit Variablen
print "Content-type: text/html"
print

# Auswertung Formularfeld
if "nn" in form:
    print "<p><b>Registrierte Daten:</b></p>"
    print "<p>Nachnamen:<br />"
    try:
        print form["nn"].value
    except:
        for element in form["nn"]:
            print element.value, "<br />"
    print "</p>"
else:
    print "<p><b>Keine Daten gesendet</b></p>"

print "</body>"
print "</html>"

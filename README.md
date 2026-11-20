Proof-of-concept für die Generierung von Meshcore-Kanalnamen aus amtlichen Regionalschlüsseln

```
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
```

Die GV-Datei ist das Gemeindeverzeichnis des statistischen Bundesamts in der Variante "regionale Gliederung":

https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/_inhalt.html

Nein, die Datei ist nicht im ASCII-Format, denn es gibt in der deutschen Sprache Umlaute. Ich vermute, dass die Datei ihren Ursprung auf dem Mainframe hat, und dort nennen sie eben alles ASCII, was nicht EBCDIC ist.

```
curl -O 'https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/Archiv/GV100ADQ/GV100AD3011.zip?__blob=publicationFile&v=17'
unzip GV100AD3011.zip GV*txt
```

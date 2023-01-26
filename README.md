# Simpler-Python-Taschenrechner-ohne-GUI

Dieser Code definiert eine Funktion namens "calculator()", die einen Taschenrechner implementiert. Der Taschenrechner bietet die Möglichkeit, Addition, Subtraktion, Multiplikation, Division, Exponenten und Wurzeln durchzuführen.

Die Funktion beginnt mit einer Endlosschleife, die es ermöglicht, immer wieder neue Berechnungen durchzuführen, ohne dass der Taschenrechner beendet werden muss. Innerhalb der Schleife werden dem Benutzer die verfügbaren Optionen angezeigt und er wird aufgefordert, eine Auswahl zu treffen.

Je nach Auswahl des Benutzers werden unterschiedliche Berechnungen durchgeführt. Wenn der Benutzer die Option 1 wählt, werden zwei Zahlen eingegeben und addiert, das Ergebnis wird auf der Konsole ausgegeben. Ähnlich funktionieren die anderen Optionen: Wenn der Benutzer die Option 2 wählt, werden zwei Zahlen eingegeben und subtrahiert, usw.

Die Auswahl "5" ermöglicht das Berechnen von Exponenten und die Auswahl "6" das Berechnen von Wurzeln. Hierfür wird die Funktion math.sqrt() aus dem Python Standardbibliothek verwendet.

Wenn der Benutzer die Option 7 wählt, wird die Schleife beendet und der Taschenrechner beendet. Wenn eine ungültige Auswahl getroffen wurde, wird eine Fehlermeldung ausgegeben und der Benutzer aufgefordert, erneut zu versuchen.

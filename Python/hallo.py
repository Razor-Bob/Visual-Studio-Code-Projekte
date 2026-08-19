# Beispiel 4.4.8
# print(len("Wasserfall"))
# Beispiel 4.4.9
# text = "Wasserfall"
# print(len(text))  # Das Ergebnis ist 10, da die Nachricht "Wasserfall" 10 Zeichen enthält.
# Beispiel 4.4.10
# print(len("Hallo Python!")) # Das Ergebnis ist 13, da die Nachricht "Hallo Python!" 13 Zeichen enthält.
# Die Methode upper() wandelt alle Buchstaben in Großbuchstaben um.
# Beispiel 4.4.11
# text = "Hallo Python!"
# grossbuchstaben = text.upper()
# print(grossbuchstaben)
# Ausgabe des Ergebnisses der Methode upper() direkt auf dem String "Hallo Python!".
# print("Hallo Python!".upper())
# Beispiel 4.4.12
# text = "Hallo Python!"
# kleinbuchstaben = text.lower()
# print(kleinbuchstaben)
# Ausgabe des Ergebnisses der Methode lower() direkt auf dem String "Hallo Python!".
# print("Hallo Python!".lower())
# Beispiel 4.4.13
# text = "Hallo Python!"
# print(text.isupper())  # Gibt False zurück, da nicht alle Buchstaben Großbuchstaben sind.
# Aufrufen der Methode isupper direkt auf dem String "Hallo Python!" und Ausgabe des Ergebnisses.
# print("Hallo Python!".isupper())  # Gibt False zurück, da nicht alle Buchstaben Großbuchstaben sind.
# Beispiel 4.4.14
# text = "Hallo Python!"
# print(text.islower())  # Gibt False zurück, da nicht alle Buchstaben Kleinbuchstaben sind.
# Aufrufen der Methode islower direkt auf dem String "Hallo Python!" und Ausgabe des Ergebnisses.
# print("Hallo Python!".islower())  # Gibt False zurück, da nicht alle Buchstaben Kleinbuchstaben sind.
# Beispiel 4.4.15
# text = "Hallo Python!"
# ergebnis = text.strip()  # Entfernt führende und nachgestellte Leerzeichen aus dem String.
# print(ergebnis)  # Gibt "Hallo Python!" zurück, da keine führenden oder nachgestellten Leerzeichen vorhanden sind.
# Aufrufen der Methode strip direkt auf dem String "   Hallo Python!   " und Ausgabe des Ergebnisses.
# print("   Hallo Python!   ".strip())  # Gibt "Hallo Python!" zurück, da führende und nachgestellte Leerzeichen entfernt werden.
# Beispiel 4.4.16
# text = "Python"
# ergebnis = text.zfill(10)  # Füllt den String mit führenden Nullen auf, um eine Gesamtlänge von 10 Zeichen zu erreichen.
# print(ergebnis)  # Gibt "0000Python" zurück, da der String auf eine Gesamtlänge von 10 Zeichen aufgefüllt wird.
# Aufrufen der Methode zfill direkt auf dem String "Python" und Ausgabe des Ergebnisses.
# print("Python".zfill(10))  # Gibt "0000Python" zurück, da der String auf eine Gesamtlänge von 10 Zeichen aufgefüllt wird.
# Beispiel 4.4.17
# text = ''
# print(text.zfill(3))  # Gibt "000" zurück, da der leere String auf eine Gesamtlänge von 3 Zeichen aufgefüllt wird.
# Beispiel 4.4.18
# text = "Python"
# print(text.zfill(3))  # Gibt "0000Python" zurück, da der String auf eine Gesamtlänge von 10 Zeichen aufgefüllt wird.
# Beispiel 4.4.19
# text = "Wasserfall"
# print(text.index("a"))  # Gibt 1 zurück, da der erste Buchstabe "a" an der Position 1 im String "Wasserfall" gefunden wird.
# Aufrufen der Methode index direkt auf dem String "Wasserfall" und Ausgabe des Ergebnisses.
# print("Wasserfall".index("a"))  # Gibt 1 zurück, da der erste Buchstabe "a" an der Position 1 im String "Wasserfall" gefunden wird.
# Beispiel 4.4.20
# text = "Hallo Python!"
# print(text.index("y"))  # Gibt 7 zurück, da der erste Buchstabe "y" an der Position 7 im String "Hallo Python!" gefunden wird.
# Beispiel 4.4.21
# text = "Hallo Python!"
# print(text.index("c"))  # Gibt einen Fehler zurück, da der Buchstabe "c" nicht im String "Hallo Python!" gefunden wird.
# Beispiel 4.4.22
# text = "Diebe"
# ergebnis = text.replace("D", "L")  # Ersetzt den Buchstaben "D" durch den Buchstaben "L" im String "Diebe".
# print(ergebnis)  # Gibt "Liebe" zurück, da der Buchstabe "D" durch den Buchstaben "L" ersetzt wurde.
# Aufrufen der Methode replace direkt auf dem String "Diebe" und Ausgabe des Ergebnisses.
# print("Diebe!".replace("D", "L"))  # Gibt "Liebe!" zurück, da der Buchstabe "D" durch den Buchstaben "L" ersetzt wurde.
# Beispiel 4.4.23
# text = "Hallo Python!"
# print(text.replace("o", "0"))  # Gibt "Hall0 Pyth0n!" zurück, da der Buchstabe "o" durch die Zahl "0" ersetzt wurde.
# Beispiel 4.4.24
# text = "Hallo Python!"
# print(text.replace("p", "C"))  # Gibt "Hallo Python!" zurück, da der Buchstabe "p" nicht im String "Hallo Python!" gefunden wird.
# Beispiel 4.4.25
# text = "Hallo Python!"
# print(text.replace("Python", "Maximilian"))  # Gibt "Hallo Maximilian!" zurück, da der Teilstring "Python" durch den Teilstring "Maximilian" ersetzt wurde.
# Beispiel 4.4.26
# text = "Hallo Python!"
# print(text.replace("o", ""))  # Gibt "Hall Pythn!" zurück, da der Buchstabe "o" durch einen leeren String ersetzt wurde.
# Beispiel 4.4.27
# name = "Florian"
# print(f"Hallo {name}!")  # Gibt "Hallo Florian!" zurück, da der Name "Florian" in den String eingefügt wird.
# Beispiel 4.4.28
# x1 = 2
# x2 = -4
# print(f"Die Lösungen von x^2+2x-8=0 sind\nx1={x1} und\nx2={x2}")  # Gibt "Die Lösungen von x^2+2x-8=0 sind x1=2 und x2=-4" zurück, da die Werte von x1 und x2 in den String eingefügt werden.
# JETZT DIE AUFGABEN VON SEITE 78 bearbeiten.

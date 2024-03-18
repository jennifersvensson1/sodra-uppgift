# Södra - Hemuppgift Systemutvecklare

Detta projekt innehåller lösningar för två programmeringsuppgifter, där den ena är ett test på SQL-kunskaper och den andra på kunskaper inom imperativ programmering.

## SQL

Filen `query.sql` innehåller en SQL-query som returnerar antalet anställda per avdelning. Queryn förutsätter en databas med tabellen _Medarbetare_ som kolumnerna _ID_, _Namn_ och _Avdelning_.
Exempelvis:

| ID |  Namn  |  Avdelning  |
| --- | --- | --- |
| 1 | Lisa | IT |
| 2 | Kalle | HR |
| 3 | Emma | HR | 

För att köra SQL-queryn, kopiera den direkt till en SQL-miljö. 

## Imperativ programmering

Filen `has_unique_chars.py` innehåller en Python-funktion som avgör om en textsträng endast har unika bokstäver/tecken. Exempelvis har textsträngen "Södra" endast unika tecken, medan det i textsträngen "Södra Skogsägarna" förekommer vissa tecken flera gånger.

För att testa funktionen, kör koden i en Python-miljö.
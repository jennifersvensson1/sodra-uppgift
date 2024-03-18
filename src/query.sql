-- Fetch number of employees per department
SELECT COUNT(*) AS [Antalet anställda], Avdelning
FROM Medarbetare
GROUP BY Avdelning;
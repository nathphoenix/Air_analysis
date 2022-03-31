SELECT MAX(`NOx`) AS MAX_NOX, `Date Time`, `Location` FROM `pollution` 
WHERE EXTRACT(YEAR FROM `Date Time`) = 2019
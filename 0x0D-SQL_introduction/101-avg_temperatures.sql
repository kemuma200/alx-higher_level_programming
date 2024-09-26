-- Script that displays the average temperature
SELECT city, AVG(value) AS avg_temp FROM temperature group by city ORDER BY avg_temp DESC;

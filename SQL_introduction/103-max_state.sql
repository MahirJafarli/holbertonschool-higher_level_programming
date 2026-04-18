-- Displays the maximum temperature of each state
-- Results are ordered by State name (alphabetically)
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state` ASC;

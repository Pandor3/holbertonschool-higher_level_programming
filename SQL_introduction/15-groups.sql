-- 15. This script will list the number of records of the same score in the second_table
SELECT score, COUNT(*) as number FROM `second_table` GROUP BY score ORDER BY score DESC;
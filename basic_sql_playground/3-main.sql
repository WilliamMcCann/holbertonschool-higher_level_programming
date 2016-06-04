/*add and update values in this database*/
UPDATE Person
SET age=27
WHERE first_name='Jon';
UPDATE Person
SET age=18
WHERE first_name='Walter Junior' AND last_name='White';
DELETE FROM EyesColor
where exists
(SELECT *
FROM Person
WHERE Person.id = EyesColor.person_id
AND first_name='Walter');
DELETE FROM Person
WHERE first_name='Walter';
SELECT *
FROM Person
ORDER BY first_name ASC;

SELECT * FROM status 
WHERE "time" > "2015-08-15" AND 
 ("bikes_available" < 2 OR "docks_available" < 2)
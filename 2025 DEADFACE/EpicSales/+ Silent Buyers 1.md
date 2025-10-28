> [!abstract] Challenge Description
> > @syyntax
> ## 400
> DEADFACE is suspected of exfiltrating targeted customer engagement data. EpicSales wants to identify a particularly valuable customer profile: the email address of the customer who has placed the most orders but has never left a review for any product. This customer represents a key target due to their high engagement without providing feedback.
> 
> Submit the flag as deadface{email}. Example: `deadface{ctf@deadface.io}`.
> 
> Host: `env01.deadface.io:3306` Username: `epicsales` Password: `Slighted3-Charting-Valium` Database: `epicsales_db`

`mysql -h env01.deadface.io -P 3306 -u epicsales -pSlighted3-Charting-Valium epicsales_db` connects me to the mySQL database.

I have to know the database
```SQL
SHOW TABLES;
+------------------------+
| Tables_in_epicsales_db |
+------------------------+
| categories             |
| customers              |
| employee_assignments   |
| employees              |
| facilities             |
| inventories            |
| loyalty_points         |
| order_items            |
| orders                 |
| products               |
| reviews                |
+------------------------+
11 rows in set (0.16 sec)

DESC customers;
+-------------+------------------+------+-----+---------+-------+
| Field       | Type             | Null | Key | Default | Extra |
+-------------+------------------+------+-----+---------+-------+
| customer_id | int(10) unsigned | NO   | PRI | NULL    |       |
| first_name  | varchar(32)      | NO   |     | NULL    |       |
| last_name   | varchar(64)      | NO   |     | NULL    |       |
| email       | varchar(128)     | NO   | UNI | NULL    |       |
| password    | varchar(60)      | NO   |     | NULL    |       |
| dob         | date             | NO   |     | NULL    |       |
| sex         | varchar(8)       | NO   |     | NULL    |       |
| join_date   | date             | NO   | MUL | NULL    |       |
| street      | varchar(64)      | NO   |     | NULL    |       |
| suite       | varchar(16)      | YES  |     | NULL    |       |
| city        | varchar(64)      | NO   |     | NULL    |       |
| state       | varchar(8)       | NO   |     | NULL    |       |
| postal      | varchar(16)      | NO   |     | NULL    |       |
| country     | varchar(8)       | NO   |     | US      |       |
+-------------+------------------+------+-----+---------+-------+
14 rows in set (0.18 sec)
```

From here I can query


Since I know what I'm looking for, I can go straight for a query.

```SQL
SELECT 
    e.email, 
    AVG(i.quantity) as avg_quantity
FROM facilities f
JOIN inventories i ON f.facility_id = i.facility_id
JOIN employee_assignments ea ON f.facility_id = ea.facility_id
JOIN employees e ON ea.employee_id = e.employee_id
WHERE e.role = 'IT Manager'
GROUP BY f.facility_id, e.email
ORDER BY avg_quantity ASC
LIMIT 1;

+------------------------------+--------------+
| email                        | avg_quantity |
+------------------------------+--------------+
| valera.kenner@epicsales.shop |    2274.4626 |
+------------------------------+--------------+
1 row in set (0.17 sec)
```

---
> [!success] Flag: `deadface{valera.kenner@epicsales.shop 2274.4626}`

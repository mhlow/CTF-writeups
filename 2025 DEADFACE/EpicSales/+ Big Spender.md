> [!abstract] Challenge Description
> > @syyntax
> ## 210
>DEADFACE has compromised the account of a SkyWave Telecommunications employee and used the employee’s EpicSales account to spend a large amount of money on products. Your task is to find the first and last name of the customer who has spent the most money across all their orders.
> 
>Submit the flag as `deadface{firstname lastname}`. Example: `deadface{John Doe}`.
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
SELECT c.first_name, c.last_name, SUM(oi.quantity * p.price) as total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_spent DESC
LIMIT 1;
+------------+-----------+-------------+
| first_name | last_name | total_spent |
+------------+-----------+-------------+
| Willabella | Wain      |  1001960.66 |
+------------+-----------+-------------+
1 row in set (0.24 sec)
```

---
> [!success] Flag: `deadface{Willabella Wain}`

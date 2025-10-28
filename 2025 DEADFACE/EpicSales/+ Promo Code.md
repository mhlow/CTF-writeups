> [!abstract] Challenge Description
> > @syyntax
> ## 25
> As a means to entice DEADFACE and honeypot them, EpicSales ran a promo code for new users that started on September 1, 2025. They had Turbo Tactical advertise the promo code in known DEADFACE channels, hoping a DEADFACE member would bite. How many customers signed up on or after September 1, 2025?
> 
> Submit the flag as `deadface{#}`.
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
SELECT COUNT(*) FROM customers WHERE join_date >= '2025-09-01';
+----------+
| COUNT(*) |
+----------+
|       18 |
+----------+
1 row in set (0.17 sec)
```

---
> [!success] Flag: `deadface{18}`

> [!abstract] Challenge Description
> > @syyntax
> ## 50
> > All challenges in the **EpicSales** series use the same database and credentials.
> 
> DEADFACE is known for causing disruptions in supply chains. EpicSales noticed unusual activity in product quantities. Identify the `product_name` and the `facility_num` for any product where the total quantity in that specific facility is less than 5. Of these, which product has the lowest quantity and at which facility?
> 
> Submit the `product_name` and `facility_num` as the flag: `deadface{product_name facility_num}`. Example: `deadface{NeonSky Tablet 4 32}` where `NeonSky Tablet 4` is the product and `32` is the facility_num.
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
SELECT p.product_name, f.facility_num, SUM(i.quantity) as total_quantity
FROM products p
JOIN inventories i ON p.product_id = i.product_id
JOIN facilities f ON i.facility_id = f.facility_id
GROUP BY p.product_name, f.facility_num
HAVING SUM(i.quantity) < 5
ORDER BY total_quantity ASC
LIMIT 1;

+---------------------------+--------------+----------------+
| product_name              | facility_num | total_quantity |
+---------------------------+--------------+----------------+
| ConnectGear SafeDrive 2TB |           16 |              1 |
+---------------------------+--------------+----------------+
1 row in set (0.18 sec)
```

---
> [!success] Flag: `deadface{ConnectGear SafeDrive 2TB 16}`

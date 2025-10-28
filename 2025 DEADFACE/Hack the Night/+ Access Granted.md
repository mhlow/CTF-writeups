> [!abstract] Challenge Description
> > @syyntax
> ## 50
> We need to gain authenticated access to the web app, but we want to see if we can do it the way DEADFACE did. NVU admits they haven’t fixed anything regarding their authentication process. See if you can login to the web app.
> 
> Submit the flag as `deadface{flag text}`.
> 
> > Note: the application will present you with the flag once you login.
> 
> [http://env01.deadface.io:8080](http://env01.deadface.io:8080/)

Initial thought was to try SQL injection on the login page.
`admin' OR 1=1 OR '` worked.



---
> [!success] Flag: `deadface{sql_1nj3ct10n_byp4ss_4uth}`

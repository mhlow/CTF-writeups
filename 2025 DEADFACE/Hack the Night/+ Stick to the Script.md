> [!abstract] Challenge Description
> > @syyntax
> ## 40
> NVU thought they were being clever by obfuscating some of their code, but DEADFACE was able to figure it out. Despite this, NVU hasn’t remediated the issue; we’re pretty sure the secret they tried to hide in their code is still there - easily readable to anyone who sees it. Find the flag that is obfuscated in the web app’s code.
> 
> Submit the flag as `deadface{flag text}`.
> 
> [http://env01.deadface.io:8080](http://env01.deadface.io:8080/)


Checking the script of the site, there is a suspicious base64 hidden as a comment.
`ZGVhZGZhY2V7ajR2NHNjcjFwdF9jNG5faDFkM19zM2NyM3RzfQ==`



---
> [!success] Flag: `deadface{j4v4scr1pt_c4n_h1d3_s3cr3ts}`

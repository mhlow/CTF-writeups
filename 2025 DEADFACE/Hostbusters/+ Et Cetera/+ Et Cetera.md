> [!abstract] Challenge Description
> > @syyntax
> ## 25
> `gh0st404` is complaining in Ghost Town about his script not working. See if you can locate the script on the remote machine and read the flag.
> 
> Submit the flag as `deadface{flag_text}`.
> 
> Use the connection information from [[+ Let Me In]].

Navigating to the `tools` directory, we see the following files:
```bash
subrecon.sh
techfinger.sh
```

There's nothing interesting on these files. Even running them on somethin like `www.example` gives an empty output.

Looking at the (forum page)[https://ghosttown.deadface.io/t/bruh-why-is-my-script-still-broken/93], we see gh0st404 asking for help with his scripts.

> [!info] gh0st404's post
> ![[Et Cetera gh0st404 post.png]]

The post mentions `/etc`
Checking it out, we see there's an unusual file `logclean.sh`, however there's no permission on it. 

For some reason I did `chmod +x` and didnt even think about read permissions, but after `chmod 777 logclean.sh`, we can read the file, revealing the flag.

---
> [!success] Flag: `deadface{hostbusters3_0547796725934bbd}`

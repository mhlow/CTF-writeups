> [!abstract] Challenge Description
> > @syyntax
> ## 5
> Due to the efforts of the Turbo Tactical team, we’ve managed to acquire credentials belonging to `gh0st404` that can be used on a remote DEADFACE machine. Access this machine and find the flag in the user’s home directory.  
>   
> Submit the flag as `deadface{flag_text}`  
> 
> IP Address: `hostbusters.deadface.io`  
> Username: `gh0st404`  
> Password: `ReadySetG0!`

Using `ssh gh0st404@hostbusters.deadface.io` with the provided password, we can log into the remote machine.

`ls -al` shows the following
```bash
total 28
drwxr-sr-x    1 gh0st404 gh0st404      4096 Oct 25 15:54 .
drwxr-xr-x    1 root     root          4096 Sep 17 02:04 ..
-rw-------    1 gh0st404 gh0st404        25 Oct 25 15:54 .ash_history
-rw-r--r--    1 gh0st404 gh0st404       382 Sep 17 02:04 .dont_forget
-rw-r--r--    1 gh0st404 gh0st404      1850 Sep 17 02:04 notes.txt
drwxr-sr-x    1 gh0st404 gh0st404      4096 Sep 17 02:04 tools
```

- `cat notes.txt` prints the flag at the end.

---
> [!success] Flag: `deadface{hostbusters1_cf6a12ddf781cfbc}`

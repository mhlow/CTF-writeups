> [!abstract] Challenge Description
> > @syyntax
> ## 70
> The system seems to have multiple users, one of which is `deephax`. There’s a GhostTown thread between `gh0st404` and `deephax` talking about a `pen-console.py` being `deephax`’s default shell. He also mentions giving `gh0st404` his password. Look around the machine and see if you escalate laterally to `deephax`’s account. There may be information we can use (i.e., flag) in `deephax`’s shell environment.
> 
> Submit the flag as `deadface{flag_text}`.
> 
> Use the connection information from [[+ Let Me In]].

Mentions a thread on the forum, not much use.
Since they were talking about `pen-console.py`, running `find -name pen-console` in the root directory shows a file.
```sh
find: ./run/sudo: Permission denied
find: ./var/lib/sudo: Permission denied
./usr/local/bin/pen-console.py
find: ./etc/sudoers.d: Permission denied
find: ./root: Permission denied
find: ./proc/tty/driver: Permission denied
find: ./proc/6/task/6/fd: Permission denied
find: ./proc/6/task/6/fdinfo: Permission denied
find: ./proc/6/task/6/ns: Permission denied
find: ./proc/6/fd: Permission denied
find: ./proc/6/map_files: Permission denied
find: ./proc/6/fdinfo: Permission denied
find: ./proc/6/ns: Permission denied
```

In the one file that isnt restricted is our flag.

---
> [!success] Flag: `deadface{hostbusters5_e16a5c8995620a24}`

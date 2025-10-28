> [!abstract] Challenge Description
> > @syyntax
> ## 20
> DEADFACE loves their vintage tech, but their "Echo Chamber" chat bot has a critical flaw from the old days. It echoes messages without sanitizing input, potentially leaking sensitive data. As a Turbo Tactical operative, connect to the remote service at echochamber.deadface.io:13337 and exploit it to reveal a hidden flag.
>
> Submit the flag as `deadface{flag_text}`.
>
> `echochamber.deadface.io:13337`

When connecting using `nc echochamber.deadface.io 13337`, you receive the following prompt:

```
DEADFACE Echo Chamber
Enter your message: test
Echo: test
```

At first, I thought it was a simple command injection challenge.
I tried many combinations of escaping into shell, `test; ls`, but many of these resulted in the string being printed back, sometimes with random binary data appended.

This told me that it was vulnerable, but the data is not the way to get it, as the data kept changing every time.

After consulting with Claude, it suggested string format attack, and voila `%s` prints the flag.

## Why this works
*I had no experience in using something like `printf(string)` so thats my excuse for why I didn't know of it.*
What `printf` sees a format string, it will literally just print it no problem, but if you give it format specifiers like `%s`, `%x`, etc, it will try to read from the stack to fill in those values.

---
> [!success] Flag: `deadface{r3tr0_f0rm4t_l34k_3xp0s3d}`

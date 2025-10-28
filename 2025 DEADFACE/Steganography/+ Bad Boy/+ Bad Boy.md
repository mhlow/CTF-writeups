> [!abstract] Challenge Description
> > @syyntax
> ## 10 
> DEADFACE left this image on a victim’s machine with a hidden message. See if you can discover the flag hidden in this image. Submit the flag as `deadface{flag text}`.

Exiftool is uninteresting.
`strings -n 8 baddestboi.png` reveals the flag.

---
> [!success] Flag: `deadface{th3_b4dd3st_B0i_al1V3}`

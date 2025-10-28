> [!abstract] Challenge Description
> > @Deputy_Doge
> ## 100
> Using the artifacts from _**Trojan Echoes: What is the Password?**_, find the flag labeled `flag 02`.
> 
> Submit the flag as `deadface{here-is-the-answer}`.

Running `grep -a -w "deadface" sample_01E9.exe.exe` on the extracted executable shows some more information.

```
8@�����������������6@06@@6@P6@`6@2��-�+�] �f���01 - deadface{We_meet_again}You wanted this to be easy?USERPROFILE\flag.txtaWxlbl9hdHNfLSBkZmFjZXtJZWFkYmVlX3doMDIgfQ==wSOFTWARE\PoliciesPoliciesMacrohardWindersaG91aGVyZXtXZV9zd2VfYmVnbGRfMDMgaW59/4c/53/5a/58/74/6c/42/6b/46/6b/51/67/5a/76/5a/6d/46/6a/5a/57/39/73/4d/44/63/6d/61/57/56/32/74/47/58/32/63/31/56/73/4a/39https://www.totallynothackers.orghttps://www.youtube.com/watch?v=z_mUo5Zg-GMopen@�@`�@p#@��@��@@�@Argument domain error (DOMAIN)Argument singularity (SIGN)Overflow range error (OVERFLOW)Partial loss of significance (PLOSS)Total loss of significance (TLOSS)The result is too small to be represented (UNDERFLOW)Unknown error_matherr(): %s in %s(%g, %g)  (retval=%g)
```

We look at the base64 string `aWxlbl9hdHNfLSBkZmFjZXtJZWFkYmVlX3doMDIgfQ==` decoding to something that looks promising, only looks like its a transposition cipher of some sort. it has the number 2 which is promising.

On closer inspction, there are multiple parts that seem already together, namely things that appear in groups of 3 if we guess the format, `|02 |- d|ead|fac|e{I|`

Brute forcing by eye gives us `02 - deadface{Its_been_a_while}`


---
> [!success] Flag: `deadface{Its_been_a_while}`

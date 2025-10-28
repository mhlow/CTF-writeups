> [!abstract] Challenge Description
> > @Deputy_Doge
> ## 200
> Using the artifacts from _**Trojan Echoes: What is the Password?**_, find the flag labeled `flag 03`.
> 
> Submit the flag as `deadface{here-is-the-answer}`.

Running `grep -a -w "deadface" sample_01E9.exe.exe` on the extracted executable shows some more information.

```
8@�����������������6@06@@6@P6@`6@2��-�+�] �f���01 - deadface{We_meet_again}You wanted this to be easy?USERPROFILE\flag.txtaWxlbl9hdHNfLSBkZmFjZXtJZWFkYmVlX3doMDIgfQ==wSOFTWARE\PoliciesPoliciesMacrohardWindersaG91aGVyZXtXZV9zd2VfYmVnbGRfMDMgaW59/4c/53/5a/58/74/6c/42/6b/46/6b/51/67/5a/76/5a/6d/46/6a/5a/57/39/73/4d/44/63/6d/61/57/56/32/74/47/58/32/63/31/56/73/4a/39https://www.totallynothackers.orghttps://www.youtube.com/watch?v=z_mUo5Zg-GMopen@�@`�@p#@��@��@@�@Argument domain error (DOMAIN)Argument singularity (SIGN)Overflow range error (OVERFLOW)Partial loss of significance (PLOSS)Total loss of significance (TLOSS)The result is too small to be represented (UNDERFLOW)Unknown error_matherr(): %s in %s(%g, %g)  (retval=%g)
```

We look at the string `aG91aGVyZXtXZV9zd2VfYmVnbGRfMDMgaW59`, it contains a `3`.

`houhere{We_swe_begld_03 in}`
similar to the last one, it looks like there are groups of 3.
Brute forcing (much harder), we get `03 e{Where_should_we_begin}`, we are probably missing a section, but this will do


---
> [!success] Flag: `deadface{Where_should_we_begin}`

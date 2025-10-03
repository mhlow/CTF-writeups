> [!abstract] Challenge Description
> > Farel Z Andarya
> ## 150
> Top-secret documents have leaked from the The Ætheric Order. Inside lies a mysterious binary that supposedly contains the activation sequence for the Experimental Machine Gun 3000™.
> 
> Legend says this gun never jams, shoots faster than light, and can pierce through blockchain encryption. Unfortunately, the engineers were lazy and just hard-coded the access code directly into the binary.
> 
> Your mission: infiltrate the file, recover the activation code, and unlock ultimate firepower.
> 
> The flag format is: `NexusCTF{<flag>}`

Decompiling in Ghidra shows a bunch of obfuscation, converting the bottom half numbers to characters, it is clear that they built up the final string letter by letter.

---
> [!success] Flag: `NexusCTF{n1t3_n3ar_s1x}`



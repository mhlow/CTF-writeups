> [!abstract] Challenge Description
> > @syyntax
> ## 100
> DEADFACE stole a sensitive document from the MyShare application! Find the document and present the flag shown within.
> 
> Submit the flag as `deadface{flag}`.
> 
> NOTE: `deadface{h1dd3n_c0mm$!!}` is NOT the flag. It's a leftover remnant that was supposed to have been removed.
> 
> > Use the ZIP file from [[+ The Source]]

There's a long stream where the attacker downloaded something. Savings this whole stream as raw data, which is in the folder, and using `binwalk` shows us the files within. At the bottom of the pdf shows the flag.

---
> [!success] Flag: `deadface{w1R3_y0uR_Br41N}`

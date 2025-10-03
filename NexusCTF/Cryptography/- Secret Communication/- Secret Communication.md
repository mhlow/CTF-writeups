> [!abstract] Challenge Description
> > Farel Z Andarya
> ## 400
> **Faction:** UDPC
> 
> **Short description (ID):** Martian People's Liberation Front (MPLF) is in secret communication with Beltway Bandits regarding a **rebellion plan**. The messages are reportedly encrypted using a simple elliptic curve. A partial leak has been discovered: the file `leak.txt` contains the `x` values of the Q and P points (respectively), as well as the **first 3 digits** of the secret (decimal prefix). We need to know their plan in advance, can you use the leaked information to find the **secret key** belonging to **Martian People's Liberation Front (MPLF)** for us to Man-In-the-Middle-ing them ?
> 
> **Given**
> 
> - `ecc.sage` contains the source code of the cryptosystem being used, written by the **Martian People's Liberation Front (MPLF)**
> - `leak.txt` contains the leaked values
> 
> **Goal:** Find the value of `secret` (as a decimal integer) belonging to Martian People's Liberation Front (MPLF) and submit it as a flag.
> 
> **Format flag:**
> 
> ```
> NexusCTF{<secret_in_decimal>}
> ```
> 
> Example: `NexusCTF{12345678}`

---
> [!success] Flag: ``

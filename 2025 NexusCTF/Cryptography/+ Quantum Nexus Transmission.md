> [!abstract] Challenge Description
> > Jerry Vu
> ## 50
> The United Planetary Defense Coalition (UPDC) has been intercepting enemy transmissions across the quantum communication grid. Our intelligence team captured an encrypted message between two command stations that appears to contain coordinates to a critical supply depot. The enemy is using an outdated encryption method: a simple shift cipher that rotates each letter by a fixed number of positions in the alphabet. Your mission is to decrypt this transmission and locate the supply depot coordinates.
> 
> The message is: `zv_lhzf_iyv`
> 
> The flag format is: `NexusCTF{<message>}`

Looks like a [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher), or [substitution cipher](https://en.wikipedia.org/wiki/Substitution_cipher).
Using [CyberChef](https://gchq.github.io/CyberChef/#recipe=ROT13_Brute_Force(true,true,false,100,0,true,'')&input=enZfbGh6Zl9peXY), we brute force ROT13 and search for a legible result.

On rotation $19$, we find the message: `so_easy_bro`.

---
> [!success] Flag: `NexusCTF{so_easy_bro}`

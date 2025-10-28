> [!abstract] Challenge Description
> > @Deputy_Doge
> ## 25
> Following the compromise of Lytton Labs, our security analysts compiled a list of suspicious files that could be related to the breach. You have been called in as the resident malware expert in order to determine if the executable is indeed malicious and, if so, what signatures can we extract in order to detect other compromised hosts.
> 
> Find the flag labeled `flag 00` and submit the flag as `deadface{here-is-the-answer}`.

Downloading the file (you gotta get past windows defender too, but honestly just do on linux), we see an AES encrypted zip file, which requires a password.

Strings shows nothing. 

Running `zip2john` and running john shows us the password `infected`.
Unzipping gives us the `flag.txt`

---
> [!success] Flag: `deadface{Hello_my_friend}`

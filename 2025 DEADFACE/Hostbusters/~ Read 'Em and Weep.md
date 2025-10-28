> [!abstract] Challenge Description
> > @syyntax
> ## 70
> `mirveal` has an encrypted file on the system that we need access to. Find a way to read the `hostbusters6.bin` file.
> 
> Submit the flag as `deadface{flag_text}`.
> 
> Use the connection information from [[+ Let Me In]].

Navigating to `mirveals` home directory shows the `hostbusters6.bin`. An encrypted file. Luckily theres the `.keys` folder which contains private and public keys.

```
openssl pkeyutl -decrypt -in hostbusters6.bin -inkey .keys/private.pem -out decrypted_file.txt
Could not open file or uri for loading private key from .keys/private.pem
28AB07B7047F0000:error:8000000D:system library:BIO_new_file:Permission denied:crypto/bio/bss_file.c:67:calling fopen(.keys/private.pem, rb)
28AB07B7047F0000:error:10080002:BIO routines:BIO_new_file:system lib:crypto/bio/bss_file.c:77:
pkeyutl: Error loading key
```

We do not have permissions to read the private key, also shown by the permissions.

---
> [!success] Flag: `deadface{hostbusters5_e16a5c8995620a24}`

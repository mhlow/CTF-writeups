> [!abstract] Challenge Description
> > @G2Gh0st
> ## 75
> While doing forensics after a recent DEADFACE attack, the team found a file that was added to the system called `qr_flag.png`. Nothing seems wrong with the file, but we are sure Deadface is doing something with it. Can you figure out how this file has been modified and reveal the hidden secrets?
> 
> Submit the flag as `deadface{flag_text}`.

Scanning the QR code is not the flag. No bitplanes for hidden images, only black and white values.

`strings -n 8 qr_code.png` shows only one string: `IyBwYXlsb2FkLnB5CgpkYXRhID0gIjY0IDY1IDYxIDY0IDY2IDYxIDYzIDY1IDdiIDQ1IDVhIDcwIDZlIDY3IDQ4IDMxIDY0IDMxIDZlIDY3IDdkIgoKZmxhZyA9IGJ5dGVzLmZyb21oZXgoZGF0YSkuZGVjb2RlKCkKcHJpbnQoZmxhZykK` decoding from [base64](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=SXlCd1lYbHNiMkZrTG5CNUNncGtZWFJoSUQwZ0lqWTBJRFkxSURZeElEWTBJRFkySURZeElEWXpJRFkxSURkaUlEUTFJRFZoSURjd0lEWmxJRFkzSURRNElETXhJRFkwSURNeElEWmxJRFkzSURka0lnb0tabXhoWnlBOUlHSjVkR1Z6TG1aeWIyMW9aWGdvWkdGMFlTa3VaR1ZqYjJSbEtDa0tjSEpwYm5Rb1pteGhaeWtL&ieol=CRLF) gives a short python snippet.

```py
# payload.py

data = "64 65 61 64 66 61 63 65 7b 45 5a 70 6e 67 48 31 64 31 6e 67 7d"

flag = bytes.fromhex(data).decode()
print(flag)
```

---
> [!success] Flag: `deadface{EZpngH1d1ng}`

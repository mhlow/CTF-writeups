> [!abstract] Challenge Description
> > @3.14ro
> ## 30 
> A DEADFACE member landed an interview at Spooky Coffee using a resume that whispers in Unicode and charms every AI it touches. Those who can read between the glyphs say it speaks in riddles, crafted to bypass filters and impress any CAPTCHA-checking HR daemon.
> 
> Analyze the resume PDF. Can you find the secret string?
> 
> Submit the flag as `deadface{here_is_the_answer}`.

Viewing the metadata of the pdf shows some weird characters.

> [!info] Weird Characters
> ![[Creepy Resume Weird Characters.png]]

Recalling from a forum thread that talked about hiding messages in [emojis](https://paulbutler.org/2025/smuggling-arbitrary-data-through-an-emoji/), putting this emoji shows the flag.

---
> [!success] Flag: `deadface{Look_@_m3!!!}`

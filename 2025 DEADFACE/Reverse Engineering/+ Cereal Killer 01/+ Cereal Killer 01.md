> [!abstract] Challenge Description
> > @TheZeol0t
> ## 75
> The Tech Bro AI Moguls are now getting in on the act! They all want to have favorite, spooky cereals, too! Unfortunately, since they can’t decide which they like the best, they are asking their respective LLMs.
> 
> Mr. Sam Altman, CEO of OpenAI, has a favorite “spooky” cereal. Choose your poison, Windows or Linux, and see if you can figure out which “spooky” (there it is again) he likes the best!
> 
> (You only need to choose one platform.)

We are given an executable file. 
This is its result when running.
```sh
This year, AI moguls are asking their LLMs which spooky cereal is best!
Mr. Sam Altman. has a favorite spooky cereal.  Tear apart this
binary and see if you can figure out what it is!


Please enter the password: hello!
ACCESS DENIED: I'm sorry, Sam, I'm AFRAID I can't DO that...
```

After decompiling in Ghidra, we see that the program essentially comparing the MD5 of my input to their stored MD5. 
> [!info] Decompilation
> ![[Cereal Killer 01 Decompilation.png]]

At the start, we see that the do while loop actually grabs every second value from an array starting at 42. Looking at the `amho16` array we see that it is

```
[4f, 00, 6e, 00, 65, 00, 20, 00, 73, 00, 74, 00, 65, 00, 70, 00, 20, 00, 63, 00, 6c, 00, 6f, 00, 73, 00, 65, 00, 72, 00, 2e, 00, 2e, 00, 2e, 00, 20, 00, 3a, 00, 20, 00, 61, 00, 65, 00, 65, 00, 31, 00, 65, 00, 65, 00, 35, 00, 32, 00, 36, 00, 32, 00, 37, 00, 35, 00, 37, 00, 63, 00, 66, 00, 36, 00, 37, 00, 62, 00, 36, 00, 31, 00, 39, 00, 66, 00, 66, 00, 36, 00, 33, 00, 65, 00, 39, 00, 36, 00, 37, 00, 32, 00, 62, 00, 36, 00, 00, 00]
```

From [hex](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')&input=NGYNCjAwDQo2ZQ0KMDANCjY1DQowMA0KMjANCjAwDQo3Mw0KMDANCjc0DQowMA0KNjUNCjAwDQo3MA0KMDANCjIwDQowMA0KNjMNCjAwDQo2Yw0KMDANCjZmDQowMA0KNzMNCjAwDQo2NQ0KMDANCjcyDQowMA0KMmUNCjAwDQoyZQ0KMDANCjJlDQowMA0KMjANCjAwDQozYQ0KMDANCjIwDQowMA0KNjENCjAwDQo2NQ0KMDANCjY1DQowMA0KMzENCjAwDQo2NQ0KMDANCjY1DQowMA0KMzUNCjAwDQozMg0KMDANCjM2DQowMA0KMzINCjAwDQozNw0KMDANCjM1DQowMA0KMzcNCjAwDQo2Mw0KMDANCjY2DQowMA0KMzYNCjAwDQozNw0KMDANCjYyDQowMA0KMzYNCjAwDQozMQ0KMDANCjM5DQowMA0KNjYNCjAwDQo2Ng0KMDANCjM2DQowMA0KMzMNCjAwDQo2NQ0KMDANCjM5DQowMA0KMzYNCjAwDQozNw0KMDANCjMyDQowMA0KNjINCjAwDQozNg0KMDANCjAwDQowMA&ieol=CRLF&oeol=CRLF), we get "One step closer:  aee1ee5262757cf67b619ff63e9672b6", (null bytes taken out), and starting from 42, its the hash `aee1ee5262757cf67b619ff63e9672b6`.

We now need to see what hashes to this. John on `rockyou.txt` doesn't come up with anything.

This [writeup](https://pingtrip.com/ctf/DEADFACE2022/cerealkiller02) from 2022 contains the same hash, and we can see that the plaintext is `peanutbuttercrunch`. This can also be done using hashcat, although it takes around 5 minutes.

```sh
./mr429yru     
This year, AI moguls are asking their LLMs which spooky cereal is best!
Mr. Sam Altman. has a favorite spooky cereal.  Tear apart this
binary and see if you can figure out what it is!


Please enter the password: peanutbuttercrunch


ChatGPT says: 
The SPOOKIEST cereal is...

*********** (I THINK I MIGHT BE HALLUCINATING) ***********

deadface{Yeah-its-not-a-monster-cereal--Mr-Altman-is----different!}

*********** (I THINK I MIGHT BE HALLUCINATING) ***********
```


---
> [!success] Flag: `deadface{Yeah-its-not-a-monster-cereal--Mr-Altman-is----different!}`



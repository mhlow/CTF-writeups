> [!abstract] Challenge Description
> > @SpiffyLich
> ## 200
> We think we found a secret downloader DEADFACE uses to share their latest tools with each other… But whenever we run it, it just deletes itself! Maybe you can find a way to get something interesting out of this? Enter the answer as `deadface{here-is-the-answer}`.

Decompiling the program, we find that theres a lot of functions. Going to `FUN_00101993` shows us the success message when we break the program. Specifically, it ends with 
```c
    printf("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%s%s@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n",
           &DAT_001060b0,&DAT_001060d0);
```

Going to where these variables are stored and extracting the values, we get
`babbbfbab8bfbdbba5a9efacedeb81bdeeb0b0edbde9edba8100000000000000`
and
`9cd998f299e19cfb9e8c8c8cd00000000820100000000000`
Removing trailing `0`'s and getting from hex, we see that the binary looks kind of in the right format for text, namely starting with `101...`. 
This had cause for me to check XOR, bruteforcing showed the key for the first string was `de` and `ad` for the second. Putting them together gives our flag.


---
> [!success] Flag: `deadface{w1r35_c0nn3c73d_1t5_4L1V3!!!}`

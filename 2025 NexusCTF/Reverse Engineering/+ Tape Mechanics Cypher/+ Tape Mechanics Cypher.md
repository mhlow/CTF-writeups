> [!abstract] Challenge Description
> > Nguyen Vu An Nhan
> ## 100
> The Ætheric Order speaks in riddles; their messages are woven through strange notations and stranger machines. One of those transmissions — a short, iridescent packet — was never meant for the light of day, but the Beltway Bandit yanked it from the noise and brought it to you. They’re not linguists. They’re not archivists. They’re collectors who buy usefulness with cash, and usefulness is what they want now.
> 
> What the Bandit has: a single cypher blob written in an esoteric dialect and an emulator that will run it. The code’s internals are obtuse and academic; static inspection only provokes headaches. Fortunately, the emulator is honest: feed it an input, observe the tape. The Bandits learned one curious fact by accident — sending "PDOSN#" through the emulator produces the plaintext "HELLO". That sample is all they kept; the rest is salvage.
> 
> What the Bandit wants you to do is straightforward and dangerous-sounding in equal measure: use the emulator and the sample to forge a different Ætheric directive. Produce an input which, when the cypher runs, yields the message:
> 
> "NO AMBUSH DO PROCEED"
> 
> Do that, hand the forged message to the Beltway Bandit, and they’ll pay handsomely for the favor. Fail, and you’ll be left with smoke, static, and the nagging sense that one more pattern went unread.
> 
> Tools provided: the intercepted cypher blob and a faithful emulator. No source-level hints. No helpful comments. Just observation and experimentation. The Order’s machine is merciless — but it speaks if you ask the right questions.
> 
> Access the emulator [here](https://morphett.info/turing/turing.html)
> 
> The flag format is: `NexusCTF{<message>}`
> 
> Example format: `NexusCTF{this is example flag}`

This is clearly a Turing Machine.
Putting our program into the emulator verifies that indeed `PDOSN#` results in `HELLO`.

From inspecting the instructions, all instructions will proceed to the right, except for the final halting state when reading `#`. This makes this a lot easier to crack, as each character is only read once.

Sorting the instructions draws a very clear picture of what is happening.
State `g7a` (starting state) always flows into `h3b` which flows into `k9c` in a cycle. Looking at what happens under the cursor of the machine, each state does different things

- `g7a`: `ABCDE` $\mapsto$ `QWERT`
- `h3b`: `ABCDE` $\mapsto$ `BCDEF`
- `k9c`: `ABCDE` $\mapsto$ `ZYXWV`

```python
decode = "NO AMBUSH DO PROCEED"
# pattern every third character, 
# map from qwerty to abcde
# map shift back by 1, bcdef to abcde
# map flip alphabet, zyxwv to abcde
# anything else ignore
qwerty = "QWERTYUIOPASDFGHJKLZXCVBNM"
abcde = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
bcdef = "BCDEFGHIJKLMNOPQRSTUVWXYZA"
zyxwv = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
for i in range(len(decode)):
    if decode[i] == " ":
        print(" ", end="")
        continue
    if i % 3 == 0:
        print(abcde[qwerty.index(decode[i])], end="")
    elif i % 3 == 1:
        print(abcde[bcdef.index(decode[i])], end="")
    else:
        print(abcde[zyxwv.index(decode[i])], end="")
print()
```

The output is `YN KLYGRS CL OIIBVCC`. Remember the halting character.

---
> [!success] Flag: `NexusCTF{YN_KLYGRS_CL_OIIBVCC#}`

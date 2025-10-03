> [!abstract] Challenge Description
> > Erik Hai
> ## 100
> Upon entering the correct flag sequence into the relay dashboard, the terminal went silent. For a moment, nothing happened. Then the interface flickered, lights along the edge of the console ignited, and a low-frequency hum began to resonate from deep within the core systems.
> 
> Lines of dormant code scrolled across the display: ancient routines buried under decades of decay. A secondary process came online. The system had been waiting, dormant and listening, for a specific input… and you just triggered it.
> 
> A new directive surfaced. No metadata. No timestamp. Just a single message stamped with an authentication header older than any known federation protocol.
> 
> Whatever this is, it was never meant to be found casually. Someone or something left it behind, locked beneath layers of obfuscation, waiting for the right operative to respond.
> 
> The message is short. Encrypted. Purposefully buried beneath layers of outdated encoding.
> 
> Someone once thought this was important enough to hide from machines built to find everything.
> 
> Now it's yours.
> 
> Will you follow the trail?
> 
> **Note**: The more failed submissions, the more points lost to the void
> 
> The flag format is: `NexusCTF{<flag>}`
> 
> > [!question] System Alert 1 (Cost: 20 points)
> 
> > [!question] System Alert 2 (Cost: 30 points)

We are given four files, `enc_payload_1.txt`, `federation.db`, `hexdump.sig` and `system_log.txt`.

## enc_payload_1.txt
`5ZTwwl87YEX2OrymxckzH2Goj5Tm86ybYHmqah7cWritjtoBYrcpr3qh5iYG+Nz7jh/2VjEXAV4kCIA/afLrEqtyw5e6K2LCjzS5YVWb3UkdNSYqx8qQUZHEV5UpvT2NDWPlJ1EDJQgfcWM23WWMhiHY9/LI2CC64GT6/PtO358=`
We are given this (probably) Base64 encrypted payload. Decrypting directly from Base64 does not yield anything useful.
We probably need a key to decrypt this.

## federation.db
This is a SQLite database. [Inspecting](https://inloop.github.io/sqlite-viewer/) the tables, we have a table called `epsilon_flags`


| **id** | **name**   | **flag**              | **location**                              |                                           |
| ------ | ---------- | --------------------- | ----------------------------------------- | ----------------------------------------- |
| 1      | Epsilon-1  | dOR_Yi~l`ehy          | dOR_Yi~ldOR_Yi~l                          |                                           |
| 2      | Epsilon-2  | dOR_Yi~l~oy~          | dOR_Yi~l`ehfoyy                           |                                           |
| 3      | Epsilon-3  | dOR_Yi~lfohxed~bomek~ | dOR_Yi~lmc                                | ooxcabkckyel~}kxomxkn  k~o`ehzfokyochomse |
| 4      | Epsilon-4  | dOR_Yi~lishoxyei      | dOR_Yi~l`oxxs~bomek~                      |                                           |
| 5      | Epsilon-5  | dOR_Yi~lbkyykd~bomek~ | dOR_Yi~l~oxxs~bomek~                      |                                           |
| 6      | Epsilon-6  | dOR_Yi~l~oxxs~bomek~  | dOR_Yi~lbkyykd~bomek~                     |                                           |
| 7      | Epsilon-7  | dOR_Yi~l`oxxs~bomek~  | dOR_Yi~lishoxyei                          |                                           |
| 8      | Epsilon-8  | dOR_Yi~lmc            | ooxcabkckyel~}kxomxkn  k~o`ehzfokyochomse | dOR_Yi~lfohxed~bomek~                     |
| 9      | Epsilon-9  | dOR_Yi~lehfoyy        | dOR_Yi~l~oy~                              |                                           |
| 10     | Epsilon-10 | dOR_Yi~ldOR_Yi~l      | dOR_Yi~l`ehy                              |                                           |

Since we are looking for a flag, I assumed the first few characters aligned with `NexusCTF`. Brute forcing the Vigenere cipher key yields nothing. We try XOR brute force on the `flag` column and find the key `2a`, resulting in 
`NexusCTFJOBS NexusCTFTEST NexusCTFLEBRONTHEGOAT NexusCTFCYBERSOC NexusCTFHASSANTHEGOAT NexusCTFTERRYTHEGOAT NexusCTFJERRYTHEGOAT NexusCTFGIVEERIKHAIASOFTWAREGRADUATEJOBPLEASEIBEGYOU NexusCTFJOBLESS NexusCTFNexusCTF` respectively.

This does not seem like the right path.

## hexdump.sig
``]RkB`tGqhpZaVzVvYxQJ``
Base64 doesn't work.
[XOR](https://gchq.github.io/CyberChef/#recipe=XOR(%7B'option':'Hex','string':'1337'%7D,'Standard',false)XOR_Brute_Force(2,200,0,'Standard',false,true,false,''/disabled)&input=XVJrQmB0R3FocFphVnpWdll4UUo) brute force with a key length of $2$ shows `NexusCTF{GIVEMEAJOB}` with a key of `1337` (hex).

## system_log.txt
This appears to be a system log, with some debug codes and messages.
Initial thoughts it could be some sort of substitution cipher, but not entirely enough words to map to something useful.
```
00001: Service stopped
# DEBUG-CODE: 1337
00002: packet info warning warning request debug process client debug timeout warning timeout error system timeout server error process system packet response request network client packet info error info success warning request response error success error server packet request system success timeout packet packet info warning client thread info system warning
... (truncated for brevity) ...
```

# Finding the flag
We only have one potential flag that is in the right format. Trying that as the flag is successful

---
> [!success] Flag: `NexusCTF{GIVEMEAJOB}`

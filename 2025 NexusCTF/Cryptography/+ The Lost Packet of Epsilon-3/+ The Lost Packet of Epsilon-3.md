> [!abstract] Challenge Description
> > Erik Hai
> ## 100
> A fragmented data packet was recovered from the wreckage of a long-abandoned comms satellite drifting through the outer relay mesh. The timestamp suggests it was transmitted over 200 years ago, but never reached its destination.
> 
> - Packet integrity: Partially preserved
> - Signal encryption: Obsolete Earth-era formats
> - Purpose: Unknown
> 
> The payload appears to be layered in multiple legacy obfuscation methods, likely used to bypass now-extinct surveillance AI. What could be contained inside?
> 
> If specified otherwise, the flag format is: `NexusCTF{<flag>}`

We see a range of different files. 
The `README.txt` tells us that there are many false positives.

## The Right File
Many of the files are red herrings, and result in a fake flag. 
The only file that matters are both `recovered.bin` and `packet_analysis.log`, which is a log file between two people, discussing the methods used to decrypt a few files.

Just based on the string from `recovered.bin`, we decode from hex, then from Base64, then notice the parenthesis and reverse the string.
Next we tried to brute force ROT13, but no visible results. The file mentions a key `ECHO` and so putting that into vigenere we get our flag `NEXUSCTF{INEEDJOB}` 

[CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')From_Base64('A-Za-z0-9%2B/%3D',true,false)Reverse('Character')Vigen%C3%A8re_Decode('echo')&input=NjY1NjQyNTc1NDQ1Njg1NDU0NDY0MjRlNjUzMTUyNDI1MjU2NjQ0YTUyNTU2NDUz)

---
> [!success] Flag: `NEXUSCTF{INEEDJOB}`

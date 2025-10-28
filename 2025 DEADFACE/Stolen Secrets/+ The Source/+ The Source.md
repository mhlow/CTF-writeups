> [!abstract] Challenge Description
> > @syyntax
> ## 5
> A department at TGRI was getting lazy with sensitive files. Rather than use the company’s approved filesharing application, a member used an application called MyShare and forgot to configure it to run HTTPS.
> 
> DEADFACE found the site and were able to compromise it and steal several sensitive files. Based on DEADFACE’s past behavior, let’s assume that flags discovered may be used as DEADFACE passwords.
> 
> First thing’s first: what is the IP address of the DEADFACE attacker? Submit the flag as `deadface{X.X.X.X}`.

Opening the file shows a bunch of log files and a `.pcap` file, which we can open in WireShark.

Looking through all three logs, it is clear that `134.199.202.160` tried a brute force attack and was disconnected.


---
> [!success] Flag: `deadface{134.199.202.160}`

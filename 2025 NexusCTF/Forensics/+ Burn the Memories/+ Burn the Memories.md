> [!abstract] Challenge Description
> > Anonymous
> ## 100
> Polaris Logistics prides itself on precision: every crate tallied, every joule accounted for. But this week, something strange surfaced deep inside their systems. Several freighter processes began consuming far more memory than they were ever allocated, as if phantom cargo had been slipped into the hold.
> 
> The lead engineer—reeling from a recent breakup—has excused themselves from the investigation, leaving management anxious. With supply lines at risk and suspicion falling on insider tampering, Polaris has turned to you. They’ve provided a stack and heap dump of the anomalous process. Somewhere in those memory images lies the truth: whether sabotage, smuggling of digital contraband, or something more insidious.
> 
> Your mission: analyze the dumps, uncover what’s bloating memory, and report your findings. Polaris is willing to pay handsomely… if you can keep their lifeline secure.
> 
> The flag format is: `NexusCTF{<message>}`

Opening the zip file shows two files, `stack.bin` and `heap.bin`.
Running `strings -n 8 | grep -i Nexus` gives our flag.


---
> [!success] Flag: `NexusCTF{s0m3_m3m0ri3s_4r3_unf0rg3774bl3}`

> [!abstract] Challenge Description
> > Wahyu Mahendra
> ## 150
> Year 2100. A Polaris Logistics freighter (callsign PLR-Auriga-47) reported intermittent packet loss near the Belt, then flagged an anomaly on its Quantum Nexus edge node. Minutes later, cargo routing systems glitched and a manifest entry vanished.
> 
> Polaris suspects a quiet snatch-and-grab by the Beltway Bandits: data pulled over a routine service channel and buried under a storm of normal web traffic. Your crew was paid to reconstruct what left the ship-fast-before the UPDC steps in and locks the case.
> 
> The flag format is: `NexusCTF{<message>}`
> 
> Example format: `NexusCTF{this_is_a_flag}`

Opening in wireshark, searching packet info for `NexusCTF` gives a bunch of false positives, but also `NexusCTF{plain_http_is_pain}`

---
> [!success] Flag: ``

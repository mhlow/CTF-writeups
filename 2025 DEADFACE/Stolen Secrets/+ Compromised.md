> [!abstract] Challenge Description
> > @syyntax
> ## 30
> Which user did DEADFACE compromise and what was that user’s password?
> 
> Submit the flag as `deadface{username_password}`. Example: `deadface{user01_P@$$w0rd!}`
> 
> > Use the ZIP file from [[+ The Source]]

Inspecting the `.pcap` file, we see a large http request stream where the attacker got in. In the early requests, we see the post request with his login details

---
> [!success] Flag: `deadface{bsampsel_Sparkles2025!}`

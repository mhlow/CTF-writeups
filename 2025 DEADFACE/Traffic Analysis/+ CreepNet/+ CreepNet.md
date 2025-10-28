> [!abstract] Challenge Description
> > @AstralByte
> ## 50
> We know that DEADFACE communicated back to one of their servers, but we're not sure how they did it. The junior analyst over at De Monne Financial doesn't see any communications through standard channels in their network traffic. So, how is DEADFACE communicating? See if you can find the message.
> 
> Submit the flag as `deadface{flag text}`.

Looking through the packet capture, nothing obvious, a lot of encrypted messages.

Since I know I'm looking for `deadface` somewhere, I hexed and base64 searched for those strings, base64 coming up positive in a DNS request.
`ZGVhZGZhY2V7SXRzX0lt.com`
This give the first half of the flag `deadface{Its_Im`

This means that they are probably communicating through DNS requests.
Filtering by DNS, another few suspicious queries comes up.
`aC1FdmVyeWQzdEBpbH0K.com`
`cDBydGFudC1UMC5jQHRj.com`
Giving reordering, stripping `.com` and decoding from base64 gives our flag.



---
> [!success] Flag: `deadface{Its_Imp0rtant-T0.c@tch-Everyd3t@il}`

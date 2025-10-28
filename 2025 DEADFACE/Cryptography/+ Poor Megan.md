> [!abstract] Challenge Description
> > @TheZeal0t
> ## 10 
> Oh, NO! Poor MEGAN! She's just been bitten by a ZOMBIE! We can save her if we act fast, but the formula for the antidote has been encoded somehow. Figure out how to unscramble the formula to save Megan from certain zombification.
> 
> Submit the flag as `deadface{here-is-the-answer}`.
> 
> The formula for the antidote:
> `jLfXjLjXiwfBRdi9lx49nwKslcvxih=1mYval2e9nLfXmxGalwy9lwi9lLf9lwy9nMnaQh=1ihSqlwDVmsvajYvXmMG8jcvZkg=1mYvwkgz1jwKspb55`
> 
> QUICK! She’s starting to GURGLE!!!

Putting this into cyberchef, from base64 yields nothing, but this still looks like base64.

For some reason I see the `Magic` feature and using it reveals the flag.
It is base64 but with a different alphabet. I have no idea how to solve it otherwise.
Alphabet: `3GHIJKLMNOPQRSTUb=cdefghijklmnopWXYZ/12+406789VaqrstuvwxyzABCDEF5`

[CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Base64('3GHIJKLMNOPQRSTUb%3DcdefghijklmnopWXYZ/12%2B406789VaqrstuvwxyzABCDEF5',true,false)&oeol=FF)

---
> [!success] Flag: `deadface{16-oz-warm-water-one-teaspoon-of-lemon-two-teaspoons-of-apple-cider-vinegar}`

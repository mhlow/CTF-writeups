> [!abstract] Challenge Description
> > Nguyen Vu An Nhan
> ## 50
> In the shifting corridors of the Quantum Nexus, the Ætheric Order has found a signal wrapped in a thousand tongues. They call it the Tower of Babel: a transmission that should be uniform, but instead splinters into fragments of meaning. Most dismiss it as noise, the byproduct of mismatched systems. The Order insists otherwise — that within the confusion lies intent, a message waiting for those willing to look past the obvious.
> 
> [Transmission here](https://www.youtube.com/watch?v=lMm1P16OB5Q).
> 
> The flag format is: `NexusCTF{<message>}`

The link brings us to an unlisted youtube video, appearing to be an unchanging black screen with the words "Lingua Franca" in the bottom right.
This roughly translates to a language that is adopted as a common language between speakers whose native languages are different.

> [!info] Youtube Video
> ![[The Tower of Babel Video Screenshot.png]]

Inspecting the description or comments yields nothing, however there is a transcription of the video.

The default transcription in *English (Australia)* shows at `0:02`: `-- .- -. -.-- /`. This is obviously [Morse code](https://en.wikipedia.org/wiki/Morse_code).

Transcribing this gives "many /". Clearly there is more to find.

We can then attempt to change the language of the transcription, and show us 
- **English (United Kingdom)** at `0:02`: `-- .- -. -.-- /`
- **English (Canada)** at `0:04`: `.-.. .- -. --. ..- .- --. . ... /`
- **English (India)** at `0:06`: `--- -. . /`
- **English (Ireland)** at `0:08`: `.-. . .--. .-. . ... . -. - .- - .. --- -.`

Altogether, this gives us the message "many languages one representation".


---
> [!success] Flag: `NexusCTF{many languages one representation}`

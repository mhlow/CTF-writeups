> [!abstract] Challenge Description
> > Yash Parmar
> ## 125
> The UPDC has sent out a secure transmission regarding it's operations using an image this time. The transmission has key information about planetary patrol shifts across the galaxy. Use your skills to identify patrol routes and intercept the comms.
> 
> The flag format is: `NexusCTF{<flag>}`

![[secure_transmission.jpeg]]
Running `file` on this image gives: `secure_transmission.jpeg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 96x96, segment length 16, comment: "Passphrase = updc_patrol_route", baseline, precision 8, 946x949, components 3`

Clearly there's some sort of steganography with a passphrase.
`steghide extract -sf secure_transmission.jpeg -p updc_patrol_route`

Wrote `NexusCTF{updc_secure_transmission}` to `flag`


---
> [!success] Flag: `NexusCTF{updc_secure_transmission}`

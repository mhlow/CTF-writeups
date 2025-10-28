> [!abstract] Challenge Description
> > @syyntax
> ## 80
> DEADFACE left behind this strange image of a frog with the message:
> 
> > “The frog has many secrets, but he’ll only tell you if you make him smile.”
> 
> There’s obviously more to this image than we can see here. Figure out if you can find the flag associated with this image. Submit the flag as `deadface{flag text}`.

`pngcheck` or `exiftool` shows that there is additional data after `IEND` chunk.

Running `binwalk` confirms this. Had to rummage around trying to get the right flags cus it wasn't extracting the gif it detected.
`binwalk -e --dd=".*" froggy-step.png`

Converting the `12AB25` to a gif shows the flag.

---
> [!success] Flag: `deadface{surPr1s3D_Fr0ggy}`

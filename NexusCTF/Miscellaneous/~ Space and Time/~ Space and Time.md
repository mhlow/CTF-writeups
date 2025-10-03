> [!abstract] Challenge Description
> > Nguyen Vu An Nhan
> ## 100
> From the shattered remains of a museum once devoted to the history of computing, the Order has recovered a curious fragment of binary code. The archivists whisper that it encodes the lineage of displays—a sequence bridging the clunky digits of the past to the luminous alphabets of the present.
> 
> Yet something resists clarity. When rendered directly upon a 7-segment display, the fragment yields only half-messages. The Order suspects this is no accident: true progress always passes through an intermediate technology, each generation building upon the last. To reveal the intended message, one must retrace this evolutionary path—convert, transform, and adapt the fragment as the engineers of old once did.
> 
> Bring the hidden text into the light, and the Order will reward you well. Fail, and the message will remain locked, just another ghost in the circuitry.
> 
> The flag format is: `NexusCTF{<message>}`

We are provided with `space_and_time.bin` which is a pure data file.

```xxd
00000000: 797d 795e 795e 715e 797d 7106 797d 4f6f  y}y^y^q^y}q.y}Oo
00000010: 795e 795e 795e 797d 797d 7907 797d 7106  y^y^y^y}y}y.y}q.
00000020: 797d 716f                                y}qo
```

>[!Question]- View Hint: Hint
> 
> There are many displays between the 7-segment and the 21st centyury's dot matrix. The old archive once known as Wikipedia may provide the right hardware used to encode this intermediate step.

Did basic research on 7 segment and dot matrices and gave up.

---
> [!failure] Flag: ``

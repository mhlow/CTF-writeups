> [!abstract] Challenge Description
> > Farel Z Andarya
> ## 225
> A cold signal blinked into the Quantum Nexus at 03:14 UTC, a faint identifier and a photograph of a rusted pylon tag: S38+688.
> 
> Polaris Logistics reports that a _freight train_ passing near Earth picked up a scavenged sensor array broadcasting what looks like an old maintenance tag. The Ætheric Order, ever hungry for anomalies, insists the tag marks the last known transmission point of something very important — an object the Order calls “the Beacon”. Polaris calls it scrap. The United Planetary Defence Command calls it harmless paperwork.
> 
> We call it a job.
> 
> Your task: identify where that pylon tag would be found in the Old World maps — then report the precise coordinates of the last-known location. The Nexus needs this item accounted for before someone less scrupulous finds it.
> 
> What to submit: A single coordinate in decimal degrees (latitude,longitude) that matches the location identified by the pylon tag photo. Round it to 3 numbers after the decimal point.
> 
> Format is: `NexusCTF{<Lat,Long>}`

## What is the tag?
![[Screenshot_2025-10-01_001407.png]]
Reverse image searching this image (on google) results in only one similar looking sign, coming from a document about [Description and Labelling of the 1500 Volt DC OHW System](https://railsafe.org.au/_media/documents/electrical/one-method-of-safe-working/SP-D-79044-Description-and-Labelling-of-the-1500-Volt-DC-OHW-System.pdf) as part of an Electrical Network Safety Booklet.

From this we can see that these are labels for OHW structures for Sydney train lines, matching up with the description on the task.

## Understanding the Label
To get a better grasp of what the numbers meant, we go to another website, specifically attaining the pdf for [[T HR EL 08005 ST_1.00_Labels for OHW Structures.pdf|Labels for OHW Structures]].

In this document, most importantly at the bottom of it, it shows that the letter at the beginning specifies the train line, and the numbers display how far along one is on the line.

We find that the trainline extends from Glenlee to Libcombe NSW.

## Locating the Sign
First thing that came to mind was to see if we could even see a similar sort of sign, as if we couldn't we would have to take a different path.  

The first Google maps spot chosen was at [Menagle Station](https://www.google.com/maps/place/Menangle/@-34.1256946,150.7439469,3a,75y,123.76h,87.72t/data=!3m7!1e1!3m5!1so0VFHYQeNn25mbJ7J81ROg!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D2.2784485244584403%26panoid%3Do0VFHYQeNn25mbJ7J81ROg%26yaw%3D123.75857747640131!7i16384!8i8192!4m23!1m16!4m15!1m6!1m2!1s0x6b12f10043c6cf97:0x733c016f000516d0!2sGlenlee,+Menangle+Park+NSW!2m2!1d150.7604084!2d-34.091932!1m6!1m2!1s0x6b12bb5ec3bbec53:0x5017d681632be40!2sLidcombe+NSW!2m2!1d151.0423034!2d-33.8616915!3e0!3m5!1s0x6b12fae806330287:0x1d017d6903797e00!8m2!3d-34.125561!4d150.7441319!16zL20vMGI4eW42?entry=ttu&g_ep=EgoyMDI1MDkyOC4wIKXMDSoASAFQAw%3D%3D). We knew it had to be along a train line, and that a station was our best bet.

Looking around the area, we see a very similar - no, the *same* type of fence, a promising find.
> [!info] Menangle Fence
> ![[Menangle Fence.png]]

However, there is nothing else of interest around here. 
Moving up the train line, we keep seeing the similar looking fences, however no sign of the train line tags.

A random shout from my friend (who I recruited to help me on this task) announced that they found the *exact type* of sign, showing that we were indeed really close to the location.

> [!info] Macquarie Fields Station
> ![[Macquarie Fields Station.png]]

From here, it was just a matter of going down the line (in the right direction), and finding out sign at **Casula Station**.

Latitude, Longitude: -33.9492901,150.9121376

---
> [!success] Flag: `NexusCTF{-33.949,150.912}`

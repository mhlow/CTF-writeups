> [!abstract] Challenge Description
> > Jose Setiawan and Wahyu Mahendra
> ## 450
> The Quantum Nexus Network flagged an unusual relay during Sable’s escape. A witness named Anthony Mark scattered his trail online. He avoided mainstream platforms, instead favoring a regional forum rooted in the land where the eruption that caused the “Year Without a Summer” once shook the world. Use open-source techniques to follow the clues and find Sable’s 'last' known physical location.
> 
> The flag format is: `NexusCTF{<Last_Location>}`
> 
> For example: `NexusCTF{Sydney_Opera_House}`

First thing that sticks out is *a regional forum rooted in the land where the eruption that caused the "Year Without a Summer"*. Doing basic research tells us that we are looking at modern day Indonesia. 

A popular Indonesian forum [Kaskus](https://www.kaskus.co.id) has a few users similar to Anthony Mark, specifically [anthonymark17](https://www.kaskus.co.id/@anthonymark17?ref=header&med=search) holds interest, as it is English and one of the posts mentioned `1337`. 

Going to [this](https://www.kaskus.co.id/thread/68c978ec767b4c31640cc7cd) post indeed confirms our suspicions as it mentioned a "Sable".

The post is below.
> [!info]
> Also — Sable always chased salt. Found an old snap of his ‘favourite spot’ — gold sign. I saved the post; someone who knows classic food places might recognise it. I guess even the review of the place was pretty good. He has a good taste for an outsider.
> ![[anthonymark17 Post Image.png]]

Clearly this is [Golden Seafood](https://www.click2houston.com/news/2018/09/27/restaurant-report-card-roaches-slime-found-by-health-inspectors-at-local-eateries/) from reverse image search.
This gives us a location in [Texas](https://www.google.com/maps/place/Golden+Seafood/@29.8084701,-95.3829829,18.5z/data=!4m6!3m5!1s0x8640b88fbe630539:0x716c0484de437951!8m2!3d29.8086435!4d-95.3824543!16s%2Fg%2F1tc_ljbb?entry=ttu&g_ep=EgoyMDI1MDkyOC4wIKXMDSoASAFQAw%3D%3D)



---
> [!failure] Flag: ``

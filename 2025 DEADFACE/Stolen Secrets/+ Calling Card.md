> [!abstract] Challenge Description
> > @syyntax
> ## 5
> DEADFACE has left a taunting message in their initial probing of the MyShare web application at [http://files.techglobalresearch.com](http://files.techglobalresearch.com/). Their attack involves a simple HTTP request with a hidden flag. Can you uncover their calling card?
> 
> Submit the flag as `deadface{text}`
> 
> > Use the ZIP file from [[+ The Source]]

Inspecting the `.pcap` file, the first http request has the hidden message, in the headers in the flag.

---
> [!success] Flag: `deadface{l3ts_get_Th3s3_fiL3$}`

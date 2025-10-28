> [!abstract] Challenge Description
> > Jerry Vu
> ## 175
> Year 2100. UPDC's defense node runs outdated authentication. Exploit the memory vulnerability to bypass security. Below is a code segment that was retrieved by a spy. Your job is to find the flag.
> 
> ```
> int main() {
>     char password[10];
>     int admin = 0;
>     
>     cout << "Enter password: ";
>     scanf("%s", password);
>     
>     if (admin == 0x41424344) {
>         displayFlag();
>     }
>     
>     return 0;
> }
> ```
> 
> Beware of padding and endianness. The program supposedly runs on an ancient distribution called Ubuntu. Access the challenge [here](http://34.129.100.231:5055/).
> 
> Flag format is: `NexusCTF{<flag>}`

This was an extremely easy buffer overflow attack. 
`aaaaaaaaaaDCBA` (little endian) gave us the flag.

---
> [!success] Flag: `NexusCTF{b@ffer_0verfl0w_m4st3r}`
